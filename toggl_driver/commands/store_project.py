from ..config import GlobalConfig, LocalConfig
from kao_command.args import Arg, BareWords

class StoreProject:
    """ Represents a command to store a Project in the local Config """
    description = "Store the Toggl Project in the Local Config"
    args = [Arg('name', action='store', provider=BareWords, nargs='+', help='Project Name')]
        
    def run(self, *, name):
        """ Run the command """
        project = GlobalConfig.connection.projects.withName(name).first
        if project:
            self.store(project)
        else:
            print("Unknown Project: {0}".format(name))
            
    def store(self, project):
        """ Store the provided project """
        LocalConfig.storeProject(project)