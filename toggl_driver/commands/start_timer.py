from ..args import OptionalProjectArg
from ..config import GlobalConfig

from kao_command.args import Arg, BareWords

class StartTimer:
    """ Represents a command to start the Toggl Timer """
    description = "Start the Toggl Timer"
    args = [Arg('description', nargs='+', provider=BareWords),
            OptionalProjectArg(help="start the timer within")]
    
    def run(self, *, description, project=None, workspace=None):
        """ Start the timer """
        entry = None
        if project:
            entry = GlobalConfig.connection.TimeEntry(description=description, pid=project.id)
        else:
            entry = GlobalConfig.connection.TimeEntry(description=description, wid=workspace.id)
        entry.start()