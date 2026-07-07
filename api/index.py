from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    # Handle the root path test
    if path == "" and request.method == 'GET':
        return "Quill Flask is live"
        
    # Handle the API data pipeline test
    if path == "save" and request.method == 'POST':
        data = request.get_json() or {}
        return jsonify({
            "status": "saved", 
            "content": data.get("content", "No content provided")
        })

    # Fallback error mapping
    return jsonify({"error": f"Path /{path} not found or method not allowed"}), 404
