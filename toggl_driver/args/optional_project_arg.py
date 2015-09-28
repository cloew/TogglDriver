from .project_arg import ProjectArg
from .workspace_arg import WorkspaceArg

class OptionalProjectArg:
    """ Represents an optional Project/Workspace Argument """
    PROJ_HELP = "Project to "
    WKSP_HELP = "Workspace to "
    
    def __init__(self, *, help):
        """ Initialize with the Project/Workspace Arg """
        self.projectArg = ProjectArg(help=self.PROJ_HELP+help)
        self.workspaceArg = WorkspaceArg(help=self.WKSP_HELP+help)
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        self.projectArg.addArguments(parser)
        self.workspaceArg.addArguments(parser)
    
    def getPair(self, args):
        """ Return the value from the args """
        projectArgName, project = self.projectArg.getPair(args)
        if project is None:
            return self.workspaceArg.getPair(args)
        return projectArgName, project