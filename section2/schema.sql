CREATE TABLE IF NOT EXISTS members (
  members_id VARCHAR(255) PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  date_of_birth DATE NOT NULL,
  above_18 BOOLEAN NOT NULL,
  email VARCHAR(50) UNIQUE NOT NULL,
  mobile_no VARCHAR(8) not null
);

CREATE TABLE IF NOT EXISTS items (
  item_id SERIAL PRIMARY KEY,
  item_name VARCHAR(255) NOT NULL,
  manufacturer_name VARCHAR(255) NOT NULL,
  cost DECIMAL(10,2) NOT NULL,
  weight DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
  transaction_id SERIAL PRIMARY KEY,
  member_id INTEGER NOT NULL REFERENCES members(id),
  item_id INTEGER NOT NULL REFERENCES items(id),
  quantity INTEGER NOT NULL,
  total_price DECIMAL(10,2) NOT NULL,
  total_weight DECIMAL(10,2) NOT NULL,
  transaction_date TIMESTAMP DEFAULT NOW()
);