import os, subprocess
import sys
from app import app, service
from flask import Flask, flash, request, jsonify, make_response
from escpos.printer import Network
import logging

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
def printEscpos():
    if request.method == "POST":
        # get json data from request
        requestBody = request.get_json()
        fileString = requestBody.get('image', False)
        ipPrintert = requestBody.get('network', False)

        # check required body request
        if fileString == '' or fileString == False:
            return make_response(jsonify(
                message='Required image',
                success=False
            ), 422)
        if ipPrintert == '' or ipPrintert == False:
            return make_response(jsonify(
                message='Required network',
                success=False
            ), 422)

        try:
            # service convert base64 to image
            imgdata = service.base64ToImage(fileString)

            if imgdata == '' or imgdata == False:
                return make_response(jsonify(
                    message='Convert base64 to image error',
                    success=False
                ), 422)

            # print to thermal escpos
            printer = Network(host=ipPrintert, port=9100, timeout=30)
            printer.image(imgdata)
            printer.cut()

            print("======================WITECH==========", printer)
            # printer.cashdraw('pin')

            return make_response(
                jsonify(
                    success=True,
                    message='Success print to thermal '+ipPrintert
                ),
                200
            )
        except Exception as e:
            logging.exception(e)
            return make_response(jsonify(
                message=e,
                success=False
            ), 500)
