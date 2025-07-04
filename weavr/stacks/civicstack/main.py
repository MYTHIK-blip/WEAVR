from flask import Flask
from routes.stack_route import stack_bp

app = Flask(__name__)
app.register_blueprint(stack_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
