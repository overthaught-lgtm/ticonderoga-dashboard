"""Main Flask application factory."""
from flask import Flask, jsonify
from api.routes import health


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    
    if config:
        app.config.update(config)
    
    # Register blueprints
    app.register_blueprint(health.bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Not found"}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
