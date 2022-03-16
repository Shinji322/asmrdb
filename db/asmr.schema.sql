-- For each asmrtist
CREATE TABLE asmrtist (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    platform TEXT, -- The platform this file is from (i.e. YouTube, Reddit, etc.)
    primary_audience TEXT, -- The user's primary audience (may be useful for archivists)

    nsfw BOOLEAN DEFAULT FALSE, -- Used for filtering purposes
    favorite BOOLEAN DEFAULT FALSE, -- if this artist is a favorite

    gender TEXT DEFAULT "N/A", -- again used for filtration purposes
    description TEXT, -- an optional description about this user

    first_archive_date DATE, -- The date this asmrtist was first added to the db
    last_archive_date DATE -- The last date information about this user was added to db
);

-- Each audio
CREATE TABLE audios (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    asmrtist_id INTEGER, 
    tags TEXT, -- Used for filtration purposes
    title TEXT, -- The name of the audio
    audience TEXT, -- Certain ASMR is designed for specific audiences
    variant TEXT, -- Roleplay | White Noise etc. 

    source TEXT, -- url where the data came from
    nsfw BOOLEAN DEFAULT FALSE, -- Used for filtration purposes
    description TEXT, -- An optional description 

    date_created DATE, -- The date this file was created (from external site)
    date_downloaded DATE, -- The date this file was archived by user

    times_viewed TINYINT DEFAULT 0, -- Bookeeping value
    favorite BOOLEAN DEFAULT FALSE, -- If the audio is a favorite

    FOREIGN KEY(asmrtist_id) REFERENCES asmrtist(id)
);

-- A bookeeping value for the current user
-- CREATE TABLE user (
--     id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
--     date_joined DATE -- date you started archiving. I'm sentimental
-- );
