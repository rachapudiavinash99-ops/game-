def test_admin_list_users(client, admin_token):
    response = client.get(
        "/api/v1/admin/users",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    users = response.json()
    assert len(users) >= 4


def test_admin_permission_denied_for_regular_user(client, user_token):
    response = client.get(
        "/api/v1/admin/users",
        headers={"Authorization": f"Bearer {user_token}"}
    )
    assert response.status_code == 403


def test_admin_create_task(client, admin_token):
    response = client.post(
        "/api/v1/admin/tasks",
        headers={"Authorization": f"Bearer {admin_token}"},
        json={
            "topic_id": 1,
            "title": "Asyncio Event Loop Invalidation",
            "question": "What happens when an event loop is closed while coroutines are still pending?",
            "difficulty": "HARD",
            "points": 35,
            "time_limit_seconds": 25,
            "explanation": "Pending tasks are cancelled or trigger runtime warnings.",
            "tags": "python,asyncio,advanced",
            "answers": [
                {"text": "Pending tasks trigger cancellation warnings.", "is_correct": True},
                {"text": "They automatically migrate to a thread pool.", "is_correct": False},
                {"text": "They block the OS process indefinitely.", "is_correct": False},
                {"text": "They serialize to disk.", "is_correct": False}
            ]
        }
    )
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == "Asyncio Event Loop Invalidation"
