try:
    from pypresence import Presence
    import time
    import os

    os.system("title Psycho's Discord RPC Changer")
    rpcid = int(input('RPC ID: '))
    uno = input('What do you want your state to be? ')
    big = input('Large image ID? ')
    rpc = Presence(rpcid)
    rpc.connect()

    rpc.update(state = f'{uno}', large_image = f'{big}', start = time.time())
    print('RPC successfully set.')
    time.sleep(2)

    while True:
        time.sleep(5)

        
except KeyboardInterrupt:
    print('\nProgram stopped using Ctrl+C.')