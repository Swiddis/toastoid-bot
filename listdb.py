import os
import pymongo

class ListDb:
    def __init__(self):
        self.cstr = os.environ["MONGODB_CONNSTRING"]
        self.client = pymongo.MongoClient(self.cstr)
        self.db = self.client["entries"]
        self.entries = self.db["entries"]
    
    def add_entry(self, uid, ls_name, entry):
        self.entries.insert_one({"uid": uid, "list": ls_name, "entry": entry})

    def get_entries(self, uid, ls_name):
        results = self.entries.find({"uid": uid, "list": ls_name})
        return list(result["entry"] for result in results)
