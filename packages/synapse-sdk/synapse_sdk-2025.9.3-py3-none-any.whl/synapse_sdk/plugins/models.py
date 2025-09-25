import os
from functools import cached_property
from typing import Any, Dict

from synapse_sdk.clients.backend import BackendClient
from synapse_sdk.devtools.config import get_backend_config
from synapse_sdk.loggers import BackendLogger, ConsoleLogger
from synapse_sdk.plugins.utils import read_plugin_config
from synapse_sdk.shared.enums import Context
from synapse_sdk.utils.storage import get_storage
from synapse_sdk.utils.string import hash_text


class PluginRelease:
    config: Dict[str, Any]
    envs = None

    def __init__(self, config=None, plugin_path=None, envs=None):
        if config:
            self.config = config
        else:
            self.config = read_plugin_config(plugin_path=plugin_path)
        self.envs = envs

    @cached_property
    def plugin(self):
        return self.config['code']

    @cached_property
    def version(self):
        return self.config['version']

    @cached_property
    def code(self):
        return f'{self.plugin}@{self.version}'

    @cached_property
    def category(self):
        return self.config['category']

    @cached_property
    def name(self):
        return self.config['name']

    @cached_property
    def package_manager(self):
        return self.config.get('package_manager', 'pip')

    @cached_property
    def package_manager_options(self):
        # Get user-defined options from config
        user_options = self.config.get('package_manager_options', [])

        # Ray 2.44.1 only supports uv_pip_install_options, not pip_install_options
        if self.package_manager == 'uv':
            defaults = ['--no-cache']
            # Add defaults if not already present
            options_list = defaults.copy()
            for option in user_options:
                if option not in options_list:
                    options_list.append(option)
            return {'uv_pip_install_options': options_list}
        else:
            # For pip, Ray 2.44.1 doesn't support pip_install_options
            # Return empty dict so no extra options are added
            return {}

    @cached_property
    def checksum(self):
        return hash_text(self.code)

    @cached_property
    def actions(self):
        return list(self.config['actions'].keys())

    def setup_runtime_env(self):
        import ray
        from ray.util.scheduling_strategies import NodeAffinitySchedulingStrategy
        from ray.util.state import list_nodes

        @ray.remote
        def warm_up():
            pass

        extra_runtime_env = {}

        if self.envs.get('SENTRY_INIT_FUNCTION') is not None:
            extra_runtime_env['worker_process_setup_hook'] = self.envs['SENTRY_INIT_FUNCTION']

        nodes = list_nodes(address=self.envs['RAY_DASHBOARD_URL'])
        node_ids = [n['node_id'] for n in nodes]
        for node_id in node_ids:
            strategy = NodeAffinitySchedulingStrategy(node_id=node_id, soft=False)

            warm_up.options(
                runtime_env={
                    self.package_manager: {
                        'packages': ['-r ${RAY_RUNTIME_ENV_CREATE_WORKING_DIR}/requirements.txt']
                        ** self.package_manager_options
                    },
                    'working_dir': self.get_url(self.envs['SYNAPSE_PLUGIN_STORAGE']),
                },
                scheduling_strategy=strategy,
            ).remote()

    def get_action_config(self, action):
        return self.config['actions'][action]

    def get_url(self, storage_url):
        storage = get_storage(storage_url)
        return storage.get_url(f'{self.checksum}.zip')

    def get_serve_url(self, serve_address, path):
        return os.path.join(serve_address, self.checksum, path)


class Run:
    """Run class for manage plugin run istance.

    Attrs:
        job_id: plugin run job id
        context: plugin run context
        client: backend client for communicate with backend
        logger: logger for log plugin run events
    """

    logger = None
    job_id = None
    context = None
    client = None

    def __init__(self, job_id, context=None):
        self.job_id = job_id
        self.context = context or {}
        config = get_backend_config()
        if config:
            self.client = BackendClient(
                config['host'],
                access_token=config['token'],
            )
        else:
            # Handle missing environment variables for test environments
            envs = self.context.get('envs', {})
            host = envs.get('SYNAPSE_PLUGIN_RUN_HOST', os.getenv('SYNAPSE_PLUGIN_RUN_HOST', 'http://localhost:8000'))
            token = envs.get('SYNAPSE_PLUGIN_RUN_USER_TOKEN', os.getenv('SYNAPSE_PLUGIN_RUN_USER_TOKEN'))
            tenant = envs.get('SYNAPSE_PLUGIN_RUN_TENANT', os.getenv('SYNAPSE_PLUGIN_RUN_TENANT'))

            self.client = BackendClient(
                host,
                token=token,
                tenant=tenant,
            )
        self.set_logger()

    def set_logger(self):
        kwargs = {
            'progress_categories': self.context.get('progress_categories'),
            'metrics_categories': self.context.get('metrics_categories'),
        }

        if self.job_id:
            self.logger = BackendLogger(self.client, self.job_id, **kwargs)
        else:
            self.logger = ConsoleLogger(**kwargs)

    def set_progress(self, current, total, category=''):
        self.logger.set_progress(current, total, category)

    def set_metrics(self, value: Dict[Any, Any], category: str):
        self.logger.set_metrics(value, category)

    def log(self, event, data, file=None):
        self.logger.log(event, data, file=file)

    def log_message(self, message, context=Context.INFO.value):
        self.logger.log('message', {'context': context, 'content': message})

    def end_log(self):
        self.log_message('Plugin run is complete.')
