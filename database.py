import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="BANCOnovo",
        user="postgres",
        password="123456"
    )
