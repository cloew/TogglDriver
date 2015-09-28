from kao_command import Commands

commands = Commands(__name__, {'start': 'start_timer.StartTimer',
                               'store': {'token': 'store_api_token.StoreApiToken'}})