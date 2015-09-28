from kao_config import GlobalConfigFile
from kao_decorators import lazy_property
from pytoggl import TogglConnection

class GlobalConfig:
    """ Represents the global Toggl Driver Configuration """
    CONFIG_FILENAME = ".toggl-driver"
    
    @lazy_property
    def config(self):
        """ Return the global config file """
        return GlobalConfigFile(self.CONFIG_FILENAME, create=True)
    
    @lazy_property
    def token(self):
        """ Return the global config Api Token """
        return self.config.readlines()[0].strip()
            
    def storeToken(self, token):
        """ Store the provided token """
        return self.config.write(token)
    
    @lazy_property
    def connection(self):
        """ Return the Toggl Connection """
        return TogglConnection(self.token)
            
GlobalConfig = GlobalConfig()