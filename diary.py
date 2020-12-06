from types import MethodType
from flask import Flask, render_template, request, jsonify
from json import load
import vars_config
from diary_controller import get_from_id, post_diary

app = Flask(__name__)
entries = vars_config.entries_in_page

@app.route("/")
def hello():
	return "Hello"

@app.route("/favicon.ico")
def favicon():
	return app.send_static_file("favicon.ico")

@app.route("/diary")
def render_diary():
	if request.args.get('p') is None:
		pager = 0
	else:
		pager = int(request.args.get('p'))

	with open('diary_db/diary.json', encoding="utf-8") as d:
		diary_list = load(d)
		if (pager + 1) * entries < len(diary_list):
			next_page = True
		else:
			next_page = False

	diary_list_on_page = diary_list[pager * entries:(pager + 1) * entries]
	return render_template('diary.j2', title='プテラノーツ', diaries=diary_list_on_page, pager=pager, next_page=next_page)

@app.route("/manage")
def render_admin():
	return render_template('manage.j2', title='管理者用')

# IDから日記を取得
@app.route("/diary_db/<int:id>", methods=["GET"])
def call_get_diary(id):
	return jsonify(get_from_id(id))

# 日記の更新
@app.route("/diary_db/<int:id>", methods=["POST"])
def call_post_diary(id):
	req_json = request.get_json()
	return jsonify(post_diary(id, req_json))

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
