from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_data():
    conn = psycopg2.connect(dbname='mindtvdata', user='postgres', password='yourpassword', host='localhost')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM eeg_data WHERE participant_id = %s", (1,))
    eeg_data = cursor.fetchall()
    
    cursor.execute("SELECT * FROM gsr_hr_data WHERE participant_id = %s", (1,))
    gsr_data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return eeg_data, gsr_data

@app.route('/')
def index():
    eeg_data, gsr_data = get_data()
    return render_template('index.html', eeg_data=eeg_data, gsr_data=gsr_data)

if __name__ == '__main__':
    app.run(debug=True)
