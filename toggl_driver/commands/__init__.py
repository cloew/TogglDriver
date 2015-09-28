from kao_command import Commands

commands = Commands(__name__, {'new': {'project': 'new_project.NewProject'},
                               'start': 'start_timer.StartTimer',
                               'stop': 'stop_timer.StopTimer',
                               'store': {'project': 'store_project.StoreProject',
                                         'token': 'store_api_token.StoreApiToken'},
                               'timer': 'current_timer.CurrentTimer'})