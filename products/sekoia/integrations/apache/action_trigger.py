from meshroom.decorators import setup
from meshroom.model import Instance
from meshroom.model import Plug
from meshroom.model import Integration
from ...api import SekoiaAPI
import yaml
import json

@setup(title='Push action to git repo', order=0, owns_both=True)
def git_push_automation_module(integration: Integration):
    """A setup hook that pushes the automation module to a git repo"""
    from meshroom.git import Git
    from meshroom.interaction import log
    name = integration.target_product
    path = integration.path.parent / 'dist' / 'automations' / name
    if Git(path).push(True, '.', f'Update {name} automation module'):
        log(f'Automation module {name} successfully pushed to git repo')
    else:
        log(f'Automation module {name} is up-to-date in git repo')

@setup(title='Sync action from git repo', order=1, owns_both=False)
def update_playbook_module_from_git(integration: Integration, instance: Instance):
    """A setup hook that syncs an integration's automation module from the git repo"""
    from meshroom.git import Git
    from meshroom.model import get_project_dir
    from uuid import uuid4
    name = integration.target_product
    path = integration.path.parent / 'dist' / 'automations' / name
    api = SekoiaAPI(instance.settings.get('region', 'fra1'), instance.get_secret('API_KEY'))
    api.pull_custom_integration(Git().get_remote(scheme='https'), Git().get_branch(), path.relative_to(get_project_dir()).as_posix(), str(uuid4()))