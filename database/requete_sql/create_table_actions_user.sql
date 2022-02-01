CREATE TABLE action_users_table (
	action_users_ID INTEGER PRIMARY KEY AUTOINCREMENT,
   	action_users_client_username CHAR NOT NULL,
   	action_users_date DATE,
   	action_users_choice CHAR NOT NULL,
	action_users_quantity INTEGER DEFAULT 0,
	action_users_total_value_transaction INTEGER DEFAULT 0,
	action_users_multiple_buy INTEGER DEFAULT 0,
	action_users_ticker CHAR NOT NULL,
	action_users_last_close INTEGER DEFAULT 0
	);
