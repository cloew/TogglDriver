from ..config import GlobalConfig
from kao_command.args import Arg

class StoreApiToken:
    """ Represents a command to store the global Api Token for connecting to Toggl """
    description = "Store the Toggl API Token"
    args = [Arg('token', action='store', help='Token to store')]
        
    def run(self, *, token):
        """ Run the command """
        self.store(token)
        
    def store(self, token):
        """ Store the token """
        GlobalConfig.storeToken(token)