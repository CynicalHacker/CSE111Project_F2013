--This script fills a blank database initialzed according to the schema:

--CREATE TABLE lab (l_rname varchar not null, l_num decimal(2,0) not null, l_title varchar not null);
--CREATE TABLE reaction (r_rname varchar not null, r_casn decimal(10,0) not null);
--CREATE TABLE compound (c_cname varchar not null, c_casn decimal(10,0) not null, c_hazard char(4) not null);
--CREATE TABLE inventory (i_amount decimal(7,0) not null, i_unit char (1) not null,  varchar i_cname not null, i_casn decimal(10,0) not null);
--CREATE TABLE catalog (cat_casn decimal(10,0) not null, cat_sname varchar not null, cat_price decimal(8,2) not null, cat_amount decimal(10,2) not null, cat_unit char(1) not null);
--CREATE TABLE supplier (s_sname varchar not null, s_phonenum decimal(11,0) not null, s_location varchar not null);
--Each statement must be one line long in order for this to work with python.

--Lab
--CREATE TABLE lab (l_rname varchar not null, l_num decimal(2,0) not null, l_title varchar not null);

INSERT INTO lab VALUES ('Recrystallization','1', 'Recrystallization');
INSERT INTO lab VALUES ('Extraction', '3', 'Extraction');
INSERT INTO lab VALUES ('Distillation', '4', 'Distillation');
INSERT INTO lab VALUES ('Malonate formation', '6', 'Reflux');
INSERT INTO lab VALUES ('Bromination', '7', 'Bromination');
INSERT INTO lab VALUES ('E2', '11', 'Eliminations');
INSERT INTO lab VALUES ('E1', '11', 'Eliminations');
INSERT INTO lab VALUES ('Electrophillic Aromatic Substitution','12', 'Electrophillic Aromatic Substitution');

--Reactions
--CREATE TABLE reaction (r_rname varchar not null, r_casn decimal(10,0) not null);

INSERT INTO reaction VALUES ('Recrystallization', '121335');
INSERT INTO reaction VALUES ('Extraction', '50782');
INSERT INTO reaction VALUES ('Distillation', '108883');
INSERT INTO reaction VALUES ('Distillation', '106423');
INSERT INTO reaction VALUES ('Malonate formation', '118923');
INSERT INTO reaction VALUES ('Malonate formation', '108247');
INSERT INTO reaction VALUES ('Bromination', '7726956');
INSERT INTO reaction VALUES ('Bromination', '140103');
INSERT INTO reaction VALUES ('E2', '71238');
INSERT INTO reaction VALUES ('E2', '507368');
INSERT INTO reaction VALUES ('E1', '75854');
INSERT INTO reaction VALUES ('E1', '137326');
INSERT INTO reaction VALUES ('E1', '865474');
INSERT INTO reaction VALUES ('Electrophillic Aromatic Substitution', '103844');
INSERT INTO reaction VALUES ('Electrophillic Aromatic Substitution', '7726956');

--Compounds
--CREATE TABLE compound (c_cname varchar not null, c_casn decimal(10,0) not null, c_hazard char(4) not null);
--FLAM = flammable
--RADI = radioactive
--IRRT = potent irritant
--OXID = oxidizer
--POIS = poison(toxic)
--CRSV = corrosive
--EXPL = explosive
--MISC = miscellaneous
--NONE = no hazard

INSERT INTO compound VALUES ('vanillin', '121335', 'NONE');
INSERT INTO compound VALUES ('aspirin', '50782', 'MISC'); 
INSERT INTO compound VALUES ('toluene', '108883', 'FLAM');
INSERT INTO compound VALUES ('p-xylene', '106423', 'FLAM');
INSERT INTO compound VALUES ('anthranilic acid', '118923', 'POIS');
INSERT INTO compound VALUES ('acetic anhydride', '108247', 'IRRT');
INSERT INTO compound VALUES ('trans-cinnamic acid', '140103', 'IRRT');
INSERT INTO compound VALUES ('bromine', '7726956', 'POIS');
INSERT INTO compound VALUES ('1-propanol', '71238', 'FLAM');
INSERT INTO compound VALUES ('2-bromo-2-methylbutane', '507368', 'FLAM');
INSERT INTO compound VALUES ('potassium tert-butoxide', '865474', 'CRSV');
INSERT INTO compound VALUES ('tert-amyl alcohol', '75854', 'FLAM');
INSERT INTO compound VALUES ('2-methyl-1-butanol', '137326', 'FLAM');
INSERT INTO compound VALUES ('acetanilide', '103844', 'POIS');
INSERT INTO compound VALUES ('radium', '7440144', 'RADI');
INSERT INTO compound VALUES ('trinitrotoluene', '118967', 'EXPL');

--Inventory
--CREATE TABLE inventory (i_amount decimal(7,0) not null, i_unit char (1) not null,  varchar i_cname not null, i_casn decimal(10,0) not null);
--Our lab director is a little weird and is only buying exotic compounds at the moment...

INSERT INTO inventory VALUES ('200', 'g', 'aspirin', '50782');
INSERT INTO inventory VALUES ('100', 'g', 'bromine', '7726956');
INSERT INTO inventory VALUES ('2000', 'g', 'radium', '7440144');
INSERT INTO inventory VALUES ('999999999999', 'g', 'trinitrotoluene', '118967');
INSERT INTO inventory VALUES ('300', 'g', 'vanillin', '121335');

--Supplier
--CREATE TABLE supplier (s_sname varchar not null, s_phonenum decimal(11,0) not null, s_location varchar not null)

INSERT INTO supplier VALUES ('Sigma-Aldrich', '18003253010', 'Ireland');
INSERT INTO supplier VALUES ('Thermo Fisher Scientific', '18007667000', 'America');
INSERT INTO supplier VALUES ('Spectrum Chemicals', '18007728786', 'Canada');

--Catalogs!
--CREATE TABLE catalog (cat_casn decimal(10,0) not null, cat_sname varchar not null, cat_price decimal(8,2) not null, cat_amount decimal(10,2) not null, cat_unit char(1) not null);

INSERT INTO catalog VALUES ('118967', 'Sigma-Aldrich', '1000.99', 20, 'g');
INSERT INTO catalog VALUES ('50782', 'Thermo Fisher Scientific', '25.00', 50, 'g');
INSERT INTO catalog VALUES ('7440144', 'Spectrum Chemicals', '2000.00', 0.1, 'g');
INSERT INTO catalog VALUES ('71238', 'Sigma-Aldrich', '200.00', 1, 'L');
INSERT INTO catalog VALUES ('7726956', 'Spectrum Chemicals', '1234.56', '9001' , 'L');

