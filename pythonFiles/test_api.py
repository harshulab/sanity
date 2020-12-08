from flask import Flask
from flask_mail import Mail, Message
from os import environ
import os

Recipients=os.environ.get('RECIPIENTS')
Sender=os.environ.get('MAIL_USERNAME')
Pass=os.environ.get('MAIL_PASSWORD')

print(Sender)
print(Pass)

app =Flask(__name__)
mail=Mail(app)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME']=Sender
app.config['MAIL_PASSWORD']=Pass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/1/<location>")
def index(location):
   msg = Message('ALERT FROM SANITIZER STATION !!', sender =Sender, recipients =[Recipients])
   msg.body = "%s 's Sanitizer Machine is running empty,Kindly refill it !!" %location
   print(msg)
   mail.send(msg)
   return "Sent mail for machine from %s" %location

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8000,debug = True)
