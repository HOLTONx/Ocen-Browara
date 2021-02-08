from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector
from random import randint

app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'GET':
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="browar_db"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM browary ORDER BY ocena DESC LIMIT 3")
        results = mycursor.fetchall()
        mycursor.execute("SELECT * FROM browary ORDER BY RAND() LIMIT 1")
        ran = mycursor.fetchone()
        mydb.close()

    return render_template('index.html', results = results, ran = ran)

@app.route('/ranking', methods=['GET', 'POST'])
def ranking():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="browar_db"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM browary ORDER BY ocena DESC")
    results = mycursor.fetchall()

    if request.method == 'POST':
        for r in results:
            try:
                if request.form[str(r[0])] == '-':
                    q = "UPDATE browary SET ocena=ocena-1 WHERE id=" + str(r[0])
                    mycursor.execute(q)
                    mydb.commit()
                elif request.form[str(r[0])] == '+':
                    q = "UPDATE browary SET ocena=ocena+1 WHERE id=" + str(r[0])
                    mycursor.execute(q)
                    mydb.commit()
            except:
                pass
            
    mycursor.execute("SELECT * FROM browary ORDER BY ocena DESC")
    results = mycursor.fetchall()

    return render_template('ranking.html', results = results)

@app.route('/dodaj-piwo', methods=['GET', 'POST'])
def addNew():
    if request.method == 'POST':
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="browar_db"
        )

        data = request.form
        q = 'INSERT INTO browary (typ, browar, alkohol) values("' + data['name'] + '","' + data['company'] + '","' + data['alcohol'] + '")'
        mycursor = mydb.cursor()
        mycursor.execute(q)
        mydb.commit()
        mydb.close()

    return render_template('dodaj_piwo.html')

@app.route('/kontakt')
def contact():
    return render_template('kontakt.html')