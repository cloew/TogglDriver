from ..config import GlobalConfig

class StopTimer:
    """ Represents a command to stop the Toggl Timer """
    description = "Stop the Toggl Timer"
    args = []
    
    def run(self):
        """ Stop the timer """
        GlobalConfig.connection.timer.stop()