from ..config import GlobalConfig, LocalConfig
from kao_command.args import FlagArg

class ProjectArg(FlagArg):
    """ Represents an CLI Argument that specifies a Project """
    
    def __init__(self, *, help):
        """ Initialize the Arg """
        FlagArg.__init__(self, '-p', '--project', action="store", help=help)
    
    def getValue(self, args):
        """ Return the value from the args """
        projectName = FlagArg.getValue(self, args)
        if projectName is None:
            project = LocalConfig.project
        else:
            project = GlobalConfig.connection.projects.withName(projectName).first
        return project