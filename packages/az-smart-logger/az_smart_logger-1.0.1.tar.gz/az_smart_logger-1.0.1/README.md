# Smart Logger

**Smart Logger** is a **Python logging library** with **FastAPI, Flask, and Django** support.
It provides **UUID-based logs**, **date/parent_folder structured logs**, **database metadata storage**, and a **FastAPI dashboard** with filters, real-time monitoring, charts.

---

## Features

* **Multi-framework support:** FastAPI, Flask, Django
* **Structured logging:** UUID for each log entry
* **Dynamic folder structure:** `date/parent_folder/filename.log`
* **Database metadata storage** (default SQLite)
* **SmartLogger class with logging levels:**

  * `logger.info()`
  * `logger.error()`
  * `logger.warning()`
  * `logger.critical()`
  * `logger.debug()`
* **FastAPI Dashboard UI:**

  * Real-time logs
  * Filter logs by **date, time, UUID, log type**
  * Bar charts for **daily, monthly, yearly log insights**
  * System info cards and statistics
  * Interactive UI with logout functionality
* **Secure:** input sanitization, token-based authentication, blacklist token support
* **CLI commands** for user management, configuration, and server launch

---

## Installation

```bash
pip install smart-logger
```

---

## Usage

### 1. FastAPI Example

```python
from fastapi import FastAPI
from smart_logger import SmartLogger

app = FastAPI()
logger = SmartLogger()

@app.get("/")
def home():
    logger.info("Home accessed")  # UUID, folder, filename auto-detected
    return {"message": "Hello FastAPI"}
```

### 2. Flask Example

```python
from flask import Flask
from smart_logger import SmartLogger

app = Flask(__name__)
logger = SmartLogger()

@app.route("/")
def home():
    logger.info("Home accessed")
    return "Hello Flask"
```

### 3. Django Example

```python
from smart_logger import SmartLogger

logger = SmartLogger()

def example_view(request):
    logger.info("Django view accessed")
    from django.http import HttpResponse
    return HttpResponse("Hello Django")
```

---

## CLI Commands

### Launch Dashboard UI

```bash
smart-logger ui --host 127.0.0.1 --port 8000 --workers 1 --reload False
```

* `--reload` optional (default `False`)
* Runs **isolated FastAPI server** independent of main project

### Initialize Database Tables

```bash
smart-logger init-db
```

### Admin User Management

* **Create admin user:**

```bash
smart-logger create-admin-user
```

* **Change password:**

```bash
smart-logger change-password <email>
```

* **Forgot password (reset without old password):**

```bash
smart-logger forgot-password <email>
```

* **List users:**

```bash
smart-logger list-users
```

* **Delete user:**

```bash
smart-logger delete-user <email>
```

### Configuration Management

* **Set global config:**

```bash
smart-logger set_config
```

* **Show active config:**

```bash
smart-logger show_config
```

* **Create default config:**

```bash
smart-logger make-smart-logger-default-conf
```

---

## Folder Structure

```
smart_logger/
├── cli/
├── config/
├── core/
├── exceptions/
├── models/
├── security/
├── ui/
├── tests/
├── examples/
├── setup.py
├── pyproject.toml
├── setup.cfg
├── LICENSE
└── README.md
```

* `core/` → Logger class, DB handlers
* `ui/` → Dashboard server, templates, static files
* `cli/` → Commands for server launch, user management
* `models/` → SQLAlchemy models
* `security/` → Auth, middleware, blacklist token
* `config/` → Default and global configuration
* `tests/` → Unit and integration tests
* `examples/` → Usage examples

---

## Logging API

```python
from smart_logger import SmartLogger

logger = SmartLogger()

logger.info("Informational message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
logger.debug("Debugging message")
```

* **Folder and file auto-detection**: module name used if not provided
* **UUID generated for every log entry**
* **Database metadata** stored automatically

---

## Dashboard Features

* **Real-time log view**
* **Filter by:** date, time, UUID, log type
* **Download:** CSV, JSON
* **Charts:**

  * Daily/Monthly/Yearly error insights
  * Bar charts by log type
* **System info:** CPU, memory, uptime
* **Cards & Stats** for quick overview
* **Logout button** for secure access

---

## License

MIT License. See LICENSE file for details.

---

✅ **Key Points:**

1. **Clear instructions** for installation and usage.
2. **Examples for FastAPI, Flask, Django** included.
3. **CLI instructions** for UI and DB initialization.
4. **Folder structure overview** for developers.
5. **Ready for PyPI** and GitHub documentation.