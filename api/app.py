import os
from datetime import datetime, timezone

from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
MONGO_DB = os.getenv("MONGO_DB", "pki_cloud")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client[MONGO_DB]
enquiries = db.enquiries

SERVICES = [
    {
        "name": "DevOps & ReleasePilot",
        "description": "Reliable cloud systems, faster releases and practical DevOps automation.",
        "icon": "🚀",
    },
    {
        "name": "Web & App Development",
        "description": "Modern applications and websites designed around real business needs.",
        "icon": "💻",
    },
    {
        "name": "Cloud Infrastructure",
        "description": "Secure, scalable AWS, Azure and cloud infrastructure for growing teams.",
        "icon": "☁️",
    },
    {
        "name": "Security & Compliance",
        "description": "Security practices that protect applications, people and business data.",
        "icon": "🛡️",
    },
    {
        "name": "IT Consulting",
        "description": "Clear technical guidance and practical solutions for complex problems.",
        "icon": "🧭",
    },
    {
        "name": "Cloud Migration",
        "description": "Move workloads to the cloud carefully while keeping your business running.",
        "icon": "🔄",
    },
    {
        "name": "Monitoring & Observability",
        "description": "Visibility into systems so problems can be found before customers notice.",
        "icon": "📊",
    },
    {
        "name": "IT Support & Infrastructure",
        "description": "Keep technology healthy, available and ready for the next challenge.",
        "icon": "⚙️",
    },
]


@app.get("/api/health")
def health():
    try:
        client.admin.command("ping")
        database = "ok"
    except Exception:
        database = "unavailable"

    return jsonify({
        "status": "ok",
        "service": "pki-api",
        "database": database,
    })


@app.get("/api/services")
def get_services():
    return jsonify(SERVICES)


@app.post("/api/enquiries")
def create_enquiry():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    message = str(data.get("message", "")).strip()

    if not name or not email or not message:
        return jsonify({"error": "name, email and message are required"}), 400

    document = {
        "name": name,
        "email": email,
        "message": message,
        "created_at": datetime.now(timezone.utc),
    }

    result = enquiries.insert_one(document)

    return jsonify({
        "message": "Enquiry received",
        "id": str(result.inserted_id),
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
