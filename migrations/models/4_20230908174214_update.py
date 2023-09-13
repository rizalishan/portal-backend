from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "portfolio" ALTER COLUMN "services" SET NOT NULL;
        ALTER TABLE "portfolio" ALTER COLUMN "services" TYPE text[] USING "services"::text[];
        ALTER TABLE "portfolio" ALTER COLUMN "images" SET NOT NULL;
        ALTER TABLE "portfolio" ALTER COLUMN "images" TYPE text[] USING "images"::text[];
        ALTER TABLE "portfolio" ALTER COLUMN "techologies" SET NOT NULL;
        ALTER TABLE "portfolio" ALTER COLUMN "techologies" TYPE text[] USING "techologies"::text[];
        CREATE TABLE IF NOT EXISTS "services" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "description" VARCHAR(126),
    "excerpt" VARCHAR(126),
    "services" VARCHAR(126),
    "icon" VARCHAR(126),
    "title" VARCHAR(126)
);
COMMENT ON TABLE "services" IS 'The Services Model';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "portfolio" ALTER COLUMN "services" TYPE VARCHAR(126) USING "services"::VARCHAR(126);
        ALTER TABLE "portfolio" ALTER COLUMN "services" DROP NOT NULL;
        ALTER TABLE "portfolio" ALTER COLUMN "images" TYPE VARCHAR(126) USING "images"::VARCHAR(126);
        ALTER TABLE "portfolio" ALTER COLUMN "images" DROP NOT NULL;
        ALTER TABLE "portfolio" ALTER COLUMN "techologies" TYPE VARCHAR(126) USING "techologies"::VARCHAR(126);
        ALTER TABLE "portfolio" ALTER COLUMN "techologies" DROP NOT NULL;
        DROP TABLE IF EXISTS "services";"""
