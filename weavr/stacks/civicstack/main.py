from flask import Flask
import sys
import os

# Dynamically include the weavr_agent path for route imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'agents', 'weavr_agent')))

from routes.stack_route import stack_bp

app = Flask(__name__)
app.register_blueprint(stack_bp, url_prefix="/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
