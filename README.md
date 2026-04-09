# 🏦 Simple Bank Account Management App

A Python practice project built to refresh and solidify intermediate Python skills.
This is a **public repository** — feel free to fork it, build on it, or use it as a starting point for your own version.

---

## 📌 About the Project

This is an **intermediate-level Python practice project** simulating a basic bank account management system.
It is not production software — the goal is clean, readable Python code that covers real concepts like
file I/O, data handling, authentication logic, and simple data visualization.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Pandas** — data handling and display
- **Seaborn / Matplotlib** — balance visualization
- **Hashlib** — password hashing (built-in)
- **Pathlib / OS** — file and directory management (built-in)
- **CSV files** — lightweight data storage (no database needed)

---

## 📁 Project Structure

Simple-Bank-Account-Management-App/
│
├── main.py
├── auth.py
├── account.py
├── storage.py
├── visualize.py
│
└── data/
    ├── registry.csv
    └── accounts/
        └── <account_id>.csv

---

## 🐍 File Breakdown

### `main.py`
The entry point of the application. Runs the CLI menu loop and routes the user to the correct
operation based on their input. Handles the overall flow between login, registration, and account actions.

### `auth.py`
Handles all authentication logic. This includes registering a new user with a name and password,
checking the registry for duplicate accounts, generating a random unique account ID, hashing passwords
with SHA-256 via `hashlib`, and verifying credentials on login.

### `account.py`
Contains the core banking operations. This covers depositing and withdrawing funds (positive and negative
balance updates), changing the account holder's name, and displaying the full transaction history
as a formatted Pandas DataFrame. Each transaction is appended as a new row with a recalculated running balance.
Loads a user's transaction history and plots the balance over time as a Seaborn line chart.
Gives a quick visual overview of how the account balance has changed across transactions.

### `storage.py`
A helper module responsible for all CSV read and write operations. Keeps file I/O logic in one place
so the other modules stay clean. Manages both the shared `registry.csv` and the individual
per-account CSV files stored under `data/accounts/`.
---

## 📂 Data Storage

### `data/registry.csv`
Stores all registered users. Contains three columns:

| name | account_id | password_hash |
|------|------------|---------------|

### `data/accounts/<account_id>.csv`
One file per account, named after the randomly generated account ID. Contains four columns:

| date | description | amount | balance |
|------|-------------|--------|---------|

---

## 👤 Author

Made by **[Your Name]** as an intermediate Python practice project.