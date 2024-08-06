import threading
import time
import random
import uuid
from datetime import datetime, timezone

class FinancialTransaction:
    def __init__(self, transaction_id, timestamp, amount, currency, sender_account_id, receiver_account_id):
        self.transaction_id = transaction_id
        self.timestamp = timestamp
        self.amount = amount
        self.currency = currency
        self.sender_account_id = sender_account_id
        self.receiver_account_id = receiver_account_id

    def __repr__(self):
        return f"FinancialTransaction(transaction_id={self.transaction_id}, timestamp={self.timestamp}, amount={self.amount}, currency={self.currency}, sender_account_id={self.sender_account_id}, receiver_account_id={self.receiver_account_id})"


def generate_dummy_transaction(transaction_id):
    timestamp = datetime.now(timezone.utc)
    amount = round(random.uniform(0.01, 1000.00), 2)
    currency = random.choice(['USD', 'EUR', 'JPY', 'GBP'])
    sender_account_id = random.randint(1, 1000)
    receiver_account_id = random.randint(1, 1000)

    while receiver_account_id == sender_account_id:
        receiver_account_id = random.randint(1, 1000)

    return FinancialTransaction(transaction_id, timestamp, amount, currency, sender_account_id, receiver_account_id)


def transaction_producer():
    transaction_id = 1
    while True:
        transaction = generate_dummy_transaction(transaction_id)
        print(transaction)
        transaction_id += 1
        time.sleep(1)


background_thread = threading.Thread(target=transaction_producer, daemon=True)


def run():
    background_thread.start()

    while True:
        pass
