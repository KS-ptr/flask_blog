from configparser import ConfigParser

_config = ConfigParser()
_config.read("config.ini")

encoding = _config.get("settings", "encoding")
mail_address = _config.get("settings", "mail_address")
entries_in_page = int(_config.get("settings", "entries_on_one_page"))

db_path = _config.get("db_settings", "db_directory_path")
auth_filename = _config.get("db_settings", "auth")
category_filename = _config.get("db_settings", "category")
diary_db_filename = _config.get("db_settings", "diary")