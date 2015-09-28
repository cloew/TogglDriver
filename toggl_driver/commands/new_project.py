from .store_project import StoreProject

from ..args import WorkspaceArg
from ..config import GlobalConfig

from kao_command.args import Arg, FlagArg, BareWords

class NewProject:
    """ Represents a command to create a new Toggl Project """
    description = "Create a new Toggl Project"
    args = [Arg('name', action='store', provider=BareWords, nargs='+', help='Project Name'),
            WorkspaceArg(help="Workspace to create the Project under"),
            FlagArg('-s', '--store', action='store_true', help="Store this project in the Local Config")]
        
    def run(self, *, name, workspace, store=False):
        """ Run the command """
        project = GlobalConfig.connection.Project(name=name, wid=workspace.id)
        project.create()
        
        if store:
            StoreProject().store(project)