-- Query to Find High-Value Clients (combined balance across all accounts exceeds Rs. 100,000)
SELECT 
    u.user_id,
    CONCAT(u.first_name, ' ', u.last_name) AS full_name,
    u.email,
    SUM(a.balance) AS total_balance
FROM 
    Users u
JOIN 
    Accounts a ON u.user_id = a.user_id
GROUP BY 
    u.user_id, u.first_name, u.last_name, u.email
HAVING 
    total_balance > 100000
ORDER BY 
    total_balance DESC;