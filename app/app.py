from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD","postgres")
POSTGRES_DB = os.getenv("POSTGRES_DB","testdb")
POSTGRES_HOST = os.getenv("POSTGRES_HOST","db")


def get_connection():
    conn = psycopg2.connect(
        host = POSTGRES_HOST,
        database = POSTGRES_DB,
        user = POSTGRES_USER,
        password = POSTGRES_PASSWORD
        )
    return conn
        
@app.route('/')
def index():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        cur.close()
        return jsonify({"message":"Hello from Flask !","postgres_version":db_version})
    except Exception as e :
        return jsonify({"error":str(e)})
        
if __name__=='__main__':
    app.run(host='0.0.0.0',port =5000)
        
