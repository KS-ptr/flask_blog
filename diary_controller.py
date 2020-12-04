import datetime
from json import load, dump
import vars_config as c
from query_api import select, insert, update, delete

def get_from_id(id: int):
    select({"id": id}, c.diary_db_filename)

def post_diary():
    pass

def main():
    upsert_diary()
    count()
    sort()

def upsert_diary():
    # diary.jsonの更新、挿入処理
    pass

def count():
    # with open(category_filename, encoding="utf-8") as f:
    #     category_list = load(f)
    pass

def sort():
    with open(c.diary_db_filename, encoding=c.encoding) as f:
        diary_list = load(f)
        diary_list.sort(key=lambda x:x['date'], reverse=True)
    
    with open(c.diary_db_filename, encoding=c.encoding, mode='w') as f:
        dump(diary_list, f, indent=4)

if __name__ == "__main__":
    main()

class Diary():
    def __init__(self):
        pass