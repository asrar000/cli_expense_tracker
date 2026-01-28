# 🧾 Expense Tracker CLI

A **Python 3 command-line expense tracker** with persistent storage, filtering, summaries, and logging.  
Designed with a clean, modular architecture similar to real-world backend tools.

---

## ✨ Features

- ➕ Add expenses with validation
- 📋 List expenses with filters and sorting
- 📊 Monthly summary with totals by category
- 💾 Persistent storage using JSON
- 🪵 Logging to file
- 🧪 Graceful handling of invalid input and corrupted files
- 🧱 Layered design (CLI → Service → Storage)

---

## 📁 Project Structure

```text
.
├── tracker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── service.py
│   ├── storage.py
│   ├── models.py
│   ├── utils.py
│   └── logger.py
├── data/
│   └── expenses.json
├── logs/
│   └── tracker.log
└── README.md

## 🛠 Requirements

- Python **3.9+**
- No external dependencies

Check version:

```bash
python3 --version
🚀 Running the CLI
From the project root:

python3 -m tracker
➕ Add an Expense
python3 -m tracker add \
  --date 2026-01-26 \
  --category food \
  --amount 250.5 \
  --note "Lunch"
Arguments
Argument	Required	Description
--date	❌	YYYY-MM-DD (default: today)
--category	✅	Expense category
--amount	✅	Positive number
--note	❌	Optional note
--currency	❌	Default: BDT
Output
Added: EXP-20260126-0001 | 2026-01-26 | food | 250.50 BDT | Lunch
📋 List Expenses
List all:

python3 -m tracker list
Filter by month:

python3 -m tracker list --month 2026-01
Filter by category:

python3 -m tracker list --category food
Filter by amount range:

python3 -m tracker list --min 100 --max 1000
Sort by amount (descending):

python3 -m tracker list --sort amount --desc
Limit results:

python3 -m tracker list --limit 20
📊 Summary
python3 -m tracker summary --month 2026-01
Example output:

Total expenses: 3
Grand total: 1210.50 BDT
By category:
  food: 650.50 BDT
  transport: 160.00 BDT
  rent: 400.00 BDT
🪵 Logging
Log file: logs/tracker.log

Logs:

Commands executed

Validation failures

File read/write errors

Example:

2026-01-27 12:30:01 | INFO | ADD EXP-20260126-0001
🧪 Validation Rules
Invalid date → date must be YYYY-MM-DD

Amount ≤ 0 → amount must be > 0

Missing required arguments → argparse error

Corrupted data file → clean error message (no stack trace)

🧪 Quick Manual Test
python3 -m tracker add --date 2026-01-25 --category transport --amount 80 --note "Rickshaw"
python3 -m tracker add --date 2026-01-26 --category food --amount 250.5 --note "Lunch"
python3 -m tracker add --date 2026-01-26 --category rent --amount 400 --note "Room rent"

python3 -m tracker list
python3 -m tracker list --month 2026-01 --sort amount --desc
python3 -m tracker summary --month 2026-01