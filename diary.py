from flask import Flask, render_template, request
from json import load
from configparser import ConfigParser

app = Flask(__name__)
config = ConfigParser()
config.read('config.ini')
entries_in_page = int(config.get("settings", "entries_on_one_page"))


@app.route("/")
def hello():
	return "Hello"

@app.route("/diary")
def render_diary():
	if request.args.get('p') is None:
		pager = 0
	else:
		pager = int(request.args.get('p'))

	with open('diary_db/diary.json', encoding="utf-8") as d:
		diary_list = load(d)
		if (pager + 1) * entries_in_page < len(diary_list):
			next_page = True
		else:
			next_page = False

	diary_list_on_page = diary_list[pager * entries_in_page:(pager + 1) * entries_in_page]
	return render_template('diary.j2', title='プテラノーツ', diaries=diary_list_on_page, pager=pager, next_page=next_page)

@app.route("/manage")
def render_admin():
	return render_template('manage.j2', title='管理者用')

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
