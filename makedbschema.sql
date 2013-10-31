--Make a schema--
--All statements must be on one line--
--CREATE TABLE statements only. 

CREATE TABLE lab (reaction varchar not null, labn decimal(2,0) not null);
CREATE TABLE reaction (rname varchar not null, casn decimal(10,0) not null);
CREATE TABLE compound (cname varchar not null, casn decimal(10,0) not null, hazard char(4) not null);
CREATE TABLE inventory (amount decimal(7,0) not null, unit char (1) not null,  varchar cname not null, casn decimal(10,0) not null);
CREATE TABLE catalog (casn decimal(10,0) not null, csname varchar not null, price decimal(8,2) not null, amount decimal(10,2) not null, unit char(1) not null);
CREATE TABLE supplier (sname varchar not null, phonen decimal(11,0) not null, location varchar not null);

