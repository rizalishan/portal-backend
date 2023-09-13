from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "jobs" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "title" VARCHAR(126),
    "description" VARCHAR(126),
    "location" VARCHAR(126)
);
COMMENT ON TABLE "jobs" IS 'The Jobs Model';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "jobs";"""
