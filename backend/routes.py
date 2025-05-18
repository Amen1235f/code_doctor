from flask import Blueprint, request, jsonify
import asyncio
import extract as extraction_logic  # Import the extraction logic from extract.py

routes = Blueprint('routes', __name__)

@routes.route('/extract', methods=['POST'])
def extract_repo():
    data = request.get_json()
    repo_url = data.get('repo_url')
    if not repo_url:
        return jsonify({'error': 'repo_url is required'}), 400
    try:
        # Run the async extraction orchestrator
        result = asyncio.run(extraction_logic.process_github_repository_async(repo_url))
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
