CREATE TABLE IF NOT EXISTS server (
    id INTEGER PRIMARY KEY,
    name TEXT,
    host TEXT,
    username TEXT,
    password TEXT,
    private_key TEXT
);

CREATE TABLE IF NOT EXISTS deploy (
    id INTEGER PRIMARY KEY,
    name TEXT,
    server_id INTEGER,
    command_origin TEXT,
    path_origin TEXT,
    path_destiny TEXT,
    command_destiny TEXT
);

CREATE TABLE IF NOT EXISTS script_manager (
    id INTEGER PRIMARY KEY,
    name TEXT,
    server_id INTEGER,
    script_text TEXT
);

CREATE TABLE IF NOT EXISTS database (
    id INTEGER PRIMARY KEY,
    description TEXT,
    database TEXT,
    host TEXT,
    username TEXT,
    password TEXT,
    port INTEGER
)