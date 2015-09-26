from ..config import GlobalConfig

class StoreApiToken:
    """ Represents a command to store the global Api Token for connecting to Toggl """
    description = "Store the Toggl API Token"
    
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('token', action='store', help='Token to store')
        
    def run(self, arguments):
        """ Run the command """
        self.store(arguments.token)
        
    def store(self, token):
        """ Store the token """
        GlobalConfig.storeToken(token)