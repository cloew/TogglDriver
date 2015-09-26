from .commands import commands
from kao_command import Driver

def TogglDriver(scriptName):
    return Driver(scriptName, commands)