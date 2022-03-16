CREATE TABLE performer (
	id INTEGER NOT NULL, 
	username VARCHAR NOT NULL, 
	platform VARCHAR, 
	primary_audience VARCHAR, 
	primary_language VARCHAR, 
	favorite BOOLEAN, 
	gender VARCHAR, 
	description VARCHAR, 
	first_archive_date DATETIME, 
	last_archive_date DATETIME, 
	PRIMARY KEY (id)
);
CREATE TABLE audio (
	id INTEGER NOT NULL, 
	asmrtist_id INTEGER, 
	tags VARCHAR, 
	title VARCHAR, 
	performer_gender VARCHAR, 
	audience VARCHAR, 
	variant VARCHAR, 
	source VARCHAR, 
	description VARCHAR, 
	date_created DATETIME, 
	date_downloaded DATETIME, 
	times_viewed INTEGER, 
	favorite BOOLEAN, 
	path VARCHAR, 
	img_path VARCHAR, 
	language VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(asmrtist_id) REFERENCES performer (id)
);
