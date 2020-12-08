from flask import Flask
from flask_mail import Mail, Message
# from os import environ
import os

Recipients = os.environ.get('RECIPIENTS')
Sender = os.environ.get('MAIL_USERNAME')
Pass = os.environ.get('MAIL_PASSWORD')

print(Sender)
print(Pass)

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = Sender
app.config['MAIL_PASSWORD'] = Pass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/1/<location>")
def index1(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/2/<location>")
def index2(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/3/<location>")
def index3(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/4/<location>")
def index4(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/5/<location>")
def index5(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/6/<location>")
def index6(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/7/<location>")
def index7(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/8/<location>")
def index8(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/9/<location>")
def index9(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/10/<location>")
def index10(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/11/<location>")
def index11(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/12/<location>")
def index12(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/13/<location>")
def index13(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/14/<location>")
def index14(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/15/<location>")
def index15(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/16/<location>")
def index16(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


@app.route("/17/<location>")
def index17(location):
    msg = Message('ALERT FROM SANITIZER STATION !!', sender=Sender, recipients=[Recipients])
    msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" % location
    print(msg)
    mail.send(msg)
    return "Sent mail for machine from %s" % location


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
