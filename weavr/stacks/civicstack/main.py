# main.py — Civicstack Flask Entrypoint

from flask import Flask
import sys
import os

# Make weavr_agent importable for blueprint reuse
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'app', 'agents', 'weavr_agent')))

# Import blueprint from stack_route.py
from routes.stack_route import stack_bp

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(stack_bp, url_prefix="/")

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
