-- ─── PROCEDURE 1: Upsert single contact ──────────────────────────────────────
-- Inserts a new contact; updates phone if the name already exists.

CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE first_name = p_name;
    ELSE
        INSERT INTO phonebook(first_name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- Usage: CALL upsert_contact('Alice', '+77001112233');


-- ─── PROCEDURE 2: Bulk insert with phone validation ───────────────────────────
-- Accepts arrays of names and phones, validates each phone (digits / + / - / spaces,
-- length 7-15), upserts valid rows, and returns invalid entries via a temp table.
--
-- After calling, retrieve bad rows with:
--   SELECT * FROM bulk_insert_errors;

CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names  VARCHAR[],
    p_phones VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i       INT;
    v_name  VARCHAR;
    v_phone VARCHAR;
BEGIN
    -- Temp table holds rows that failed validation (lives for this session).
    CREATE TEMP TABLE IF NOT EXISTS bulk_insert_errors (
        first_name VARCHAR,
        phone      VARCHAR,
        reason     TEXT
    ) ON COMMIT DELETE ROWS;

    -- Clear previous errors.
    DELETE FROM bulk_insert_errors;

    IF array_length(p_names, 1) IS NULL THEN
        RETURN;
    END IF;

    FOR i IN 1 .. array_length(p_names, 1) LOOP
        v_name  := TRIM(p_names[i]);
        v_phone := TRIM(p_phones[i]);

        -- Validate: only digits, +, -, spaces; total 7-15 chars.
        IF v_phone !~ '^\+?[\d\s\-]{7,15}$' THEN
            INSERT INTO bulk_insert_errors VALUES (v_name, v_phone, 'invalid phone format');
        ELSE
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = v_name) THEN
                UPDATE phonebook SET phone = v_phone WHERE first_name = v_name;
            ELSE
                INSERT INTO phonebook(first_name, phone) VALUES (v_name, v_phone);
            END IF;
        END IF;
    END LOOP;
END;
$$;

-- Usage:
--   CALL insert_many_contacts(
--       ARRAY['Bob', 'Eve', 'Bad'],
--       ARRAY['+77771234567', '87001112233', 'not-a-phone']
--   );
--   SELECT * FROM bulk_insert_errors;


-- ─── PROCEDURE 3: Delete by username or phone ─────────────────────────────────
-- Pass a non-empty value for whichever field you want to match.
-- Passing NULL skips that criterion.

CREATE OR REPLACE PROCEDURE delete_contact(
    p_name  VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL AND p_name <> '' THEN
        DELETE FROM phonebook WHERE first_name = p_name;
    END IF;

    IF p_phone IS NOT NULL AND p_phone <> '' THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    END IF;
END;
$$;

-- Usage:
--   CALL delete_contact(p_name  := 'Alice');
--   CALL delete_contact(p_phone := '+77001112233');
--   CALL delete_contact('Bob', '+77771234567');
