import json

config = json.load(open('db_config.json'))  #load db in json format
LOGIN_EXPIRE = 3600