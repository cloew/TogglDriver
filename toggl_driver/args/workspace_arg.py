from ..config import GlobalConfig
from kao_command.args import FlagArg

class WorkspaceArg(FlagArg):
    """ Represents an CLI Argument that specifies a Workspace """
    
    def __init__(self, *, help):
        """ Initialize the Arg """
        FlagArg.__init__(self, '-w', '--workspace', action="store", help=help)
    
    def getValue(self, args):
        """ Return the value from the args """
        workspaceName = FlagArg.getValue(self, args)
        return GlobalConfig.connection.workspaces.findByName(workspaceName)