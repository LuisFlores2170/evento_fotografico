
from flask import Flask, render_template, redirect, url_for
from main import app

#----------------------------------------------------------------------------------------------

@app.route('/')
def login():
    return render_template(
        'login.html', 
        foto = "https://cama165802507.files.wordpress.com/2019/09/el-mejor-objetivo-para-fotografia-de-producto-de-tu-tienda-online.jpg"
        
    )
    