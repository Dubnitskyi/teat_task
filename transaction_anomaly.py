import json
def finding_anomalies(transaction_list, deviation):

    user_amount = {}
    anomaly_transaction = []

    # Розбиваємо список на потрібні нам елементи, а саме користувач (user_id а не просто  id транзації) і сумма транзакції
    for transaction in transaction_list:
        user = transaction['user_id']
        amount = transaction['amount']

        if user not in user_amount:
            user_amount[user] = []

        # Групуємо всі транзакції користувачів до одного юзера щоб позбутись лишніх
        user_amount[user].append(amount)


        # За формулою підраховуємо стандартне відхилення
        amounts = user_amount[user]
        mean = sum(amounts) / len(amounts)
        standard_deviation = (sum((x - mean) ** 2 for x in amounts) / len(amounts)) ** 0.5

        #Перевірка для уникнення помилок
        if standard_deviation > 0:
            anomaly = abs(amount - deviation) / standard_deviation
        else:
            anomaly = 0

        #Заповнення нового списку аномальниими транзакціями
        if anomaly > deviation:
            anomaly_transaction.append({
                "id": transaction["id"],
                "user_id": user,
                "category": transaction["category"],
                "amount": amount,
                "timestamp": transaction["timestamp"],
                "anomaly_score": round(anomaly, 2)
            })
    return anomaly_transaction


deviation = 2.5 #Норма відхилення

transactions_list = [
    {"id": 1, "user_id": 1001, "category": "food", "amount": 15.50, "timestamp": "2024-03-06 12:30:00"},
    {"id": 2, "user_id": 1001, "category": "food", "amount": 16.00, "timestamp": "2024-03-07 13:00:00"},
    {"id": 3, "user_id": 1001, "category": "food", "amount": 500.00, "timestamp": "2024-03-08 14:15:00"},
    {"id": 4, "user_id": 1002, "category": "electronics", "amount": 250.00, "timestamp": "2024-03-05 14:00:00"},
    {"id": 5, "user_id": 1002, "category": "electronics", "amount": 100.00, "timestamp": "2024-03-06 15:00:00"},
    {"id": 6, "user_id": 1002, "category": "electronics", "amount": 500.00, "timestamp": "2024-03-07 16:00:00"},
    {"id": 7, "user_id": 1003, "category": "electronics", "amount": 20.32, "timestamp": "2024-03-07 16:00:00"},
    {"id": 8, "user_id": 1003, "category": "electronics", "amount": 370.00, "timestamp": "2024-03-07 16:00:00"},
    {"id": 9, "user_id": 1002, "category": "electronics", "amount": 50.50, "timestamp": "2024-03-07 16:00:00"},
    {"id": 10, "user_id": 1002, "category": "electronics", "amount": 20.00, "timestamp": "2024-03-07 16:00:00"},
    {"id": 11, "user_id": 1001, "category": "electronics", "amount": 3200.00, "timestamp": "2024-03-07 16:00:00"},

]


print(finding_anomalies(transactions_list, deviation))

with open('anomaly_transaction.json', 'w') as json_file:
    json.dump(finding_anomalies(transactions_list, deviation), json_file, indent=4)