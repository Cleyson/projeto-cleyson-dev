from flask import Flask, request, jsonify
from time import sleep
import psycopg2
import os


app = Flask(__name__)

host = os.getenv("192.168.15.154:8000")
database = os.getenv("quero")
user = os.getenv("postgres")
password = os.getenv("")

html="""
<br>Insira a mensagem no campo abaixo: <br>
<form method='POST' action='/'>
    <input type='text' name='message'>
    <input type='submit'>
</form>
@app.route('/', methods=['GET'])
def index():
    if request.method == 'POST':
        message = request.form.get("message")
        app.logger.info(message)
        save(message)
    return html
"""
def save(message):
    conn = psycopg2.connect(
            host=host,
            database=database,
            user=user
        )
    cur = conn.cursor()  
    sql = "INSERT INTO messages(message) VALUES(%s);"
    cur.execute(sql, (message,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    app.run(debug=True, host="192.168.15.154", port=80)
