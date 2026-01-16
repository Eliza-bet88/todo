from db import get_connection

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
            CREATE TABLE IF NOT EXISTS todo (
                id serial PRIMARY KEY,
                task TEXT,
                status BOOLEAN)
            """)


def add_task(task, status=False):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO todo (task,status) VALUES (%s, %s)",
                (task, status),
            )
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





        