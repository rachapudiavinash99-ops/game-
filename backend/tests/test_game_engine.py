def test_start_quick_challenge(client, user_token):
    response = client.post(
        "/api/v1/games/start",
        headers={"Authorization": f"Bearer {user_token}"},
        json={"mode": "QUICK_CHALLENGE", "question_count": 3}
    )
    assert response.status_code == 200
    session = response.json()
    assert session["mode"] == "QUICK_CHALLENGE"
    assert session["status"] == "IN_PROGRESS"
    assert len(session["questions"]) == 3
    assert session["score"] == 0


def test_submit_answer_and_score(client, user_token):
    # Start game session
    start_res = client.post(
        "/api/v1/games/start",
        headers={"Authorization": f"Bearer {user_token}"},
        json={"mode": "QUICK_CHALLENGE", "question_count": 2}
    )
    session_id = start_res.json()["id"]
    first_q = start_res.json()["questions"][0]
    task_id = first_q["task"]["id"]
    ans_id = first_q["task"]["answers"][0]["id"]

    # Submit answer
    sub_res = client.post(
        "/api/v1/games/submit-answer",
        headers={"Authorization": f"Bearer {user_token}"},
        json={
            "session_id": session_id,
            "task_id": task_id,
            "selected_answer_id": ans_id,
            "time_spent_seconds": 3.5
        }
    )
    assert sub_res.status_code == 200
    ans_data = sub_res.json()
    assert "is_correct" in ans_data
    assert "points_earned" in ans_data
    assert "explanation" in ans_data


def test_finish_game_session(client, user_token):
    start_res = client.post(
        "/api/v1/games/start",
        headers={"Authorization": f"Bearer {user_token}"},
        json={"mode": "QUICK_CHALLENGE", "question_count": 1}
    )
    session_id = start_res.json()["id"]

    finish_res = client.post(
        f"/api/v1/games/finish/{session_id}",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert finish_res.status_code == 200
    result = finish_res.json()
    assert result["session_id"] == session_id
    assert "xp_earned" in result
    assert "accuracy" in result
