CREATE TABLE downloading (
  link TEXT PRIMARY KEY,
  title TEXT,
  path TEXT,
  kind TEXT,
  size INTEGER
);

CREATE TABLE downloaded (
  link TEXT PRIMARY KEY,
  title TEXT,
  path TEXT,
  kind TEXT,
  size INTEGER,
  date TEXT
);

CREATE TABLE filelist (
  path TEXT PRIMARY KEY,
  link TEXT
);
