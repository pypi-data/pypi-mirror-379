def set_postgres():
    """pip install python-dotenv
--- settings.py

from dotenv import load_dotenv
# Загружаем .env
load_dotenv(BASE_DIR / ".env")

DATABASES = {
"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "crm_db"),
        "USER": os.getenv("POSTGRES_USER", "crm_user"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "crm_pass"),
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}

--- .env

POSTGRES_DB=crm_db
POSTGRES_USER=crm_user
POSTGRES_PASSWORD=crm_pass
POSTGRES_HOST=db
POSTGRES_PORT=5432
    """
    ...