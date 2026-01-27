from dataclasses import dataclass

@dataclass
class Expense:
    id: str
    date: str
    category: str
    amount: float
    currency: str
    note: str
    created_at: str
