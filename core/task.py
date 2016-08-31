import os
import re
import json
import requests
from urllib import parse
from . import util
from . import setting


def create_task(link):
    if re.match(r'^http://\S+$', link) or re.match(r'^https://\S+$', link):
        return _HttpTask(link)
    else:
        raise Exception('wrong s(link)')


def load_task(info):
    if info['kind'] == 'HTTP':
        return _HttpTask(info)


class _BaseTask(object):
    def start(self):
        pass

    def stop(self):
        pass

    def is_stop(self):
        pass

    def is_end(self):
        pass


class _HttpTask(_BaseTask):
    def __init__(self, param):
        self.__path = None
        self.__threads = []
        self.__process = []
        self.__filename = None
        self.__size = None
        self.__url = None
        self.__stop = True

        if isinstance(param, str):
            self.url = param
        elif isinstance(param, dict):
            self.info = param
        else:
            raise Exception('wrong param')

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        if self.__url is None:
            self.__url = url

            resp = requests.get(url, stream=True, headers={'Range': 'bytes=0-'})
            resp.close()

            # 获取下载的文件名
            disp = resp.headers.get('Content-Disposition')
            if disp is None:
                u = parse.urlparse(url).path
                filename = u[u.rindex("/") + 1:]
            else:
                filename = re.search(r'(?<=filename=")\S+(?=")|(?<=filename=)\S+', disp).group()
            self.__filename = parse.unquote(filename, resp.encoding)

            # 获取下载内容的大小
            length = resp.headers.get('Content-Length')
            if length is None:
                self.__size = -1
            else:
                self.__size = int(length)

            if resp.headers.get('Content-Range') is None:
                info = {
                    'start': 0,
                    'end': self.size,
                    'has': 0,
                }
                self.__process.append(info)
            else:
                thread_num = setting.thread_num
                piece_len = self.size // thread_num
                surplus = self.size % thread_num
                for i in range(thread_num):
                    info = {
                        'start': piece_len * i,
                        'end': piece_len * (i + 1) - 1,
                        'has': 0,
                    }
                    if i == thread_num - 1:
                        info['end'] += surplus
                    self.__process.append(info)

    @property
    def info(self):
        result = {
            'title': self.title,
            'size': self.size,
            'kind': 'HTTP',
            'path': self.path,
            'link': self.url,
        }
        return result

    @info.setter
    def info(self, info):
        self.__filename = info['title']
        self.__size = info['size']
        self.__path = info['path']
        self.__url = info['link']

        with open(self.__path + self.__filename + '.json', 'r') as fp:
            self.__process = json.load(fp)

    def start(self):
        if self.__path is None:
            raise Exception('not set path')
        self.__stop = False
        if len(self.__threads) is 0:
            self.__threads = \
                [util.HttpDownThread(self.__url, self.__path + self.__filename, info)
                 for info in self.__process]
            self.__process = None
        try:
            for t in self.__threads:
                t.start()
        except RuntimeError:
            self.__threads = \
                [util.HttpDownThread(
                    self.__url, self.__path + self.__filename, t.get_info()) for t in self.__threads]
            for t in self.__threads:
                t.start()

    def stop(self):
        self.__stop = True
        for t in self.__threads:
            t.stop()
        self.wait()

    def is_stop(self):
        return self.__stop

    def is_end(self):
        return self.downloaded == self.size

    def wait(self):
        for t in self.__threads:
            t.join()
        if not self.is_end():
            if len(self.__threads) is not 0:
                with open(self.__path + self.__filename + '.json', 'w') as fp:
                    json.dump([t.get_info() for t in self.__threads], fp)
        else:
            if os.path.exists(self.path + self.__filename + '.json'):
                os.remove(self.path + self.__filename + '.json')

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        if self.__path is None:
            self.__path = path

    @property
    def size(self):
        return self.__size

    @property
    def downloaded(self):
        result = 0
        if self.__process:
            for info in self.__process:
                result += info['has']
        else:
            for t in self.__threads:
                result += t.has()
        return result

    @property
    def title(self):
        return self.__filename

    @property
    def filelist(self):
        result = [
            {'name': self.__filename, 'size': self.size}
        ]
        return result

    @property
    def link(self):
        return self.__url
