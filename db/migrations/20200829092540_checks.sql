-- migrate:up
create table metrics (
    id serial,
    site_id integer,
    status_code integer,
    constraint fk_site
        foreign key(site_id) 
            references sites(id)
                on delete cascade
);


-- migrate:down

drop table metrics;

