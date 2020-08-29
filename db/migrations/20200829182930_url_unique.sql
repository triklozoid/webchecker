-- migrate:up
ALTER TABLE sites
ADD CONSTRAINT url_unique UNIQUE (url);


-- migrate:down

ALTER TABLE sites
DROP CONSTRAINT url_unique;
