-- Ensure indexes exist on foreign key relationships for faster joins
CREATE INDEX idx_accounts_user_id ON Accounts(user_id);

-- Optional: Index on balance if filtering based on balance ranges frequently
CREATE INDEX idx_balance ON Accounts(balance);

-- Email index already exists on Users for quick lookup
-- But if sorting/filtering by name or email often, you may add:
CREATE INDEX idx_users_name_email ON Users(first_name, last_name, email);

-- Users Table
CREATE INDEX idx_email ON Users(email);

-- Accounts Table
CREATE INDEX idx_account_type ON Accounts(account_type);

-- Transactions Table
CREATE INDEX idx_account_id_transactions ON Transactions(account_id);
CREATE INDEX idx_transaction_date ON Transactions(transaction_date);

-- Investments Table
CREATE INDEX idx_account_id_investments ON Investments(account_id);
CREATE INDEX idx_investment_type ON Investments(investment_type);

-- Loans Table
CREATE INDEX idx_user_id_loans ON Loans(user_id);
CREATE INDEX idx_loan_status ON Loans(loan_status);