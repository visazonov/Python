import psycopg2

first_name = 'Ваня'
last_name = 'Иванов4'
email = '56ivan@mail.ru'
def create_db(cur):
        cur.execute('''
        DROP TABLE phone;
        DROP TABLE client;
        ''')

        cur.execute('''
                CREATE TABLE IF NOT EXISTS client (
                client_id SERIAL PRIMARY KEY, 
                name VARCHAR(20) NOT NULL, 
	            last_name VARCHAR(20) NOT NULL, 
	            mail VARCHAR(50) unique NOT NULL); 
	            ''')

        cur.execute('''
                CREATE TABLE IF NOT EXISTS phone (
	                    phone_id SERIAL PRIMARY KEY, 
	                    phone_number VARCHAR(12) unique, 
	                    client_id INTEGER REFERENCES client(client_id) 
                                                  ); 
                ''')
        conn.rollback() # все описанные запросы выше будут проигнорированы
        # conn.commit() #отправить запрос


def add_client(cur, first_name, last_name, email, phones=None):
        cur.execute(
        '''INSERT INTO client(name, last_name, mail)
        VALUES(%s, %s, %s) RETURNING client_id, name;''', (first_name, last_name, email)
        )
        client_id = cur.fetchone()[0]
        print(client_id)
        if phones is None:
                pass
        else:
                add_phone(cur, client_id, phones)

def add_phone(cur, client_id, phone):
        cur.execute(
        '''INSERT INTO phone(phone_number, client_id) 
        VALUES(%s, %s);''', (phone, client_id)
        )
        conn.rollback()
        # conn.commit()

def change_client(cur, client_id, first_name=None, last_name=None, email=None, phones=None, phone_id=None):
        if first_name is None:
                pass
        else:
                cur.execute(
                '''UPDATE client 
                SET name = %s  
                WHERE client_id = %s;''', (first_name, client_id)
                )

        if last_name is None:
                pass
        else:
                cur.execute(
                '''UPDATE client 
                SET last_name = %s  
                WHERE client_id = %s;''', (last_name, client_id)
                )

        if email is None:
                pass
        else:
                cur.execute(
                '''UPDATE client 
                SET mail = %s  
                WHERE client_id = %s;''', (email, client_id)
                )

        if phones is None:
                pass
        else:
                cur.execute(
                '''UPDATE phone 
                SET phone_number = %s  
                WHERE phone_id = %s;''', (phones, phone_id)
                )

        # conn.rollback()
        conn.commit()

def delete_phone(cur, client_id, phone):
        cur.execute(
        '''DELETE FROM phone 
        WHERE phone_number = %s AND client_id = %s;''', (phone, client_id)
        )
        conn.rollback()
        # conn.commit()

def delete_client(cur, client_id):
        cur.execute(
        '''DELETE FROM phone 
        WHERE client_id = %s;''', (client_id,)
        )

        cur.execute(
        '''DELETE FROM client 
        WHERE client_id = %s;''', (client_id,)
        )
        # conn.rollback()
        conn.commit()

def find_client(cur, first_name=None, last_name=None, email=None, phone=None):
        if first_name is None:
                pass
        else:
                cur.execute(
                '''SELECT *  
                FROM client  
                WHERE name = %s;''', (first_name,)
                )

        if last_name is None:
                pass
        else:
                cur.execute(
                '''SELECT *  
                FROM client  
                WHERE last_name = %s;''', (last_name,)
                )

        if email is None:
                pass
        else:
                cur.execute(
                '''SELECT *  
                FROM client  
                WHERE mail = %s;''', (email,)
                )
                client = cur.fetchall()
                print(client)

        if phone is None:
                pass
        else:
                cur.execute(
                '''SELECT *  
                FROM phone  
                WHERE phone_number = %s;''', (phone,)
                )
                client_id = cur.fetchone()[2]
                cur.execute(
                '''SELECT *  
                FROM client  
                WHERE client_id = %s;''', (client_id,)
                )
                client = cur.fetchone()
                print(client)


conn = psycopg2.connect(database='netology', user='postgres', password='123Swe22+') #создали соединение с БД
with conn.cursor() as cur:
        # create_db(cur)
        # add_client(cur, first_name, last_name, email, phones=None)
        # add_client(cur, 'Vasily', 'Vasilyev', 'Vasily@mail.ru', '89995551122')
        # add_phone(cur, 17, '89995544118')
        # change_client(cur, 5, first_name='Alexey', last_name=None, email=None, phones='89995554415', phone_id=2)
        # change_client(cur, 2, last_name='Petrova')
        # delete_phone(cur, 5, '89995554415')
        # delete_client(cur, 5)
        # find_client(cur, first_name=None, last_name=None, email=None, phone='89995551135')

conn.close()