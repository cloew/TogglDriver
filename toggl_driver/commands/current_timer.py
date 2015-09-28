from ..config import GlobalConfig

class CurrentTimer:
    """ Represents a command to view the current Toggl Timer """
    description = "View the Toggl Timer"
    args = []
    
    def run(self):
        """ View the timer """
        entry = GlobalConfig.connection.timer.current()
        print(entry.description, entry.duration)