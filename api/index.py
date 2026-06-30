from flask import Flask, jsonify, request
from db import init_db, get_db
import time

app = Flask(__name__)
init_db()

@app.route("/")
def root():
    return jsonify({"status": "ok", "system": "EARS", "version": "1.0.0"})

@app.route("/hubs")
def hubs():
    db = get_db()
    rows = db.execute("SELECT * FROM hubs").fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])

@app.route("/hubs/<int:hub_id>/status")
def hub_status(hub_id):
    db = get_db()
    row = db.execute("SELECT * FROM hubs WHERE id=?", (hub_id,)).fetchone()
    db.close()
    if not row:
        return jsonify({"error": "not found"}), 404
    return jsonify(dict(row))

@app.route("/ears/ingest", methods=["POST"])
def ingest():
    data = request.get_json()
    hub_id   = data.get("hub_id", 1)
    event    = data.get("event_type", "movement")
    velocity = data.get("velocity", 0.0)
    dwell    = data.get("dwell", 0.0)
    acoustic = data.get("acoustic", 0.0)
    affinity = data.get("affinity", "READY")
    db = get_db()
    db.execute(
        "INSERT INTO ears_events (hub_id, event_type, velocity, dwell, acoustic, affinity, raw) VALUES (?,?,?,?,?,?,?)",
        (hub_id, event, velocity, dwell, acoustic, affinity, str(data))
    )
    db.commit()
    db.close()
    return jsonify({"status": "ingested", "hub_id": hub_id})

@app.route("/ears/stream")
def stream():
    hub_id = request.args.get("hub_id", 1, type=int)
    limit  = request.args.get("limit", 50, type=int)
    db = get_db()
    rows = db.execute(
        "SELECT * FROM ears_events WHERE hub_id=? ORDER BY ts DESC LIMIT ?",
        (hub_id, limit)
    ).fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])

@app.route("/dap/score", methods=["POST"])
def dap_score():
    data     = request.get_json()
    hub_id   = data.get("hub_id", 1)
    persona  = data.get("persona", "UNKNOWN")
    ltv      = data.get("ltv_score", 0.0)
    signal   = data.get("signal_index", 0.0)
    db = get_db()
    db.execute(
        "INSERT INTO dap_scores (hub_id, persona, ltv_score, signal_index) VALUES (?,?,?,?)",
        (hub_id, persona, ltv, signal)
    )
    db.commit()
    db.close()
    return jsonify({"status": "scored", "persona": persona, "ltv": ltv})

@app.route("/dap/scores")
def dap_scores():
    hub_id = request.args.get("hub_id", 1, type=int)
    db = get_db()
    rows = db.execute(
        "SELECT * FROM dap_scores WHERE hub_id=? ORDER BY ts DESC LIMIT 100",
        (hub_id,)
    ).fetchall()
    db.close()
    return jsonify([dict(r) for r in rows])

@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "hubs": 3,
        "system": "TEAKWOOD",
        "uptime": time.time()
    })
