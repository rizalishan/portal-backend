from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "portfolio" ADD "kv" VARCHAR(256);
        ALTER TABLE "portfolio" ADD "services" VARCHAR(126);
        ALTER TABLE "portfolio" ADD "techologies" VARCHAR(126);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "portfolio" DROP COLUMN "kv";
        ALTER TABLE "portfolio" DROP COLUMN "services";
        ALTER TABLE "portfolio" DROP COLUMN "techologies";"""
