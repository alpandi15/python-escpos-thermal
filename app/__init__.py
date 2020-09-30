from flask import Flask
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)
cors = CORS(app, reqources={
   r"/*": {
      "origins": "*"
   }
})
from app import controller

if __name__ == "__main__":
   logging.basicConfig(filename='error.log',level=logging.DEBUG)
   app.run(host='0.0.0.0', port=5000, ssl_context=('ssl/cert.pem', 'ssl/key.pem'))
