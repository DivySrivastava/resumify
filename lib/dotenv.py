import os

final_list = []

def load():
    env = open('.env', 'r')
    env = env.read(100)
    env = env.split('\n')
    for ln in env:
        final_list.insert(1, {
           "var": ln.split('=')[0].split(' ')[0],
           "value": ln.split('=')[1].split(' ')[1]
        })
        pass
    for env_obj in final_list:
        os.environ[env_obj["var"]] = env_obj["value"]
        pass
    return os.environ

load()