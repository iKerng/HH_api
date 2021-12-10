# token.json
# {
# 	"client_id": "",
# 	"client_secret": "",
# 	"token_id": "",
# 	"token_type": ""
# }
import requests as rq
import os.path

full_path = os.path.abspath('') + '\\HH_api\\data\\token.json'
full_path = os.path.realpath(full_path)
token_dict = dict()

if os.path.exists(full_path):
    with open(full_path, 'r', encoding='utf8') as file:
        exec('token_dict = ' + file.read())
        file.close()
    hh_token = token_dict.get('token_id')
    hh_token_type = str.upper(token_dict.get('token_type')[0]) + token_dict.get('token_type')[1:]
    token_dict.update({'token_type':hh_token_type})
else:
    print('Файл с данными для использования Токена не найден. Подложите файл (token.xml) с данными в папку "data"')