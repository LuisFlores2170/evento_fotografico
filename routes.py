from flask import Flask, render_template, redirect, url_for, session, request, flash
from main import app
from models.__init__ import *
sesion = session

#----------------------------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template(
        'login.html', 
        foto = "https://cama165802507.files.wordpress.com/2019/09/el-mejor-objetivo-para-fotografia-de-producto-de-tu-tienda-online.jpg"
        
    )

#----------------------------------------------------------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    answer_obtained = model_perfil.get_perfil(
        request.form.get('username'),
        request.form.get('password')
    )
    flash(answer_obtained[1])
    if answer_obtained[0] != None:
        sesion['id'] = answer_obtained[0]
        print('id:', answer_obtained[0])
        return redirect(url_for('panel'))

    
    return redirect(url_for('index'))

#----------------------------------------------------------------------------------------------

@app.route('/logout')
def logout():
    if sesion.get('id') != None:
        sesion['id'] = None
    return redirect(url_for('index'))

#----------------------------------------------------------------------------------------------

@app.route('/account_creation_form')
def account_creation_form():
    return render_template(
        'account_creation_form.html', 
        foto = 'https://th.bing.com/th/id/OIP.e4iL0MAAR5a0dsecvgUk_wHaE8?pid=ImgDet&rs=1'
    )


#----------------------------------------------------------------------------------------------

@app.route('/account_creation', methods=['POST'])
def account_creation():
    done = model_perfil.register(
        request.form.get('username'),
        request.form.get('password'),
        request.form.get('type')
    )
    flash(done)
    return redirect(url_for('account_creation_form'))


#----------------------------------------------------------------------------------------------

@app.route('/panel')
def panel():
    if sesion.get('id') != None:
        return render_template('panel.html')
    return redirect(url_for('index'))
