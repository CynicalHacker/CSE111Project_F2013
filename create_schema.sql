CREATE TABLE lab (reactions varchar not null, labn decimal(2,0) not null);
CREATE TABLE reaction (r_name varchar not null, casn decimal(10,0) not null);
CREATE TABLE compound (casn decimal(10,0) not null, cname varchar not null, hazard char(4) not null);
CREATE TABLE inventory (amount decimal(7,0) not null, units char (1) not null, casn decimal(10,0) not null);
CREATE TABLE catalog (casn decimal(10,0) not null, csname varchar not null, price decimal(8,2) not null, amount decimal(10,2) not null, units char(1) not null);
CREATE TABLE supplier (sname varchar not null, phonen decimal(10,0) not null, warehouse varchar not null);

