from db import get_connection


def register(email,password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO userr(email,password) VALUES(%s, %s)", (email, password))
        conn.commit()

def login_user(email,password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM userr WHERE email = %s AND password = %s", (email, password))
            login_user = cur.fetchone() 
            return(login_user)


def access_id(email,password):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM userr WHERE email = %s AND password = %s", (email, password)
                        )
            user_id = cur.fetchone() 
            return(user_id)


def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS todo (
                id serial PRIMARY KEY,
                task TEXT,
                status BOOLEAN,
                access_id INT REFERENCES access(id))
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS access (
                id SERIAL PRIMARY KEY,
                user_id INT REFERENCES userr(id),
                todo_id INT REFERENCES todo(id))
            """)
            cur.execute("""
            CREATE TABLE IF NOT EXISTS userr (
                id serial PRIMARY KEY,
                email TEXT,
                password TEXT)
            """)
 


def add_task(task, user_id, status = False):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO todo (task,status) VALUES (%s, %s)",
                (task, status),
            )
            cur.execute("SELECT id FROM todo WHERE task = %s", (task,))
            todo_id = cur.fetchone()
            print(todo_id)
            cur.execute("INSERT INTO access (user_id,todo_id) VALUES (%s, %s)", (user_id, todo_id[0]))
        conn.commit()

    
def show_all_tasks():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM todo")
            print(cur.fetchall())
        conn.commit()

    
def show_not_comleted():
    with get_connection() as conn:
        with conn.cursor() as cur: 
            cur.execute("SELECT id, task FROM todo WHERE status = FALSE")
            print(cur.fetchall())
        conn.commit()


def update_task_status(task_id):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE todo SET status = TRUE WHERE id = %s", (task_id,))
        conn.commit()

def delete_tasks(task_id):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM todo WHERE id = %s", (task_id,))
            conn.commit()
