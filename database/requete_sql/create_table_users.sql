CREATE TABLE client_table (
	client_ID INTEGER PRIMARY KEY AUTOINCREMENT,
   	client_username CHAR NOT NULL,
	client_password CHAR NOT NULL,
	client_capital INTEGER DEFAULT 0,
	client_is_admin BIT DEFAULT 0,
	client_name CHAR NOT NULL,
	client_surname CHAR NOT NULL,
	client_creation_date_account DATE);
