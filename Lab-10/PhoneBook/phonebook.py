import psycopg2 # Нужно для подключения к PostgreSQL
import csv # Нужно для чтения файлов

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",          
    password="123", 
    host="localhost"
)

cur = conn.cursor()

# TASK 1
def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

query_create_table_users = """
    CREATE TABLE IF NOT EXISTS Users (
        user_id SERIAL PRIMARY KEY,
        user_name TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
"""

query_create_func_search_users = """
    CREATE OR REPLACE FUNCTION search_users(pattern text)
    RETURNS TABLE(user_id integer, user_name text, phone_number text)
    
    AS $BODY$
    BEGIN
        RETURN QUERY SELECT u.user_id, u.user_name, u.phone_number FROM Users u
            WHERE u.user_name LIKE '%' || pattern || '%'
            OR u.phone_number LIKE '%' || pattern || '%';
        RETURN;
    END;
    $BODY$

    LANGUAGE 'plpgsql';
"""

query_create_func_get_users_page = """
    CREATE OR REPLACE FUNCTION public.get_users_page(p_limit integer, p_offset integer)
    RETURNS TABLE(user_id integer, user_name text, phone_number text) 

    AS $BODY$
    BEGIN
        RETURN QUERY SELECT u.user_id, u.user_name, u.phone_number FROM Users u
            ORDER BY u.user_id 
            LIMIT p_limit OFFSET p_offset;
        RETURN;
    END;
    $BODY$

    LANGUAGE 'plpgsql';
"""

query_create_proc_delete_user = """
    CREATE OR REPLACE PROCEDURE public.delete_user(
	IN p_name text DEFAULT NULL::text,
	IN p_phone text DEFAULT NULL::text)
    
    AS $BODY$
    BEGIN
        IF p_name IS NOT NULL THEN
            DELETE FROM Users WHERE user_name = p_name;
        ELSIF p_phone IS NOT NULL THEN
            DELETE FROM Users WHERE phone_number = p_phone;
        END IF;
    END;
    $BODY$

    LANGUAGE 'plpgsql';
"""

query_create_proc_insert_many_users = """
    CREATE OR REPLACE PROCEDURE public.insert_many_users(IN names text[], IN phones text[])
    
    AS $BODY$
    DECLARE
        i INT;
    BEGIN
        FOR i IN 1..array_length(names, 1) LOOP
            INSERT INTO Users(user_name, phone_number)
            VALUES (names[i], phones[i]);
        END LOOP;
    END;
    $BODY$

    LANGUAGE 'plpgsql';
"""

query_create_proc_insert_or_update_user = """
    CREATE OR REPLACE PROCEDURE public.insert_or_update_user(IN p_name text, IN p_phone text)
    
    AS $BODY$
    BEGIN
        IF EXISTS (SELECT 1 FROM Users WHERE user_name = p_name) THEN
            UPDATE Users SET phone_number = p_phone WHERE user_name = p_name;
        ELSE
            INSERT INTO Users (user_name, phone_number) VALUES (p_name, p_phone);
        END IF;
    END;
    $BODY$

    LANGUAGE 'plpgsql';
"""

# TASK 2
# Функции для получения данных из csv и консоли
def insert_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f) # возвращает словарь и поэтому у нас row['user_name'], row['phone_number']
        for row in reader:
            cur.execute(
                "INSERT INTO Users (user_name, phone_number) VALUES (%s, %s)",
                (row['user_name'], row['phone_number'])
            )
    conn.commit()

def insert_from_console():
    name = input("Enter user name: ")
    phone = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO Users (user_name, phone_number) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()


# TASK 3

def update_user(user_id, new_name=None, new_phone=None):
    if new_name:
        cur.execute("UPDATE Users SET user_name = %s WHERE user_id = %s", (new_name, user_id))
    if new_phone:
        cur.execute("UPDATE Users SET phone_number = %s WHERE user_id = %s", (new_phone, user_id))
    conn.commit()

# TASK 4

def search_by_name(name):
    cur.execute("SELECT * FROM Users WHERE user_name ILIKE %s", ('%' + name + '%',))
    return cur.fetchall()

def search_by_phone(phone):
    cur.execute("SELECT * FROM Users WHERE phone_number = %s", (phone,)) # важно получить как кортеж, а не как просто строку
    return cur.fetchall()


# TASK 5
def delete_by_name(name):
    cur.execute("DELETE FROM Users WHERE user_name = %s", (name,))
    conn.commit()

def delete_by_phone(phone):
    cur.execute("DELETE FROM Users WHERE phone_number = %s", (phone,))
    conn.commit()


# *** TASKS FROM LAB 11 ***
# TASK 1
def search_users(pattern):
    try:
        cur.execute("SELECT * FROM search_users(%s)", (pattern,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except:
        conn.rollback()
    conn.commit()

# TASK 2
def insert_or_update_user(name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    conn.commit()
    print(f"User '{name}' added/updated.")

# TASK 3
def insert_many_users(names, phones):

    cur.execute("CALL insert_many_users(%s, %s)", (names, phones)) 
    conn.commit()


# TASK 4
def get_users_page(limit, offset):
    try:
        cur.execute("SELECT * FROM get_users_page(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
    except:
        conn.rollback()
    conn.commit()

# TASK 5
def delete_user(name=None, phone=None):
    cur.execute("CALL delete_user(%s, %s)", (name, phone))
    conn.commit()



# LAB 10
execute_query(query_create_table_users)

insert_from_console()
insert_from_csv("Lab-10/PhoneBook/contacts.csv")
print(search_by_name("Flaw"))
update_user(1, new_phone="6667866") # кого хотим поменять, на что хотим поменять
delete_by_phone("3335433")

# LAB 11

execute_query(query_create_func_get_users_page)
execute_query(query_create_func_search_users)
execute_query(query_create_proc_delete_user)
execute_query(query_create_proc_insert_many_users)
execute_query(query_create_proc_insert_or_update_user)

search_users("Flaw")
insert_or_update_user("Tod", "111222")
insert_many_users(
    ["Lol", "Kek", "InvalidGuy"],
    ["123456", "654321", "333555"]
)
get_users_page(5, 0)
delete_user(name="Lol")
delete_user(phone="654321")

cur.close()
conn.close()
