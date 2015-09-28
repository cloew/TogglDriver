from .global_config import GlobalConfig

from kao_config import LocalConfigFile
from kao_decorators import lazy_property

class LocalConfig:
    """ Represents the local Toggl Driver Configuration """
    CONFIG_FILENAME = ".toggl-settings"
    
    @lazy_property
    def config(self):
        """ Return the local config file """
        return LocalConfigFile(self.CONFIG_FILENAME, create=True)
    
    @lazy_property
    def pid(self):
        """ Return the project id """
        return self.config.readlines()[0].strip()
    
    @lazy_property
    def project(self):
        """ Return the stored project """
        return GlobalConfig.connection.projects.withId(self.pid)
            
    def storeProject(self, project):
        """ Store the provided project """
        return self.config.write(str(project.id))
            
LocalConfig = LocalConfig()