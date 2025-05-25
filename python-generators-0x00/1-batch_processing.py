import mysql.connector
from seed import connect_to_prodev

def stream_users_in_batches(batch_size):
    connection = connect_to_prodev()
    if not connection:
        return
    try:
        cursor = connection.cursor(dictionary=True)
        offset = 0
        while True:
            cursor.execute(f"SELECT * FROM user_data LIMIT {batch_size} OFFSET {offset}")
            batch = cursor.fetchall()
            if not batch:
                break
            yield batch
            offset += batch_size
        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error streaming batches: {err}")

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
                yield user