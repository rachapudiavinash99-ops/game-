# Test Your Knowledge â€” Modern Python Full-Stack Gaming Platform

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18-61dafb.svg?logo=react)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.2%2B-3178c6.svg?logo=typescript)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4%2B-38bdf8.svg?logo=tailwind-css)](https://tailwindcss.com/)
[![WebSockets](https://img.shields.io/badge/WebSockets-Real--Time-orange.svg)](https://websockets.readthedocs.io/)


---

## 1. Project Overview

**Test Your Knowledge** is an authoritative, end-to-end Python full-stack gaming and challenge platform. Built with a **FastAPI** backend and a modern **React 18 + TypeScript + Vite + Tailwind CSS** frontend, Test Your Knowledge offers single-player challenge arenas and real-time multiplayer WebSocket battles across 15+ dynamic knowledge domains.

---

## 2. System Architecture

```
                               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                               â”‚         React 18 + TypeScript Client         â”‚
                               â”‚   Vite, Tailwind CSS, Lucide Icons, Audio    â”‚
                               â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                                      â”‚ REST APIs & WebSockets
                                                      â–¼
                               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                               â”‚           FastAPI Backend Service            â”‚
                               â”‚  - JWT Authentication & RBAC                 â”‚
                               â”‚  - Authoritative Scoring & Streak Multipliers â”‚
                               â”‚  - Dynamic XP Progression & Level Formula    â”‚
                               â”‚  - Real-Time WebSocket Multiplayer Engine    â”‚
                               â”‚  - Task Engine & Auto-Unlock Achievements    â”‚
                               â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                               â”‚              â”‚
                                               â–¼              â–¼
                               â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                               â”‚   SQLAlchemy Models    â”‚   â”‚ SQLite / Postgreâ”‚
                               â”‚   (Relational Schema)  â”‚   â”‚ Database Engine â”‚
                               â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

---

## 3. Core Game Modes

1. **Quick Challenge**:
   - Instant randomized question challenge with dynamic time bonuses, combo streaks, and immediate feedback.
2. **Topic Challenge**:
   - Choose specific domains (Python, SQL, Cybersecurity, AI/ML, Science, Algorithms, History, etc.) and difficulty levels (*Easy*, *Medium*, *Hard*, *Expert*).
3. **Time Attack (60s)**:
   - High-intensity 60-second speedrun to solve as many questions as possible with speed streak multipliers.
4. **Survival Mode**:
   - 3 lives / sudden death mode where difficulty escalates as your combo streak grows.
5. **Real-Time Multiplayer Showdown**:
   - WebSocket multiplayer lobby and arena. Create or join custom rooms with a 6-digit code, ready up, receive synchronized live questions, and battle for the top spot on the live match podium.

---

## 4. Extensible Topic & Task Engine

Test Your Knowledge is built with an unlimited task creation engine. Administrators can continuously add topics, categories, difficulties, and questions with explanations without changing any game logic.

### 15 Seeded Topic Universes:
- **Python Programming** (Syntax, OOP, GIL, Asyncio, Memory Internals)
- **Computer Science & Programming** (Paradigms, Memory, SOLID, Idempotency)
- **SQL & Relational Databases** (Joins, B-Tree Indexing, ACID, 3NF)
- **Modern Web Development** (React, Virtual DOM, CSS Flexbox/Grid, CORS)
- **Cybersecurity & Cryptography** (SQLi, AES/RSA, CSP, XSS Mitigations)
- **Mathematics & Discrete Math** (Permutations, Linear Algebra, Euler Paths)
- **Natural Sciences** (Physics Constants, Cell Respiration, Astronomy)
- **General Knowledge & Trivia** (Historic Milestones, Scientific Facts)
- **Logical Reasoning & Puzzles** (Contrapositives, Sequence Deductions)
- **Data Analytics & Statistics** (Distributions, Variance, Type I/II Errors)
- **Artificial Intelligence & ML** (Transformers, Attention, Dropout)
- **Networking & Cloud** (TCP 3-Way Handshake, DNS Records, OSI Layer)
- **Data Structures & Algorithms** (Binary Search, Dijkstra, Big-O)
- **World History** (Magna Carta, Revolutions, World Empires)
- **World Geography** (Topography, Oceanic Trenches, Capitals)

---

## 5. Scoring, XP & Progression Math

### Base Points by Difficulty:
$$	ext{Base Score} = egin{cases} 10 & 	ext{EASY} \ 20 & 	ext{MEDIUM} \ 35 & 	ext{HARD} \ 50 & 	ext{EXPERT} \end{cases}$$

### Speed Bonus & Streak Multiplier:
$$	ext{Speed Bonus} = 	ext{round}\left( rac{	ext{Time Remaining}}{	ext{Total Time}} 	imes 15 
ight)$$
$$	ext{Streak Multiplier} = \min(2.5, 1.0 + (	ext{Streak} 	imes 0.1))$$
$$	ext{Final Question Points} = \lceil (	ext{Base} + 	ext{Speed Bonus}) 	imes 	ext{Streak Multiplier} 
ceil$$

### Level Progression Threshold:
$$	ext{XP Required for Level } L = 	ext{round}\left( 100 	imes L^{1.5} 
ight)$$

---

## 6. Authentication & Security (RBAC)

- Secure password hashing using native **bcrypt**.
- Stateless **JWT Access & Refresh Token** authentication with standard token refresh rotation.
- Role-Based Access Control (**USER**, **MODERATOR**, **ADMIN**).
- Centralized exception middleware and CORS policy.

### Default Seed Credentials:
- **Admin**: `admin` / `AdminPassword123!`
- **Demo Player**: `alex_cyber` / `PlayerPass123!`
- **Demo Player 2**: `sarah_code` / `PlayerPass123!`

---

## 7. Installation & Quick Start

### Prerequisites
- **Python 3.12+**
- **Node.js 18+ / 20+**
- **Git**

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python -m app.seeds.seed_runner
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 3. One-Click Launch (Windows)
Double click `start.bat` or run:
```powershell
./start.ps1
```

- **Frontend Application**: `http://localhost:5173`
- **Swagger Interactive API Docs**: `http://localhost:8000/docs`
- **ReDoc API Reference**: `http://localhost:8000/redoc`

---

## 8. Docker Deployment

Launch the complete containerized stack (Frontend, Backend, Database) with a single command:

```bash
docker compose up --build -d
```

---

## 9. Automated Testing Suite

The backend contains a comprehensive Pytest test suite covering authentication, game sessions, task filtering, scoring algorithms, achievement triggers, multiplayer rooms, and administrative controls.

Run all tests:
```bash
pytest backend/tests -v
```

---

## 10. API Specification Reference

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `GET` | `/api/v1/health` | Service health status | No |
| `POST` | `/api/v1/auth/register` | Register new player | No |
| `POST` | `/api/v1/auth/login` | Login and receive JWT pair | No |
| `POST` | `/api/v1/auth/refresh` | Refresh access token | No |
| `GET` | `/api/v1/auth/me` | Current user profile | Yes |
| `GET` | `/api/v1/topics` | List active topics | No |
| `GET` | `/api/v1/tasks` | Filter tasks by topic/difficulty | No |
| `POST` | `/api/v1/games/start` | Initialize game session | Optional |
| `POST` | `/api/v1/games/submit-answer` | Submit answer & calculate score | Optional |
| `POST` | `/api/v1/games/finish/{id}` | Complete game session & earn XP | Optional |
| `POST` | `/api/v1/multiplayer/rooms` | Create multiplayer room | Yes |
| `GET` | `/api/v1/multiplayer/rooms` | List active waiting lobbies | No |
| `WS` | `/ws/multiplayer/{room_code}` | Real-time WebSocket battle match | Token |
| `GET` | `/api/v1/leaderboards/global` | Global leaderboard rankings | No |
| `GET` | `/api/v1/achievements` | List achievements and statuses | Optional |
| `GET` | `/api/v1/challenges/daily` | Today's daily quest | Optional |
| `GET` | `/api/v1/admin/users` | Admin user moderation | Admin |
| `POST` | `/api/v1/admin/tasks` | Create new challenge question | Admin |
| `GET` | `/api/v1/admin/audit-logs` | View system audit trail | Admin |

---

## 11. License
Proprietary software. All rights reserved.
