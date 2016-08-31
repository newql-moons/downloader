import sqlite3
import os


DB_PATH = './db.sqlite3'


def pre_db():
    if not os.path.exists(DB_PATH):
        with open('db.sql', 'r') as fp:
            sql = fp.read()
        conn = sqlite3.connect(DB_PATH)
        for s in sql.split(';'):
            conn.execute(s)
        conn.commit()
        conn.close()


class DownloadingTab(object):
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)

    def select(self, link=None):
        if link:
            sql = 'SELECT * FROM downloading WHERE link=?'
            cs = self.conn.execute(sql, (link,))
        else:
            sql = 'SELECT * FROM downloading'
            cs = self.conn.execute(sql)
        result = []
        for item in cs.fetchall():
            result.append({
                'link': item[0],
                'title': item[1],
                'path': item[2],
                'kind': item[3],
                'size': item[4],
            })
        return result

    def insert(self, info):
        link = info['link']
        if len(self.select(link)) is 0:
            title = info['title']
            path = info['path']
            kind = info['kind']
            size = info['size']
            sql = 'INSERT INTO downloading VALUES (?,?,?,?,?)'
            self.conn.execute(sql, (link, title, path, kind, size,))
            self.conn.commit()

    def delete(self, link):
        if len(self.select(link)) is not 0:
            sql = 'DELETE FROM downloading WHERE link=?'
            self.conn.execute(sql, (link,))
            self.conn.commit()

    def close(self):
        self.conn.close()


class DownloadedTab(object):
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)

    def select(self, link=None):
        if link:
            sql = 'SELECT * FROM downloaded WHERE link=?'
            cs = self.conn.execute(sql, (link,))
        else:
            sql = 'SELECT * FROM downloaded'
            cs = self.conn.execute(sql)
        result = []
        for item in cs.fetchall():
            result.append({
                'link': item[0],
                'title': item[1],
                'path': item[2],
                'kind': item[3],
                'size': item[4],
            })
        return result

    def insert(self, info):
        link = info['link']
        if len(self.select(link)) is 0:
            title = info['title']
            path = info['path']
            kind = info['kind']
            size = info['size']
            date = info['date']
            sql = 'INSERT INTO downloaded VALUES (?,?,?,?,?,?)'
            self.conn.execute(sql, (link, title, path, kind, size, date,))
            self.conn.commit()

    def delete(self, link):
        if len(self.select(link)) is not 0:
            sql = 'DELETE FROM downloaded WHERE link=?'
            self.conn.execute(sql, (link,))
            self.conn.commit()

    def close(self):
        self.conn.close()


class FilelistTab(object):
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)

    def insert(self, file):
        if len(self.select_by_path(file['path'])) is 0:
            sql = 'INSERT INTO filelist VALUES (?,?)'
            self.conn.execute(sql, (file['path'], file['link'],))
            self.conn.commit()

    def select_by_path(self, path):
        sql = 'SELECT * FROM filelist WHERE path=?'
        cs = self.conn.execute(sql, (path,))
        result = []
        for item in cs.fetchall():
            result.append({
                'path': item[0],
                'link': item[1],
            })
        return result

    def select_by_link(self, link):
        sql = 'SELECT * FROM filelist WHERE link=?'
        cs = self.conn.execute(sql, (link,))
        result = []
        for item in cs.fetchall():
            result.append({
                'path': item[0],
                'link': item[1],
            })
        return result

    def delete_by_link(self, link):
        if len(self.select_by_link(link)) is not 0:
            sql = 'DELETE FROM filelist WHERE link=?'
            self.conn.execute(sql, (link,))
            self.conn.commit()

    def close(self):
        self.conn.close()
