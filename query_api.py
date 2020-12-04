from json import load, dump
import vars_config as c

# 抽出
def select(cond: dict, db_filename: str):
    with open(db_filename, encoding=c.encoding) as f:
        all_list = load(f)

# 追加        
def insert(entry: dict, db_filename: str):
    with open(db_filename, encoding=c.encoding, mode="w") as f:
        pass

# 変更
def update(entry: dict, db_filename: str):
    with open(db_filename, encoding=c.encoding, mode="w") as f:
        pass

# 削除
def delete(id: int, db_filename: str):
    with open(db_filename, encoding=c.encoding, mode="w") as f:
        pass