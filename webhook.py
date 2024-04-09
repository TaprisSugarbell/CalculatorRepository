from flask import Flask, request, json

app = Flask(__name__)


@app.route('/webhook', methods=["POST"])
def webhook():
    if request.headers["Content-Type"] == "application/json":
        info = json.dumps(request.json)
        print(info)
        return info


if __name__ == "__main__":
    app.run()
