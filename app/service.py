from base64 import b64decode

def base64ToImage(string):
    try:
        if string == '':
            return False

        imgdata = b64decode(string)
        filename = 'app/public/bill.png'
        with open(filename, 'wb') as f:
            f.write(imgdata)

        return filename
    except Exception as e:
        return e
