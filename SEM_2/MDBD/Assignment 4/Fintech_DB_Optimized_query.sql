-- Get Total Balance by Account Type for a User

SELECT 
    account_type, 
    SUM(balance) AS total_balance
FROM 
    Accounts USE INDEX (idx_accounts_user_id, idx_account_type)
WHERE 
    user_id = 1
GROUP BY 
    account_type;

-- Get Recent Transactions for an Account (Last 30 Days)

SELECT 
    t.transaction_id, t.amount, t.transaction_type, t.transaction_date
FROM 
    Transactions t USE INDEX (idx_account_id_transactions, idx_transaction_date)
WHERE 
    t.account_id = 1
    AND t.transaction_date >= CURDATE() - INTERVAL 30 DAY
ORDER BY 
    t.transaction_date DESC;

-- Filter Investments by Type for an Account

SELECT 
    investment_type, amount, current_value, purchase_date
FROM 
    Investments USE INDEX (idx_account_id_investments, idx_investment_type)
WHERE 
    account_id = 13
    AND investment_type = 'stocks';


-- Retrieve All Active Loans for a User

SELECT 
    loan_amount, interest_rate, loan_term_months, loan_start_date
FROM 
    Loans USE INDEX (idx_user_id_loans, idx_loan_status)
WHERE 
    user_id = 5
    AND loan_status = 'active';


-- Search Users by Partial Name and Email (e.g. for Admin Dashboard)

SELECT 
    user_id, first_name, last_name, email
FROM 
    Users USE INDEX (idx_users_name_email)
WHERE 
    first_name LIKE 'S%'
    AND email LIKE '%example.com';


-- Accounts with High Balances (e.g. for priority banking)

SELECT 
    account_id, user_id, account_type, balance
FROM 
    Accounts USE INDEX (idx_balance)
WHERE 
    balance > 100000
ORDER BY 
    balance DESC;
