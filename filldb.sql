--This script fills a blank database initialzed according to the schema:

--CREATE TABLE lab (reactions varchar not null, labn decimal(2,0) not null);
--CREATE TABLE reaction (r_name varchar not null, casn decimal(10,0));
--CREATE TABLE compound (casn decimal(10,0) not null, cname varchar not null, hazoard char(4) not null);
--CREATE TABLE inventory (amount decimal(7,0) not null, units char (1) not null,  varchar name not null, casn decimal(10,0) not null,);
--CREATE TABLE catalog (casn decimal(10,0) not null, csname varchar not null, price decimal(8,2) not null, amount decimal(10,2) not null, units char(1) not null);
--CREATE TABLE supplier (sname varchar not null, phonen decimal(11,0) not null, location varchar not null);

--Each statement must be one line long in order for this to work with python.

--Lab
--CREATE TABLE lab (reactions varchar not null, labn decimal(2,0) not null);

INSERT INTO lab VALUES ('Recrystallization','1');
INSERT INTO lab VALUES ('Extraction', '3');
INSERT INTO lab VALUES ('Distillation', '4');
INSERT INTO lab VALUES ('Malonate formation', '6');
INSERT INTO lab VALUES ('Bromination', '7');
INSERT INTO lab VALUES ('E2', '11');
INSERT INTO lab VALUES ('E1', '11');
INSERT INTO lab VALUES ('Electrophillic Aromatic Substitution','12');

--Reactions
--CREATE TABLE reaction (r_name varchar not null, casn decimal(10,0));

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
--CREATE TABLE compound (cname varchar not null, casn decimal(10,0) not null, hazard char(4) not null);
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
--CREATE TABLE inventory (amount decimal(7,0) not null, units char (1) not null,  varchar name not null, casn decimal(10,0) not null,);
--Our lab director is a little weird and is only buying exotic compounds at the moment...

INSERT INTO inventory VALUES ('200', 'g', 'aspirin', '50782');
INSERT INTO inventory VALUES ('100', 'g', 'bromine', '7726956');
INSERT INTO inventory VALUES ('2000', 'g', 'radium', '7440144');
INSERT INTO inventory VALUES ('999999999999', 'g', 'trinitrotoluene', '118967');
INSERT INTO inventory VALUES ('300', 'g', 'vanillin', '121335');

--Supplier
--CREATE TABLE supplier (sname varchar not null, phonen decimal(11,0) not null, location varchar not null);

INSERT INTO supplier VALUES ('Sigma-Aldrich', '18003253010', 'Ireland');
INSERT INTO supplier VALUES ('Thermo Fisher Scientific', '18007667000', 'America');
INSERT INTO supplier VALUES ('Spectrum Chemicals', '18007728786', 'Canada');

--Catalogs!
--CREATE TABLE catalog (casn decimal(10,0) not null, csname varchar not null, price decimal(8,2) not null, amount decimal(10,2) not null, units char(1) not null);

INSERT INTO catalog VALUES ('118967', 'Sigma-Aldrich', '1000.99', 20, 'g');




