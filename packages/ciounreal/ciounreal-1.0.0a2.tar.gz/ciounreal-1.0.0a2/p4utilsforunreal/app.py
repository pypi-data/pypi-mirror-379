#  Copyright 2024 CoreWeave
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import uuid
import json
import pprint
import socket
from pathlib import Path
from typing import Optional

from p4utilsforunreal import perforce
from p4utilsforunreal.log import get_logger


logger = get_logger()


def get_conductor_task_id() -> Optional[str]:
    """
    Trying to find Conductor Task ID in os environment variable CONDUCTOR_TASK

    :return: Conductor Task ID or None
    :rtype: Optional[str]
    """

    return os.getenv('CONDUCTOR_TASK')


def get_workspace_name(project_name: str) -> str:
    """
    Build and return the workspace name based on the given project name:
    <USERNAME>_<HOST>_<PROJECT_NAME>_conductor

    :param project_name: Name of the project

    :return: Workspace name
    :rtype: str
    """

    unique_id = get_conductor_task_id() or 'NoConductorTaskId'
    return f'{os.getlogin()}_{socket.gethostname()}_{unique_id}_{project_name}_conductor'


def get_workspace_specification_template_from_file(workspace_specification_template_path: str) -> dict:
    """
    Read the given workspace specification template file path and return loaded content

    :param workspace_specification_template_path: Path to the workspace specification template file

    :return: Loaded workspace specification template dictionary
    :rtype: dict
    """

    if not os.path.exists(workspace_specification_template_path):
        raise FileNotFoundError(
            f'The workspace specification template does not exist: {workspace_specification_template_path}'
        )

    logger.info(f'Getting workspace specification template from file: {workspace_specification_template_path} ...')
    with open(workspace_specification_template_path, 'r') as f:
        return json.load(f)


def create_perforce_workspace_from_template(
        specification_template: dict,
        project_name: str,
        perforce_server: str,
        overridden_workspace_root: str = None,
) -> perforce.PerforceClient:
    """
    Creates Perforce workspace from the template

    :param specification_template: Workspace specification template dictionary
    :param project_name: Name of the project to build workspace name
    :param perforce_server: Perforce server address to connect to
    :param overridden_workspace_root: Workspace local path root (Optional, root from template is used by default)

    :return: :class:`p4utilsforunreal.perforce.PerforceClient` instance
    :rtype: :class:`p4utilsforunreal.perforce.PerforceClient`
    """

    logger.info(f'Creating perforce workspace from template: \n'
          f'Specification template: {specification_template}\n'
          f'Project: {project_name}\n'
          f'Perforce server: {perforce_server}\n'
          f'Overridden workspace root: {overridden_workspace_root}')

    workspace_name = get_workspace_name(project_name=project_name)

    specification_template_str = json.dumps(specification_template)
    specification_str = specification_template_str.replace('{workspace_name}', workspace_name)
    specification = json.loads(specification_str)

    if overridden_workspace_root:
        specification['Root'] = overridden_workspace_root

    logger.info(f'Specification: {specification}')

    perforce_client = perforce.PerforceClient(
        connection=perforce.PerforceConnection(port=perforce_server),
        name=workspace_name,
        specification=specification
    )

    perforce_client.save()

    logger.info('Perforce workspace created!')
    logger.info(pprint.pformat(perforce_client.spec))

    return perforce_client


def initial_workspace_sync(workspace: perforce.PerforceClient, unreal_project_relative_path: str) -> None:
    """
    Do initial workspace synchronization:

    - .uproject file
    - Binaries folder
    - Config folder
    - Plugins folder

    :param workspace: p4utilsforunreal.perforce.PerforceClient instance
    :param unreal_project_relative_path: path to the .uproject file relative to the workspace root
    """

    logger.info('Workspace initial synchronizing ...')

    workspace_root = workspace.spec['Root'].replace('\\', '/')

    paths_to_sync = [f'{workspace_root}/{unreal_project_relative_path}']

    unreal_project_directory = os.path.dirname(unreal_project_relative_path)

    for folder in ['Binaries', 'Config', 'Plugins']:
        tokens = filter(
            lambda t: t not in [None, ''],
            [workspace_root, unreal_project_directory, folder, '...']
        )
        paths_to_sync.append('/'.join(tokens))

    logger.info(f'Paths to sync: {paths_to_sync}')

    for path in paths_to_sync:
        try:
            workspace.sync(path)
        except Exception as e:
            logger.info(f'Initial workspace sync exception: {str(e)}')


