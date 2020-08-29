-- migrate:up
alter table metrics 
add column error varchar;

-- migrate:down

alter table metrics 
drop column error;

