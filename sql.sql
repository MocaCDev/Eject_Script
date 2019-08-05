CREATE TABLE database (
  ID INTEGER PRIMARY KEY,
  USERSNAME TEXT NOT NULL UNIQUE,
  LINKED_ACCOUNTS TEXT NOT NULL UNIQUE
);

INSERT INTO database (ID,USERSNAME,LINKED_ACCOUNTS)
VALUES (1,'ARACADERISE','NONE');

-- ADDING PRIMARY USER WEBPAGE LINK
ALTER TABLE database
ADD COLUMN webpage TEXT DEFAULT 'None';

-- We want to update a value
UPDATE database
set webpage = 'https://'
where wepage = 'None';

SELECT DISTINCT *
FROM database;
