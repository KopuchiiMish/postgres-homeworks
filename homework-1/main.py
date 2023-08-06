"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
import psycopg2
import csv

ORDERS_DATA = os.path.join('north_data', 'orders_data.csv')
EMPLOYEES_DATA = os.path.join('north_data', 'employees_data.csv')
CUSTOMERS_DATA = os.path.join('north_data', 'customers_data.csv')

if __name__ == '__main__':
    connection = psycopg2.connect(host='localhost', database='north', user='nataliagovorushkina', password='Qwerty12345')
    try:
        with connection:
            with connection.cursor() as cursor:
                with open(CUSTOMERS_DATA) as csvfile:
                    list_ = csv.DictReader(csvfile, delimiter=',')
                    for row in list_:
                        cursor.execute('INSERT INTO customers_data VALUES (%s, %s, %s)',
                                       (row['customer_id'], row['company_name'], row['contact_name']))
                with open(EMPLOYEES_DATA) as csvfile:
                    list_ = csv.DictReader(csvfile, delimiter=',')
                    for row in list_:
                        cursor.execute('INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)',
                                       (row['employee_id'], row['first_name'], row['last_name'],
                                        row['title'], row['birth_date'], row['notes']))
                with open(ORDERS_DATA) as csvfile:
                    list_ = csv.DictReader(csvfile, delimiter=',')
                    for row in list_:
                        cursor.execute('INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)',
                                       (row['order_id'], row['customer_id'],
                                        row['employee_id'], row['order_date'], row['ship_city']))
    finally:
        connection.close()
