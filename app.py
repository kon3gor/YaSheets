import flask
import os
import sheets_bot
import json

app = flask.Flask(__name__)


@app.route("/<sheet_id>", methods=["POST"])
def upload_dict_to_sheet(sheet_id: str):
    data_str = flask.request.get_data().decode("utf-8")
    data = json.loads(data_str)
    sheets_bot.add_answer(sheet_id, data["answers"])
    return "ok", 200


@app.route("/ping", methods=["GET"])
def ping():
    return "pong", 200


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run("0.0.0.0", port=port)
