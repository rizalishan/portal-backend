from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "portfolio" DROP COLUMN "kv";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "portfolio" ADD "kv" VARCHAR(256);"""
