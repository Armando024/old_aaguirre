import time
import datetime
import db 
import os
import sqlite3
from flask import jsonify,request,Flask, request, session, g, redirect, url_for, abort, render_template, flash

app=Flask(__name__)
app.secret_key='aaguirrewebsie2329ncs'

@app.route('/login',methods=['GET','POST'])
def login():
    if 'login' in session:
        Visits=db.get_Visits();
        return render_template('visits.html',Visits=Visits)
    if(request.method=='POST'):
        password=request.form['password']
        if len(password)==0:
            return render_template('login.html')
        if str(password)=="Not real password":
            Visits=db.get_Visits();
            session['login']=True
            return render_template('visits.html',Visits=Visits)
    return render_template('login.html')

@app.route('/logout', methods=['GET','Post'])
def logout():
    if 'login' in session:
        session.pop('login')
    return render_template('index.html')

@app.route('/logdnns',methods=['POST'])
def logdnns():
    db.log_pro_visits(str(session['id']),'1') 
    return jsonify({'works': str(session['id'])})

@app.route('/logrr',methods=['POST'])
def logrr():
    db.log_pro_visits(str(session['id']),'2') 
    return jsonify({'works': str(session['id'])})

@app.route('/logcal',methods=['POST'])
def logcal():
    db.log_pro_visits(str(session['id']),'3') 
    return jsonify({'works': str(session['id'])})

@app.route('/logSim',methods=['POST'])
def logSim():
    db.log_pro_visits(str(session['id']),'4') 
    return jsonify({'works': str(session['id'])})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.route('/',methods=['GET'])
def index():
    #print(db.get_Visits())
    #db.log_visit(str(request.remote_addr))
    id=db.log_visit(str(request.environ['REMOTE_ADDR']),request.user_agent)
    print(id)
    session['id']=id[0] 
    return render_template('index.html')


if __name__=='__main__':
    app.run()
