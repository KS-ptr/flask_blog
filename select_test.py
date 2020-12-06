import vars_config as c
from json import load

encoding = c.encoding
db_filename = c.db_path + c.diary_db_filename

cond_dict = {"id": 1}

cond_keys = cond_dict.keys()
result_list = []
with open(db_filename, encoding=encoding) as f:
    all_list = load(f)
    for diary in all_list:
        for key in cond_keys:
            if diary[key] == cond_dict[key]:
                result_list.append(diary)

print(result_list)