from kao_config import GlobalConfigDir
from kao_decorators import lazy_property

class GlobalConfig:
    """ Represents the global Toggl Driver Configuration """
    DIR_NAME = ".toggl-driver"
    TOKEN_FILENAME = ".token"
    
    @lazy_property
    def configDir(self):
        """ Return the global config directory """
        return GlobalConfigDir(self.DIR_NAME, create=True)
    
    @lazy_property
    def tokenFilename(self):
        """ Return the global config filename """
        return self.configDir.getFile(self.TOKEN_FILENAME, create=True)
    
    @lazy_property
    def token(self):
        """ Return the global config Api Token """
        with open(self.tokenFilename, 'r') as file:
            return file.readlines()[0].strip()
            
    def storeToken(self, token):
        """ Store the provided token """
        with open(self.tokenFilename, 'w') as file:
            return file.write(token)
            
GlobalConfig = GlobalConfig()