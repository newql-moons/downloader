import json


SETTING_PATH = 'config/setting.json'


def _load_setting(path = SETTING_PATH):
    with open(path, 'r') as fp:
        setting = json.load(fp)

    global thread_num
    global download_path
    global data_path
    thread_num = setting['thread_num']
    download_path = setting['download_path']
    data_path = setting['data_path']


def upload_setting(setting, path = SETTING_PATH):
    with open(path, 'w') as fp:
        json.dump(setting, fp)


_load_setting(SETTING_PATH)
