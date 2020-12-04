from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

encoding = config.get("settings", "encoding")
mail_address = config.get("settings", "mail_address")
entries_in_page = int(config.get("settings", "entries_on_one_page"))

category_filename = config.get("db_settings", "category")
diary_db_filename = config.get("db_settings", "diary")