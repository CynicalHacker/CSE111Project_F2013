SELECT * FROM inventory
UPDATE inventory SET i_amount=? WHERE i_casn=?
SELECT * FROM inventory WHERE i_cname = ?
SELECT DISTINCT c_cname,c_hazard FROM compound WHERE c_casn = ?
SELECT l_title, l_num FROM lab WHERE l_rname=?
SELECT * FROM compound WHERE c_casn = ?
SELECT * FROM compound WHERE c_cname = ?
SELECT DISTINCT l_rname FROM lab WHERE l_num=(?)
SELECT DISTINCT c_cname,c_casn,c_hazard FROM compound, reaction WHERE c_casn = r_casn AND r_rname = ?
SELECT DISTINCT l_title,l_num FROM lab WHERE l_rname=?
SELECT r_casn FROM reaction WHERE r_rname=(?)
SELECT DISTINCT r_rname FROM reaction WHERE r_casn = ?
SELECT * FROM inventory WHERE i_casn = ?
SELECT DISTINCT l_title FROM lab WHERE l_num=(?)
