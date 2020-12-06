import datetime
from json import load, dump
import vars_config as c
from query_api import insert, select, update, which_upsert, delete

encoding = c.encoding
diary_filename = c.db_path + c.diary_db_filename

def get_from_id(id: int):
    return select({"id": id}, diary_filename)

def post_diary(id: int, req_diary: dict):
    if len(select({"id": id}, diary_filename)) == 0:
        return insert(id, req_diary, diary_filename)
    else:
        return update(id, req_diary, diary_filename)

def main():
    count()
    sort()

def count():
    # with open(category_filename, encoding="utf-8") as f:
    #     category_list = load(f)
    pass

def sort():
    with open(diary_filename, encoding=encoding) as f:
        diary_list = load(f)
        diary_list.sort(key=lambda x:x['date'], reverse=True)
    
    with open(diary_filename, encoding=encoding, mode='w') as f:
        dump(diary_list, f, indent=4)

if __name__ == "__main__":
    main()

class Diary():
    def __init__(self):
        pass