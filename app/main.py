import os
from fastapi import FastAPI
from .resources.portfolio import routes as portfolio_routes
from .resources.jobs import routes as jobs_routes
from .resources.services import routes  as services_routes
from .docs import meta_tags, meta_title, meta_description, meta_version
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise


app = FastAPI(
    title=meta_title,
    description=meta_description,   
    version=meta_version,
    dependencies=[],
    openapi_tags=meta_tags,
)

def get_db_url():
    USER = os.getenv("DATABSE_USER", "postgres")
    PASSWORD = os.getenv("DATABSE_PASSWORD", "admin")
    HOST = os.getenv("DATABSE_HOST", "localhost")
    PORT = os.getenv("DATABSE_PORT", "5432")
    NAME = os.getenv("DATABSE_NAME", "Portal-Backend")

    return f"postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"




MODULES_LIST = [
    "app.resources.portfolio.model",
    "app.resources.jobs.model",
    "app.resources.services.model"
]


Tortoise.init_models(MODULES_LIST, "models")   




register_tortoise(
    app,
    db_url=get_db_url(),
    modules={"models": MODULES_LIST},
    add_exception_handlers=True,
    generate_schemas=True,
)



TORTOISE_ORM_MIGRATIONS = {
    "connections": {"default": get_db_url()},
    "apps": {
        "models": {
            "models": MODULES_LIST + ["aerich.models"],
            "default_connection": "default",
        },
    },
}



app.include_router(portfolio_routes.router)
app.include_router(jobs_routes.router)
app.include_router(services_routes.router)
