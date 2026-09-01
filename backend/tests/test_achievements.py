def test_list_achievements(client):
    response = client.get("/api/v1/achievements")
    assert response.status_code == 200
    achievements = response.json()
    assert len(achievements) >= 5
    codes = [a["code"] for a in achievements]
    assert "FIRST_GAME" in codes
    assert "PERFECT_ROUND" in codes
