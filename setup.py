from distutils.core import setup

setup(name='toggl_driver',
      version='0.0.1',
      description="",
      author='',
      author_email='',
      packages=['toggl_driver', 'toggl_driver.args', 'toggl_driver.commands', 'toggl_driver.config'],
      scripts=['toggl_driver/scripts/toggl']
     )