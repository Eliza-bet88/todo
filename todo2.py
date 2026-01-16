import psycopg

with psycopg.connect("dbname=postgres user=postgres password=151731 host=localhost") as conn:

    with conn.cursor() as cur:

        cur.execute("""
            CREATE TABLE IF NOT EXISTS todo (
                id serial PRIMARY KEY,
                task TEXT,
                status BOOLEAN)
            """)

        cur.execute(
            "INSERT INTO todo (task, status) VALUES (%s, %s)",
            ("buy milk", False)
             
             )

        cur.execute("SELECT * FROM todo")
        print("all tasks:")
        for row in cur:
            print(row)
        
        cur.execute("UPDATE todo SET status = TRUE WHERE id = %s", (1,))

        cur.execute("DELETE FROM todo WHERE id = %s", (2,))
        

        conn.commit()