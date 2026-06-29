"""Health check endpoints."""
from flask import Blueprint, jsonify

bp = Blueprint("health", __name__, url_prefix="/api/health")


@bp.route("/", methods=["GET"])
def status():
    """Return API health status."""
    return jsonify({"status": "ok", "version": "0.1.0"}), 200


@bp.route("/ping", methods=["GET"])
def ping():
    """Simple ping endpoint."""
    return jsonify({"message": "pong"}), 200
