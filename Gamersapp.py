import re
from flask import Flask
"import dbconnection as db"


app = Flask(__name__)

from flask import abort, redirect, render_template, request, url_for
"""import mysql.connector
import sys
import boto3
import os

ENDPOINT="database-1.cvlek1uj9drj.us-west-1.rds.amazonaws.com"
PORT="3306"
USER="Administrator"
REGION="us-west-1c"
DBNAME="database-1"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
#session = boto3.Session(profile_name='admin')
#client = session.client('rds')

#token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USER, passwd='Hackztecs.Audi2022', port=PORT, db=DBNAME)
    cur = conn.cursor()
    cur.execute("SELECT now()")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))"""


@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("inicio.html")



@app.route('/principal', methods=['GET', 'POST'])
def principal():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("principal.html")


@app.route('/fotos_cui', methods=['GET', 'POST'])
def fotos_cui():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("fotos_cui.html")


@app.route('/fotos_juegos', methods=['GET', 'POST'])
def fotos_juegos():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("fotos_juegos.html")

@app.route('/fotos_accesorios', methods=['GET', 'POST'])
def fotos_accesorios():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("fotos_accesorios.html")


@app.route('/navbar_2', methods=['GET', 'POST'])
def navbar_2():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("navbar_2.html")

@app.route('/nav_bar1', methods=['GET', 'POST'])
def nav_bar1():
    if request.method == "GET":
        print("GETTTTTTTTTTTTTTTTTTTTTTTTTTTT")
        return render_template("nav_bar1.html")