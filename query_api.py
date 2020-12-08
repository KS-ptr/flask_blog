from json import load, dumps, dump
import vars_config as c

encoding = c.encoding

# 抽出
def select(cond_dict: dict, db_filename: str):
    cond_keys = cond_dict.keys()
    result_list = []
    with open(db_filename, encoding=encoding) as f:
        all_list = load(f)
        for diary in all_list:
            for key in cond_keys:
                if diary[key] == cond_dict[key]:
                    result_list.append(diary)
    return result_list

# 追加        
def insert(id: int, entry: dict, db_filename: str):
    try:
        with open(db_filename, encoding=encoding, mode="w") as f:
            f.seek(-1, 2)
            f.truncate()
            f.write(' ,'.encode())
            f.write(dumps(entry, ensure_ascii=False, indent=4, sort_keys=True, separators=(",", ": ")).encode(encoding=encoding))
            f.write(']'.encode())
        return {"status_code": 200, "posted_id": id}
    except Exception as e:
        return {"status_code": 500, "posted_id": id, "message": e}

# 変更
def update(id: int, entry: dict, db_filename: str):
    with open(db_filename, encoding=encoding, mode="w") as f:
        pass

# 削除
def delete(id: int, db_filename: str):
    with open(db_filename, encoding=encoding, mode="w") as f:
        pass