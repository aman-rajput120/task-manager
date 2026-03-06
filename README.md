# TaskFlow — Task Manager with User Authentication

A full-featured task management web application with user authentication, built with Python Django and SQLite.

## Features
- 🔐 User registration & login (with hashed passwords)
- ✅ Add, view, edit, complete, and delete tasks
- 🎨 Beautiful dark theme UI with gradient accents
- 🔖 Task priorities (High / Medium / Low)
- 🏷️ Task categories (Work / Personal / Shopping / Health / Other)
- 📅 Due dates
- 🔍 Search, filter, and sort tasks
- 📊 Stats dashboard (total, completed, pending, high-priority)
- 💾 Persistent SQLite storage (one DB file per app instance)

## Project Structure

```
taskmanager/
├── requirements.txt    ← Python dependencies
│
└── django_version/     ← Full Django version (requires Django installed)
    ├── manage.py
    ├── taskmanager/    ← Django project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── tasks/          ← Django app
        ├── models.py
        ├── views.py
        ├── forms.py
        ├── urls.py
        ├── admin.py
        └── templates/tasks/
            ├── base.html
            ├── login.html
            ├── register.html
            ├── dashboard.html
            └── edit_task.html
```



### 4. Register an account and start adding tasks!

---

## Django Version Setup

### 1. Install Django
```bash
pip install django
```

### 2. Run migrations
```bash
cd django_version
python manage.py makemigrations
python manage.py migrate
```

### 3. Start the server
```bash
python manage.py runserver
```

### 4. Open: http://127.0.0.1:8000

---

## How It Works

### Authentication
- Passwords are hashed using  Django's built-in hasher (Django)
- Sessions are managed server-side with secure cookies
- Each user's tasks are completely isolated

### Task Management
- Every task has: title, description, priority, category, due date, status
- Tasks can be marked complete/pending by clicking the circle checkbox
- All data persists in SQLite (no extra database server needed)

### File Handling
- Django version: `db.sqlite3` SQLite file

---

## Tech Stack
| Component | Django Version |
|-----------|--------------|----------------|
| Framework | Django 4.x+    |
| Database  | SQLite via ORM |
| Auth      | Django Auth |
| Templates | Django Templates |
| Styling   | Same CSS |

---

