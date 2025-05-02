
try:
    # Attempt to withdraw cash
    withdraw_cash(amount)
except InsufficientBalanceException:
    print("Insufficient balance. Please check your account.")
except CashDispenserEmptyException:
    print("Cash dispenser is empty. Please try again later.")
except Exception as e:
    print("An unexpected error occurred:", str(e))
