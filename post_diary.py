import datetime
from json import load, dump

category_filename = 'diary_db/category.json'
diary_db_filename = 'diary_db/diary.json'

def main():
    upsert_diary()
    count()
    sort()

def upsert_diary():
    # diary.jsonの更新、挿入処理
    pass

def count():
    with open(category_filename, encoding="utf-8") as f:
        category_list = load(f)


def sort():
    with open('diary_db/diary.json', encoding="utf-8") as f:
        diary_list = load(f)
        diary_list.sort(key=lambda x:x['date'], reverse=True)
    
    with open('diary_db/diary.json', encoding="utf-8", mode='w') as f:
        dump(diary_list, f, indent=4)

if __name__ == "__main__":
    main()

class Diary():
    def __init__(self):
        pass