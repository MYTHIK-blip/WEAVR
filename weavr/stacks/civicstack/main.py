from flask import Flask
import sys
import os

# Add weavr_agent to the system path to allow relative imports from routes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'agents', 'weavr_agent')))

# Now import the stack route blueprint
from routes.stack_route import stack_bp

# Initialize Flask app
app = Flask(__name__)
app.register_blueprint(stack_bp, url_prefix="/")

# Run app on 0.0.0.0:8050
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050)
