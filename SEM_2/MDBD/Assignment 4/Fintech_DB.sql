-- FinTech Database SQL Script
-- This script creates and populates a database for a FinTech application

-- Drop database if it exists and create new one
DROP DATABASE IF EXISTS Fintech;
CREATE DATABASE Fintech;

-- Use the Fintech database
USE Fintech;

-- Create user and grant privileges
DROP USER IF EXISTS 'MDBD'@'localhost';
CREATE USER 'MDBD'@'localhost' IDENTIFIED BY 'Mdbd@123';
GRANT ALL PRIVILEGES ON Fintech.* TO 'MDBD'@'localhost';
FLUSH PRIVILEGES;

-- Create Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    date_of_birth DATE NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_email (email)
);

-- Create Accounts table
CREATE TABLE Accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    account_type ENUM('savings', 'checking', 'brokerage') NOT NULL,
    balance DECIMAL(15, 2) NOT NULL DEFAULT 0.00,
    currency VARCHAR(3) NOT NULL DEFAULT 'INR',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX idx_user_id (user_id),
    INDEX idx_account_type (account_type)
);

-- Create Transactions table
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_type ENUM('credit', 'debit') NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    description VARCHAR(255),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id),
    INDEX idx_account_id (account_id),
    INDEX idx_transaction_date (transaction_date)
);

-- Create Investments table
CREATE TABLE Investments (
    investment_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT NOT NULL,
    investment_type ENUM('stocks', 'bonds', 'mutual_funds', 'crypto') NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    current_value DECIMAL(15, 2),
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id),
    INDEX idx_account_id (account_id),
    INDEX idx_investment_type (investment_type)
);

-- Create Loans table
CREATE TABLE Loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    loan_amount DECIMAL(15, 2) NOT NULL,
    interest_rate DECIMAL(5, 2) NOT NULL,
    loan_term_months INT NOT NULL,
    loan_start_date DATE NOT NULL,
    loan_status ENUM('active', 'closed', 'defaulted') NOT NULL DEFAULT 'active',
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    INDEX idx_user_id (user_id),
    INDEX idx_loan_status (loan_status)
);