-- migrate:up
create table sites (
  id serial primary key,
  url varchar,
  regex varchar
);


-- migrate:down

drop table sites;

