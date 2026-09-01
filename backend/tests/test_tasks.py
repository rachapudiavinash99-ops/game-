def test_list_topics(client):
    response = client.get("/api/v1/topics")
    assert response.status_code == 200
    topics = response.json()
    assert len(topics) >= 10
    slugs = [t["slug"] for t in topics]
    assert "python" in slugs
    assert "cybersecurity" in slugs


def test_list_tasks(client):
    response = client.get("/api/v1/tasks?limit=10")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) > 0
    task = tasks[0]
    assert "title" in task
    assert "question" in task
    assert "answers" in task
    assert len(task["answers"]) > 0


def test_filter_tasks_by_difficulty(client):
    response = client.get("/api/v1/tasks?difficulty=EASY")
    assert response.status_code == 200
    tasks = response.json()
    for t in tasks:
        assert t["difficulty"] == "EASY"
