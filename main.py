
from flask import Flask, flash

#--------------------------------------------------------------------------

app = Flask(__name__)
app.secret_key = "mysecretkey"

#--------------------------------------------------------------------------

from routes import *

#--------------------------------------------------------------------------

if __name__=='__main__':
	app.run(debug=True)