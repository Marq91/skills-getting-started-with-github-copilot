def test_get_activities_returns_activity_dictionary(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_get_activities_contains_expected_activity_fields(client):
    response = client.get("/activities")
    payload = response.json()

    for activity in payload.values():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity
        assert isinstance(activity["participants"], list)
