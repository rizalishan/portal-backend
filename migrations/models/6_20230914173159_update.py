from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "candidates" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(255) NOT NULL,
    "cv" VARCHAR(255) NOT NULL,
    "created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "candidates" IS 'The Candidate Model';
        CREATE TABLE IF NOT EXISTS "examinations" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "type" VARCHAR(255) NOT NULL,
    "title" VARCHAR(255) NOT NULL,
    "difficulty" DOUBLE PRECISION NOT NULL,
    "created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "examinations" IS 'The Examination Model';
        CREATE TABLE IF NOT EXISTS "assessments" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "total_score" DOUBLE PRECISION NOT NULL,
    "total_score_without_negative" DOUBLE PRECISION NOT NULL  DEFAULT 0,
    "created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "candidate_id" INT NOT NULL REFERENCES "candidates" ("id") ON DELETE CASCADE,
    "examination_id" INT NOT NULL REFERENCES "examinations" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "assessments" IS 'The Assessment Model';
        CREATE TABLE IF NOT EXISTS "questions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "question" TEXT NOT NULL,
    "correct_answer" VARCHAR(255) NOT NULL,
    "type" VARCHAR(255) NOT NULL,
    "score" DOUBLE PRECISION NOT NULL,
    "options" JSONB,
    "code" TEXT,
    "created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "examination_id" INT NOT NULL REFERENCES "examinations" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "questions" IS 'The Question Model';
        CREATE TABLE IF NOT EXISTS "assessment_questions" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "answer" TEXT NOT NULL,
    "score" DOUBLE PRECISION NOT NULL,
    "created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "assessment_id" INT NOT NULL REFERENCES "assessments" ("id") ON DELETE CASCADE,
    "question_id_id" INT REFERENCES "questions" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "assessment_questions" IS 'The Assessment Questions Model';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "candidates";
        DROP TABLE IF EXISTS "examinations";
        DROP TABLE IF EXISTS "assessments";
        DROP TABLE IF EXISTS "questions";
        DROP TABLE IF EXISTS "assessment_questions";"""
