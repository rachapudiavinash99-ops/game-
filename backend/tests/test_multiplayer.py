def test_create_and_list_multiplayer_rooms(client, user_token):
    create_res = client.post(
        "/api/v1/multiplayer/rooms",
        headers={"Authorization": f"Bearer {user_token}"},
        json={
            "name": "Championship Arena",
            "difficulty": "MEDIUM",
            "max_players": 4,
            "question_count": 5,
            "time_per_question": 15
        }
    )
    assert create_res.status_code == 200
    room_data = create_res.json()
    assert room_data["name"] == "Championship Arena"
    assert "room_code" in room_data
    assert room_data["status"] == "WAITING"

    list_res = client.get("/api/v1/multiplayer/rooms")
    assert list_res.status_code == 200
    rooms = list_res.json()
    assert any(r["room_code"] == room_data["room_code"] for r in rooms)
