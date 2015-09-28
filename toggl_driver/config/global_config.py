from kao_config import GlobalConfigFile
from kao_decorators import lazy_property

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
        with open(self.config.path, 'r') as file:
            return file.readlines()[0].strip()
            
    def storeToken(self, token):
        """ Store the provided token """
        with open(self.config.path, 'w') as file:
            return file.write(token)
            
GlobalConfig = GlobalConfig()