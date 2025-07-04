from flask import Flask
from app.agents.weavr_agent.routes.run_route import run_bp
from app.agents.weavr_agent.routes.stack_route import stack_bp
from app.agents.weavr_agent.routes.ollama_route import ollama_bp
from app.agents.weavr_agent.routes.status_route import status_bp

app = Flask(__name__)

# Register modular blueprints
app.register_blueprint(run_bp, url_prefix='/run')
app.register_blueprint(stack_bp, url_prefix='/stack')
app.register_blueprint(ollama_bp, url_prefix='/ollama')
app.register_blueprint(status_bp, url_prefix='/status')

@app.route("/")
def home():
    return {
        "weavr_agent": "online",
        "message": "🧵 WEAVR is listening. Route /run or /stack to begin stackweaving.",
        "status": "OK"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5151, debug=True)
