def test_signup_success_adds_participant(client):
    email = "newstudent@mergington.edu"

    response = client.post(f"/activities/Chess Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for Chess Club"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email in participants


def test_signup_nonexistent_activity_returns_404(client):
    response = client.post("/activities/Robotics/signup?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_email_returns_400(client):
    response = client.post("/activities/Chess Club/signup?email=michael@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
