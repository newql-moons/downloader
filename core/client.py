from . import task


class Downloader(object):
    def __init__(self, infos=None):
        if infos:
            self._tasks = [task.load_task(info) for info in infos]
        else:
            self._tasks = []

    def add_task(self, task, path='./'):
        task.path = path
        self._tasks.append(task)

    def start_task(self, i):
        self._tasks[i].start()

    def stop_task(self, i):
        self._tasks[i].stop()

    def get_task(self, i):
        return self._tasks[i]

    def rm_task(self, i):
        self.stop_task(i)
        return self._tasks.pop(i)

    def close(self):
        for i in range(len(self._tasks)):
            self.stop_task(i)
