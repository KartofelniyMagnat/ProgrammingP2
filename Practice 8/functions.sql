-- ─── FUNCTION 1: Search by pattern ──────────────────────────────────────────
-- Returns all contacts where name or phone matches the given pattern.

CREATE OR REPLACE FUNCTION search_contacts(p_pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT pb.id, pb.first_name, pb.phone
        FROM phonebook pb
        WHERE pb.first_name ILIKE '%' || p_pattern || '%'
           OR pb.phone      ILIKE '%' || p_pattern || '%'
        ORDER BY pb.id;
END;
$$ LANGUAGE plpgsql;

-- Usage: SELECT * FROM search_contacts('Ali');


-- ─── FUNCTION 2: Paginated query ─────────────────────────────────────────────
-- Returns contacts page by page using LIMIT / OFFSET.

CREATE OR REPLACE FUNCTION get_contacts_page(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
        SELECT pb.id, pb.first_name, pb.phone
        FROM phonebook pb
        ORDER BY pb.id
        LIMIT  p_limit
        OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- Usage: SELECT * FROM get_contacts_page(10, 0);   -- page 1
--        SELECT * FROM get_contacts_page(10, 10);  -- page 2
