def set_postgres():
    """pip install python-dotenv
--- settings.py

from dotenv import load_dotenv
import os
# Загружаем .env
load_dotenv(BASE_DIR / ".env")

DATABASES = {
"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "database"),
        "USER": os.getenv("POSTGRES_USER", "user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "password"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

--- .env

POSTGRES_DB=database
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
    """
    ...