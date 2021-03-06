import mysql.connector
import yaml
from flask import jsonify

db = yaml.safe_load(open("yamls/db.yaml"))


class CostumerTable:
    def __init__(self):
        costumer_db = mysql.connector.connect(
            host=db["mysql_host"],
            port = int(db["mysql_port"]),
            user=db["mysql_user"],
            password=db["mysql_password"],
            database=db["mysql_db"]
        )

        # to do : videti sta jos dodati u tabelu; transakcije, novac, idt...
        costumer_cursor = costumer_db.cursor()
        costumer_cursor.execute('CREATE TABLE IF NOT EXISTS Costumers (FirstName varchar(32), LastName varchar(32), '
                            'Address varchar(32), City varchar(32), Country varchar(32), PhoneNumber varchar(32), '
                            'Password varchar(256), Email varchar(32), Verified boolean)')
        costumer_cursor.close()
        costumer_db.close()

    def add_customer(self, customer, costumer_cursor, conn):
        sql = 'INSERT INTO Costumers (FirstName, LastName, Address, City, Country, PhoneNumber, Password, Email, Verified) ' \
              'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (customer.first_name, customer.last_name, customer.address, customer.town, customer.country,
               customer.phoneNumber, customer.password, customer.email, False)
        costumer_cursor.execute(sql, val)
        conn.commit()

    def update_customer(self, customer, costumer_cursor, conn):
        sql = 'UPDATE Costumers SET FirstName = %s, LastName = %s, Address = %s, City = %s, Country = %s, PhoneNumber = %s, Password = %s WHERE Email = %s'
        val = (customer.first_name, customer.last_name, customer.address, customer.town, customer.country,
               customer.phoneNumber, customer.password, customer.email)
        costumer_cursor.execute(sql, val)
        conn.commit()

    def verify_customer(self, customer, costumer_cursor, conn):
        sql = 'UPDATE Costumers SET Verified = %s WHERE Email = %s'
        val = (True, customer[7])
        costumer_cursor.execute(sql, val)
        conn.commit()

    def get_costumer(self, costumer_cursor, email):
        costumer_cursor.execute('SELECT * FROM Costumers')
        data = costumer_cursor.fetchall()

        for costumer in data:
            print(costumer, '\n')
            if costumer[7] == email:
               return costumer

        return None
