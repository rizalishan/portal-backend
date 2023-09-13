from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "services" ALTER COLUMN "services" SET NOT NULL;
        ALTER TABLE "services" ALTER COLUMN "services" TYPE text[] USING "services"::text[];"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "services" ALTER COLUMN "services" TYPE VARCHAR(126) USING "services"::VARCHAR(126);
        ALTER TABLE "services" ALTER COLUMN "services" DROP NOT NULL;"""
