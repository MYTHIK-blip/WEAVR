from flask import Blueprint, jsonify
import yaml
import os

stack_bp = Blueprint('stack', __name__)
PIPELINE_PATH = os.path.join(os.path.dirname(__file__), '..', 'pipeline.yaml')

@stack_bp.route('/', methods=['GET'])
def get_stack_pipeline():
    try:
        with open(PIPELINE_PATH, 'r') as file:
            pipeline_data = yaml.safe_load(file)
        return jsonify({
            "status": "🧵 stack pipeline loaded",
            "pipeline": pipeline_data
        }), 200
    except FileNotFoundError:
        return jsonify({
            "status": "error",
            "message": "pipeline.yaml not found"
        }), 404
    except yaml.YAMLError as e:
        return jsonify({
            "status": "error",
            "message": "invalid YAML format",
            "details": str(e)
        }), 400
    
@stack_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "health": "ok",
        "status": "running",
        "uptime_hint": "container reachable, blueprint functional"
    })
