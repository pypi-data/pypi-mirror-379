# MikaGram's sessions
Easy to use sessions from popular libs as one 


## Install

```pip install mikagram_sessions```

## Converting

```python
from mikagram_sessions import TelethonSqlite, PyrogramSqlite


from_session = PyrogramSqlite("a.session")
to_session = TelethonSqlite.from_session(from_session, "b.session")
```


## Sessions supporting
| Name              | Read          | Write         |
|-------------------|---------------|---------------|
| Telethon (Sqlite) | Full          | Full          |
| Pyrogram (Sqlite) | Full          | Full          |
| MikaGram (json)   | Full          | Full          |
| Tdata             | Not supported | Not supported |
