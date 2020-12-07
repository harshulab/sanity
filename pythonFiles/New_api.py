from flask import Flask
from flask_mail import Mail, Message
import os

UserName=os.getenv('USR_NAME')
UserPass=os.getenv('USR_PASS')
Recipients=os.getenv('RECIPIENTS')


app =Flask(__name__)
mail=Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] =UserName
app.config['MAIL_PASSWORD'] =UserPass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/1/<location>")
def index(location):
   msg = Message('ALERT FROM SANITIZER STATION !!', sender = UserName, recipients =Recipients)
   msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" %location
   mail.send(msg)
   return "Sent mail for machine from %s" %location

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000,debug = True)
