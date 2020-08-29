-- migrate:up
alter table metrics 
add column request_time decimal;

-- migrate:down

alter table metrics 
drop column request_time;

