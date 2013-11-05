--Make a schema--
--All statements must be on one line--
--CREATE TABLE statements only. 

CREATE TABLE lab (l_rname varchar not null, l_num decimal(2,0) not null, l_title varchar not null);
CREATE TABLE reaction (r_rname varchar not null, r_casn decimal(10,0) not null);
CREATE TABLE compound (c_cname varchar not null, c_casn decimal(10,0) not null, c_hazard char(4) not null);
CREATE TABLE inventory (i_amount decimal(7,0) not null, i_unit char (1) not null,  varchar i_cname not null, i_casn decimal(10,0) not null);
CREATE TABLE catalog (cat_casn decimal(10,0) not null, cat_sname varchar not null, cat_price decimal(8,2) not null, cat_amount decimal(10,2) not null, cat_unit char(1) not null);
CREATE TABLE supplier (s_sname varchar not null, s_phonenum decimal(11,0) not null, s_location varchar not null);

