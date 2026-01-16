import psycopg

# Connect to an existing database
def get_connection():
    return psycopg.connect("dbname=postgres user=postgres password=151731 host=localhost")