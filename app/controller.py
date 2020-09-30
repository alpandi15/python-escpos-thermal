from app import app
from flask import Flask, flash, request, jsonify, make_response
from escpos.printer import Network
from base64 import b64decode

@app.route('/', methods = ['GET'])
def index():
    return make_response(
        jsonify(
            info="Web service thermal print",
            version="1.0"
        ),
        200
    )

@app.route('/print', methods = ['POST'])
def print():
    if request.method == "POST":
        fileString = request.get_json()
        printer = Network('192.168.1.216')
        printer.text("Hello World\n")
        printer.barcode('1324354657687', 'EAN13', 64, 2, '', '')
        printer.cut()

        return make_response(
            jsonify(
                success=True,
                printer=fileString
            ),
            200
        )
