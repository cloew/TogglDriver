from ..args import ProjectArg
from ..args import WorkspaceArg
from ..config import GlobalConfig

from kao_command.args import Arg, BareWords

class StartTimer:
    """ Represents a command to start the Toggl Timer """
    description = "Start the Toggl Timer"
    args = [Arg('description', nargs='+', provider=BareWords),
            ProjectArg(help="The Project to start the timer within"),
            WorkspaceArg(help="The Workspace to start the timer within")]
    
    def run(self, *, description, project, workspace):
        """ Start the timer """
        entry = None
        if project:
            entry = GlobalConfig.connection.TimeEntry(description=description, pid=project.id)
        else:
            entry = GlobalConfig.connection.TimeEntry(description=description, wid=workspace.id)
        entry.start()