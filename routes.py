from flask import Flask, render_template, redirect, url_for, session, request, flash
from main import app
from models.__init__ import *
sesion = session
#----------------------------------------------------------------------------------------------

# Mensaje de registro de nota de credito
def message(done):
    msg = ['style','color:red', 'EL PROCESO HA FALLADO']
    if done:
        msg = ['style','color:green', 'PROCESO EXITOSO']
    return msg

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
    id_user = model_perfil.model_perfil.get_perfil(
        request.form.get('username'),
        request.form.get('password')
    )
    flash(message(id_user))
    
    return redirect(url_for('index'))

#----------------------------------------------------------------------------------------------

@app.route('/account_creation_form')
def account_creation_form():
    return render_template('account_creation_form.html', foto = 'https://admisionweb.uagrm.edu.bo/img/ficct-892x892.png')
