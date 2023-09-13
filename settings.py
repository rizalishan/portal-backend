import os

MODULES_LIST = [
    "app.resources.portfolio.model"
]


def get_db_url():
    USER = os.getenv("DATABSE_USER", "postgres")
    PASSWORD = os.getenv("DATABSE_PASSWORD", "admin")
    HOST = os.getenv("DATABSE_HOST", "localhost")
    PORT = os.getenv("DATABSE_PORT", "5432")
    NAME = os.getenv("DATABSE_NAME", "Portal-Backend")

    return f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"


TORTOISE_ORM = {
    "connections": {"default": get_db_url()},
    "apps": {
        "models": {
            "models": MODULES_LIST + ["aerich.models"],
            "default_connection": "default",
        },
    },
}
