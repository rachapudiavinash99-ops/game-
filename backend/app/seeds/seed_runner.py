
import logging
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, Base, engine
from app.core.security import get_password_hash
from app.models.user import User, Profile, UserRole
from app.models.topic import Topic
from app.models.task import Task, Answer
from app.models.achievement import Achievement
from app.seeds.seed_data import TOPICS_DATA, ACHIEVEMENTS_DATA, TASKS_DATA

logger = logging.getLogger("gameverse.seeds")


def run_seeds(db: Session):
    logger.info("Initializing database tables and running GameVerse seeds...")
    Base.metadata.create_all(bind=engine)

    # 1. Seed Users
    seed_users = [
        {"username": "admin", "email": "admin@gameverse.io", "password": "AdminPassword123!", "role": UserRole.ADMIN.value, "display_name": "GameVerse Admin", "level": 10, "xp": 4500, "score": 12800},
        {"username": "alex_cyber", "email": "alex@gameverse.io", "password": "PlayerPass123!", "role": UserRole.USER.value, "display_name": "CyberNinja", "level": 6, "xp": 1850, "score": 6400},
        {"username": "sarah_code", "email": "sarah@gameverse.io", "password": "PlayerPass123!", "role": UserRole.USER.value, "display_name": "SarahDev", "level": 5, "xp": 1400, "score": 5200},
        {"username": "matrix_neo", "email": "neo@gameverse.io", "password": "PlayerPass123!", "role": UserRole.USER.value, "display_name": "Neo", "level": 8, "xp": 3100, "score": 9600},
        {"username": "elena_data", "email": "elena@gameverse.io", "password": "PlayerPass123!", "role": UserRole.USER.value, "display_name": "Elena Stats", "level": 4, "xp": 950, "score": 3800}
    ]

    for u_data in seed_users:
        existing = db.query(User).filter(User.username == u_data["username"]).first()
        if not existing:
            user = User(
                username=u_data["username"],
                email=u_data["email"],
                hashed_password=get_password_hash(u_data["password"]),
                role=u_data["role"],
                is_active=True
            )
            db.add(user)
            db.flush()

            profile = Profile(
                user_id=user.id,
                display_name=u_data["display_name"],
                avatar_url=f"https://api.dicebear.com/7.x/bottts/svg?seed={u_data['username']}",
                level=u_data["level"],
                current_xp=u_data["xp"],
                next_level_xp=int(100 * (u_data["level"] ** 1.5)),
                total_score=u_data["score"],
                total_games=u_data["level"] * 4,
                wins=int(u_data["level"] * 2.5),
                win_rate=65.0,
                current_streak=3,
                best_streak=7
            )
            db.add(profile)

    # 2. Seed Topics
    topic_map = {}
    for t_data in TOPICS_DATA:
        existing_topic = db.query(Topic).filter(Topic.slug == t_data["slug"]).first()
        if not existing_topic:
            topic = Topic(
                name=t_data["name"],
                slug=t_data["slug"],
                description=t_data["description"],
                icon=t_data["icon"],
                color=t_data["color"],
                order=t_data["order"],
                is_active=True
            )
            db.add(topic)
            db.flush()
            topic_map[t_data["slug"]] = topic.id
        else:
            topic_map[t_data["slug"]] = existing_topic.id

    # 3. Seed Achievements
    for a_data in ACHIEVEMENTS_DATA:
        existing_ach = db.query(Achievement).filter(Achievement.code == a_data["code"]).first()
        if not existing_ach:
            ach = Achievement(
                code=a_data["code"],
                title=a_data["title"],
                description=a_data["description"],
                icon=a_data["icon"],
                category=a_data["category"],
                requirement_type=a_data["requirement_type"],
                requirement_value=a_data["requirement_value"],
                xp_reward=a_data["xp_reward"],
                badge_color=a_data["badge_color"]
            )
            db.add(ach)

    # 4. Seed Tasks and Answers
    for task_item in TASKS_DATA:
        topic_id = topic_map.get(task_item["topic_slug"])
        if not topic_id:
            continue

        existing_task = db.query(Task).filter(Task.title == task_item["title"]).first()
        if not existing_task:
            task = Task(
                topic_id=topic_id,
                title=task_item["title"],
                question=task_item["question"],
                task_type="MULTIPLE_CHOICE",
                difficulty=task_item["difficulty"],
                points=task_item["points"],
                time_limit_seconds=task_item["time_limit_seconds"],
                explanation=task_item["explanation"],
                tags=task_item["tags"],
                is_active=True
            )
            db.add(task)
            db.flush()

            for idx, ans in enumerate(task_item["answers"]):
                answer_obj = Answer(
                    task_id=task.id,
                    text=ans["text"],
                    is_correct=ans["is_correct"],
                    order=idx
                )
                db.add(answer_obj)

    db.commit()
    logger.info("Database seeding completed.")


if __name__ == "__main__":
    db = SessionLocal()
    try:
        run_seeds(db)
        print("Database initialized and seeded successfully!")
    finally:
        db.close()
