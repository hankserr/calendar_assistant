# AI-Powered Calendar Assistant

## Project Overview
The AI-Powered Calendar Assistant is a smart backend service designed to help users automatically schedule tasks into their calendar based on priority, duration, and personal preferences. The initial version focuses on core infrastructure, task management, and Apple Calendar integration.

## Features
- **Task Input System:**
  - API endpoints to add and retrieve tasks with metadata (title, deadline, duration, priority, type).
  - Backend stores and retrieves tasks from a PostgreSQL database.
- **Calendar Sync (Planned):**
  - Integration with Apple Calendar (CalDAV/EventKit).
  - Identify free/busy time slots for scheduling.
- **Rule-Based Scheduling Engine (Planned):**
  - Automatically insert tasks into available time blocks.
  - Prioritize based on urgency and task type.
  - Avoid scheduling during blocked or Do Not Disturb times.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Deployment:** AWS EC2 (recommended)
- **Calendar Integration:** CalDAV or EventKit (future)

## Getting Started

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd calendar_assistant
```

### 2. Set Up Python Environment
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Edit the `.env` file with your PostgreSQL credentials:
```
DATABASE_URL=postgresql://youruser:yourpassword@localhost/calendar_db
```

### 4. Set Up PostgreSQL
```sh
sudo -u postgres psql
# In the psql shell:
CREATE DATABASE calendar_db;
CREATE USER youruser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE calendar_db TO youruser;
\q
```

### 5. Run the Application
```sh
source venv/bin/activate
./run.sh
```
The API will be available at `http://localhost:8000` by default.

## API Endpoints
- `POST /add-task` — Add a new task
- `GET /get-tasks/{user_id}` — Retrieve all tasks for a user
- `POST /sync-calendar` — (Stub) Sync with Apple Calendar
- `POST /schedule-tasks` — (Stub) Schedule tasks automatically

## Roadmap
- [x] Core infrastructure and task management
- [ ] Apple Calendar integration
- [ ] Rule-based scheduling engine
- [ ] AI-based rescheduling and natural language input
- [ ] Analytics dashboard and multi-calendar support

## Contributing
Contributions are welcome! Please open issues or submit pull requests for improvements and new features.

## License
This project is licensed under the MIT License.
