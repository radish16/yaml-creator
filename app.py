from flask import Flask, render_template, request
import yaml
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    yaml_output = ""
    if request.method == "POST":
        keys = request.form.getlist("key")
        values = request.form.getlist("value")
        data = {k: v for k, v in zip(keys, values) if k}
        yaml_output = yaml.dump(data, allow_unicode=True)
    return render_template("index.html", yaml_output=yaml_output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Renderが指定するポートを取得
    app.run(debug=False, host="0.0.0.0", port=port)  # 外部アクセス許可
