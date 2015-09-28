from ..args import WorkspaceArg

class StartTimer:
    """ Represents a command to start the Toggl Timer """
    description = "Start the Toggl Timer"
    args = [WorkspaceArg(help="The Workspace to start the timer within")]
    
    def run(self, *, workspace):
        """ Start the timer """
        print(workspace)