from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def status():
    return jsonify({"status": "🧠 WEAVR agent online", "port": 5151})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5151)
