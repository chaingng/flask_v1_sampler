from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # return send_file('/etc/passwd', mimetype='text/plain', conditional=True)
    return send_file('/etc/passwd', as_attachment=True, attachment_filename=u'Ñandú／pingüino.txt')

app.run()