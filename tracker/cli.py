import argparse
from tracker.service import add_expense, list_expenses, summary

def main():
    """
    Entry point for the Expense Tracker CLI.

    This function:
    - Defines all CLI commands and arguments
    - Parses user input
    - Calls the appropriate service-layer function
    - Prints formatted results to stdout

    Commands:
    - add:
        Adds a new expense record.
    - list:
        Lists existing expenses with optional filters.
    - summary:
        Displays aggregated expense data for a given month.

    Any unhandled exception is caught and displayed as a clean
    error message without a stack trace.
    """
    parser = argparse.ArgumentParser(prog="tracker")
    sub = parser.add_subparsers(dest="command")

    # ADD
    add = sub.add_parser("add")
    add.add_argument("--date")
    add.add_argument("--category", required=True)
    add.add_argument("--amount", type=float, required=True)
    add.add_argument("--note", default="")
    add.add_argument("--currency", default="BDT")

    # LIST
    lst = sub.add_parser("list")
    lst.add_argument("--month")
    lst.add_argument("--category")
    lst.add_argument("--min", type=float)
    lst.add_argument("--max", type=float)
    lst.add_argument("--sort")
    lst.add_argument("--desc", action="store_true")
    lst.add_argument("--limit", type=int)

    # SUMMARY
    summ = sub.add_parser("summary")
    summ.add_argument("--month")

    args = parser.parse_args()

    try:
        if args.command == "add":
            exp = add_expense(
                date=args.date,
                category=args.category,
                amount=args.amount,
                note=args.note,
                currency=args.currency,
            )
            print(
                f"Added: {exp.id} | {exp.date} | {exp.category} | "
                f"{exp.amount:.2f} {exp.currency} | {exp.note}"
            )

        elif args.command == "list":
            filters = vars(args)
            expenses = list_expenses(filters)

            if not expenses:
                print("No expenses found")
                return

            for e in expenses:
                print(
                    f"{e['id']} | {e['date']} | {e['category']} | "
                    f"{e['amount']:.2f} {e['currency']} | {e['note']}"
                )

        elif args.command == "summary":
            result = summary({"month": args.month})
            if not result:
                print("No expenses found")
                return

            print(f"Total expenses: {result['count']}")
            print(f"Grand total: {result['grand_total']:.2f} BDT")
            print("By category:")
            for cat, amt in result["by_category"].items():
                print(f"  {cat}: {amt:.2f} BDT")

        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")
