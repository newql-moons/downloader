import threading
import requests
import os


class HttpDownThread(threading.Thread):
    def __init__(self, url, path, info):
        super().__init__()
        self.__start = info['start']
        self.__end = info['end']
        self.__has = info['has']
        self.__url = url
        self.__path = path
        self.__stop = True

    def run(self):
        if (self.__start + self.__has) <= self.__end:
            if os.path.exists(self.__path):
               fp = open(self.__path, 'rb+')
            else:
                fp = open(self.__path, 'wb+')
            headers = {
                'Range': 'bytes={0}-{1}'.format(self.__start + self.__has, self.__end)
            }
            print(headers)
            resp = requests.get(self.__url, stream=True, headers=headers)
            try:
                print(resp.headers['Content-Range'])
            except Exception:
                self.__has = 0
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    fp.seek(self.__start + self.__has)
                    fp.write(chunk)
                    self.__has += len(chunk)
                    # print('loading...')
                if self.__stop:
                    break

            resp.close()
            fp.close()

        self.__stop = True
        print(self.name + ' is end')

    def start(self):
        self.__stop = False
        super().start()

    def stop(self):
        self.__stop = True

    def get_info(self):
        info = {
            'start': self.__start,
            'end': self.__end,
            'has': self.__has,
        }
        return info

    def has(self):
        return self.__has
