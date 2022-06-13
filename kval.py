import sqlite3

class KValDb:
    def __init__(self):
        with sqlite3.connect("./store/kval.db") as con:
            con.execute('''
                CREATE TABLE IF NOT EXISTS kval (
                    key text primary key not null,
                    value text
                )
            ''')
    
    def set_item(self, key, value):
        with sqlite3.connect('./store/kval.db') as con:
            con.execute("replace into kval values (?, ?)", (key, value))
    
    def get_item(self, key):
        with sqlite3.connect('./store/kval.db') as con:
            return list(r[0] for r in con.execute("select value from kval where key = (?)", (key,)))
