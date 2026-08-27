def test_unregister_success_removes_participant(client):
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/Chess Club/participants/{email}")

    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from Chess Club"}

    activities_response = client.get("/activities")
    participants = activities_response.json()["Chess Club"]["participants"]
    assert email not in participants


def test_unregister_nonexistent_activity_returns_404(client):
    response = client.delete("/activities/Robotics/participants/test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_missing_participant_returns_404(client):
    response = client.delete("/activities/Chess Club/participants/not-registered@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
