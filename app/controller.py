from app import app, service
from flask import Flask, flash, request, jsonify, make_response
from escpos.printer import Network

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
        requestBody = request.get_json()
        fileString = requestBody.get('image', False)

        if fileString == '' or fileString == False:
            return make_response(jsonify(
                message='Required image',
                success=False
            ), 422)

        imgdata = service.base64ToImage(fileString)

        if imgdata == '' or imgdata == False:
            return make_response(jsonify(
                message='Convert base64 to image error',
                success=False
            ), 422)

        printer = Network(host='192.168.1.216')
        printer.image(imgdata)
        printer.cut()

        return make_response(
            jsonify(
                success=True,
                printer=fileString
            ),
            200
        )
