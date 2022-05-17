-- upgrade --
CREATE TABLE IF NOT EXISTS "council_members" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "party" VARCHAR(100) NOT NULL,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "uid_council_mem_name_169c5f" UNIQUE ("name", "party")
);
CREATE INDEX IF NOT EXISTS "idx_council_mem_name_39f3ec" ON "council_members" ("name");
CREATE INDEX IF NOT EXISTS "idx_council_mem_party_5bfe90" ON "council_members" ("party");
CREATE INDEX IF NOT EXISTS "idx_council_mem_name_169c5f" ON "council_members" ("name", "party");
CREATE TABLE IF NOT EXISTS "meetings" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "date" DATE NOT NULL,
    "number" INT NOT NULL,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT "uid_meetings_date_a94b67" UNIQUE ("date", "number")
);
CREATE TABLE IF NOT EXISTS "agenda_items" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "gr_number" VARCHAR(10),
    "meeting_ordering" SMALLINT NOT NULL,
    "title" TEXT NOT NULL,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "meeting_id" INT NOT NULL REFERENCES "meetings" ("id") ON DELETE CASCADE,
    "parent_id" INT REFERENCES "agenda_items" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_agenda_item_meeting_e1f80e" UNIQUE ("meeting_id", "meeting_ordering")
);
CREATE INDEX IF NOT EXISTS "idx_agenda_item_gr_numb_7eb370" ON "agenda_items" ("gr_number");
CREATE INDEX IF NOT EXISTS "idx_agenda_item_gr_numb_b9e89c" ON "agenda_items" ("gr_number", "meeting_id", "title");
CREATE TABLE IF NOT EXISTS "speeches" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "item_ordering" SMALLINT NOT NULL,
    "mp3_url" TEXT NOT NULL,
    "mp3_path" TEXT,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "council_member_id" INT NOT NULL REFERENCES "council_members" ("id") ON DELETE CASCADE,
    "item_id" INT NOT NULL REFERENCES "agenda_items" ("id") ON DELETE CASCADE,
    CONSTRAINT "uid_speeches_item_id_a5e507" UNIQUE ("item_id", "item_ordering")
);
CREATE INDEX IF NOT EXISTS "idx_speeches_council_b8395e" ON "speeches" ("council_member_id", "item_id");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
