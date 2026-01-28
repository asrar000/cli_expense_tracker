from tracker.models import Expense
from tracker.storage import load_data, save_data
from tracker.utils import validate_date, today_date, now_iso
from tracker.logger import setup_logger

logger = setup_logger()


def generate_id(expenses):
    """
    Generate a unique expense ID based on the current date and
    number of existing expenses.

    ID format:
        EXP-YYYYMMDD-XXXX

    Args:
        expenses (list): List of existing expense records.

    Returns:
        str: A unique expense identifier.
    """
    count = len(expenses) + 1
    date_part = today_date().replace("-", "")
    return f"EXP-{date_part}-{count:04d}"


def add_expense(category, amount, date=None, note="", currency="BDT"):
    """
    Create and store a new expense.

    This function validates input, generates a unique ID,
    persists the expense to storage, and logs the operation.

    Args:
        category (str): Expense category (e.g. food, transport).
        amount (float): Expense amount (must be greater than 0).
        date (str, optional): Expense date in YYYY-MM-DD format.
                              Defaults to today's date.
        note (str, optional): Optional note or description.
        currency (str, optional): Currency code. Defaults to "BDT".

    Raises:
        ValueError: If amount is less than or equal to zero.
        ValueError: If date format is invalid.

    Returns:
        Expense: The created Expense object.
    """
    if amount <= 0:
        raise ValueError("amount must be > 0")

    date = validate_date(date or today_date())
    category = category.lower()

    data = load_data()
    expense_id = generate_id(data["expenses"])

    expense = Expense(
        id=expense_id,
        date=date,
        category=category,
        amount=amount,
        currency=currency,
        note=note,
        created_at=now_iso()
    )

    data["expenses"].append(expense.__dict__)
    save_data(data)

    logger.info(f"ADD {expense_id}")
    return expense


def list_expenses(filters):
    """
    Retrieve expenses using filtering, sorting, and limiting options.

    Supported filters:
        - month (YYYY-MM)
        - category
        - min (minimum amount)
        - max (maximum amount)
        - sort (field name)
        - desc (descending order)
        - limit (maximum number of results)

    Args:
        filters (dict): Dictionary containing filter options.

    Returns:
        list: List of expense dictionaries matching the filters.
    """
    data = load_data()
    expenses = data["expenses"]

    if not expenses:
        return []

    if filters.get("month"):
        expenses = [e for e in expenses if e["date"].startswith(filters["month"])]

    if filters.get("category"):
        expenses = [e for e in expenses if e["category"] == filters["category"]]

    if filters.get("min") is not None:
        expenses = [e for e in expenses if e["amount"] >= filters["min"]]

    if filters.get("max") is not None:
        expenses = [e for e in expenses if e["amount"] <= filters["max"]]

    if filters.get("sort"):
        reverse = filters.get("desc", False)
        expenses = sorted(
            expenses,
            key=lambda x: x[filters["sort"]],
            reverse=reverse
        )

    if filters.get("limit"):
        expenses = expenses[:filters["limit"]]

    return expenses


def summary(filters):
    """
    Generate a summary of expenses.

    The summary includes:
        - Total number of expenses
        - Grand total amount
        - Total amount grouped by category

    Args:
        filters (dict): Dictionary of filter options (e.g. month).

    Returns:
        dict | None: Summary dictionary or None if no expenses exist.
    """
    expenses = list_expenses(filters)

    if not expenses:
        return None

    total = sum(e["amount"] for e in expenses)
    by_category = {}

    for e in expenses:
        by_category.setdefault(e["category"], 0)
        by_category[e["category"]] += e["amount"]

    return {
        "count": len(expenses),
        "grand_total": total,
        "by_category": by_category
    }
