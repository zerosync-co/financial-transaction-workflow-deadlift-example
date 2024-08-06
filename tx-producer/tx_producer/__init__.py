import time
import random
from datetime import datetime, timezone
from confluent_kafka import Producer

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


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.value()))


def run():
    producer = Producer({
        'bootstrap.servers': 'localhost:9092'
    })

    try:
        transaction_id = 1
        while True:
            transaction = generate_dummy_transaction(transaction_id)
            producer.produce('transaction', str(transaction), callback=delivery_report)
            producer.poll(0)
            transaction_id += 1
            time.sleep(1)
    except KeyboardInterrupt:
        print()
    finally:
        producer.flush()
