from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration

db = mysql.connector.connect(
  user='root',
  host='localhost',
  database='mess-buddy',
  password='hjt&()8976A'
)


# Homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

# Complaint Page
@app.route('/complaints', methods=['GET', 'POST'])
def complaints():
    
    if request.method == 'POST':
        student_name = request.form['student_name']
        complaint_text = request.form['complaint_text']
        cursor = db.cursor()
        cursor.execute("INSERT INTO complaints (student_name, complaint_text) VALUES (%s, %s)", (student_name, complaint_text))
        db.commit()
        flash('Complaint submitted successfully!')
        return redirect('/complaints')
    return render_template('complaints.html')

# Rebate Form Page
@app.route('/rebate', methods=['GET', 'POST'])
def rebate():
    if request.method == 'POST':
        student_id = request.form['student_id']
        reason = request.form['reason']
        cursor = db.cursor()
        cursor.execute("INSERT INTO rebate_requests (student_id, reason) VALUES (%s, %s)", (student_id, reason))
        db.commit()
        flash('Rebate form submitted successfully!')
        return redirect('/rebate')
    return render_template('rebate.html')

if __name__== '_main_':
    app.run(debug=True)