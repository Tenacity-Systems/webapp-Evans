from app import app


def test_services_endpoint():
    client = app.test_client()

    response = client.get("/api/services")

    assert response.status_code == 200
    assert len(response.get_json()) >= 5


def test_enquiry_requires_fields():
    client = app.test_client()

    response = client.post("/api/enquiries", json={"name": "Student"})

    assert response.status_code == 400