def configure_project_source_control_settings(workspace: perforce.PerforceClient, unreal_project_relative_path: str):
    """
    Configure SourceControl settings (Saved/Config/WindowsEditor/SourceControlSettings.ini)
    with the current P4 connection settings

    :param workspace: p4utilsforunreal.perforce.PerforceClient instance
    :param unreal_project_relative_path: path to the .uproject file relative to the workspace root
    """

    logger.info('Configuring Unreal project SourceControl settings ...')
    unreal_project_directory = os.path.dirname(unreal_project_relative_path)
    tokens = filter(
        lambda t: t not in [None, ''],
        [workspace.spec['Root'], unreal_project_directory, 'Saved/Config/WindowsEditor/SourceControlSettings.ini']
    )
    source_control_settings_path = '/'.join(tokens)
    try:
        workspace.sync(source_control_settings_path)
    except:
        pass
    os.makedirs(os.path.dirname(source_control_settings_path), exist_ok=True)
    logger.info(f'Source Control settings file: {source_control_settings_path}')

    source_control_settings_lines = [
        '[PerforceSourceControl.PerforceSourceControlSettings]\n',
        'UseP4Config = False\n',
        f'Port = {workspace.p4.port}\n',
        f'UserName = {workspace.p4.user}\n',
        f'Workspace = {workspace.p4.client}\n\n',

        '[SourceControl.SourceControlSettings]\n',
        'Provider = Perforce\n'

    ]
    logger.info('source control settings:\n')
    for setting_line in source_control_settings_lines:
        logger.info(setting_line)

    with open(source_control_settings_path, 'w+') as f:
        for setting_line in source_control_settings_lines:
            f.write(setting_line)


def create_workspace(
        perforce_specification_template_path: str,
        unreal_project_relative_path: str,
        perforce_server: str,
        overridden_workspace_root: str = None
):
    """
    Create P4 workspace and execute next steps:

    - :meth:`p4utilsforunreal.app.get_workspace_specification_template_from_file()`
    - :meth:`p4utilsforunreal.app.initial_workspace_sync()`
    - :meth:`p4utilsforunreal.app.configure_project_source_control_settings()`

    :param perforce_specification_template_path: Path to the perforce specification template file to read specification from
    :param unreal_project_relative_path: path to the .uproject file relative to the workspace root
    :param perforce_server: Perforce server address to connect to
    :param overridden_workspace_root: Workspace local path root (Optional, root from template is used by default)
    """

    logger.info('Creating workspace with the following settings:\n'
                f'Specification template: {perforce_specification_template_path}\n'
                f'Unreal project relative path: {unreal_project_relative_path}'
                f'Perforce server: {perforce_server}'
                f'Overridden workspace root: {overridden_workspace_root}')

    workspace_specification_template = get_workspace_specification_template_from_file(
        workspace_specification_template_path=perforce_specification_template_path
    )

    workspace = create_perforce_workspace_from_template(
        specification_template=workspace_specification_template,
        project_name=Path(unreal_project_relative_path).stem,
        perforce_server=perforce_server,
        overridden_workspace_root=overridden_workspace_root
    )

    initial_workspace_sync(
        workspace=workspace,
        unreal_project_relative_path=unreal_project_relative_path
    )

    configure_project_source_control_settings(
        workspace=workspace,
        unreal_project_relative_path=unreal_project_relative_path
    )


def delete_workspace(unreal_project_relative_path: str):
    """
    Clear workspace files that are in depot and delete the workspace

    :param unreal_project_relative_path: path to the .uproject file relative to the workspace root
    """

    project_name = Path(unreal_project_relative_path).stem

    logger.info(f'Deleting workspace for the project: {project_name}')

    workspace_name = get_workspace_name(project_name)
    p4 = perforce.PerforceConnection().p4

    last_exception = None

    workspace_root = p4.fetch_client(workspace_name).get('Root').replace('\\', '/')
    if workspace_root and os.path.exists(workspace_root):
        try:
            logger.info('Reverting changes in default changelist')
            p4.client = workspace_name
            p4.run('revert', '-c', 'default', workspace_root + '/...')
        except Exception as e:
            if 'file(s) not opened on this client' in str(e):
                logger.info('Nothing to revert')
                pass
            else:
                logger.info(f'Error handled while reverting changes: {e}')
                last_exception = e
        try:
            logger.info(f'Clearing workspace root: {workspace_root}')
            p4.client = workspace_name
            p4.run('sync', '-f', workspace_root + '/...#0')
        except Exception as e:
            if 'file(s) up-to-date' in str(e):
                logger.info('Nothing to clear')
            else:
                logger.info(f'Error handled while clearing workspace: {e}')
                last_exception = e

    try:
        logger.info(f'Deleting workspace: {workspace_name}')
        p4.run('client', '-d', workspace_name)
    except Exception as e:
        logger.info(f'Error handled while deleting workspace: {e}')
        last_exception = e

    if last_exception and isinstance(last_exception, Exception):
        raise last_exception
