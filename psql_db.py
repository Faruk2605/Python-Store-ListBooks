import psycopg2
from psycopg2 import sql


def connect():    
    return psycopg2.connect(
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
        database="mini_liblary"
    )
    
def insert_data(book_name, author, year_publication):
    try:
        connection = connect()
        cursor = connection.cursor()
        insert_query = """insert into list_books (book_name, author, year_publication) values (%s, %s, %s);"""
        record_to_insert = (book_name, author, year_publication)
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        connection.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        return False
        


