"""Learning exercise: a simulated withdrawal from a fixed sample balance."""

import math

balance = 500.00

try:
    amount = float(input("Enter a withdrawal amount (R): "))
except ValueError:
    print("Please enter a number.")
else:
    if not math.isfinite(amount) or amount <= 0:
        print("Enter a positive, finite amount.")
    elif amount > balance:
        print("Declined: insufficient simulated funds.")
    else:
        balance -= amount
        print(f"Withdrawal accepted. Simulated balance: R{balance:.2f}")
