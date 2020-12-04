import flask

import smtplib


SENDER_UNAME= 'sanitizerstation2@gmail.com'
RECIPIENTS_ = "avnoorsingh488@gmail.com"
subject = 'SANITATION STATION ALERT!!!'
CC='chiyabansal@gmail.com'
body= 'Directorate Office Tank Is Running Empty \n  Please refill the tank'

email_text = "From: {0} \nTo: {1} \nCC:{2}Subject: {3} \n\n {4}".format(SENDER_UNAME, RECIPIENTS_,CC,
                                                                                  subject, body)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465) 
server.ehlo()
server.login(SENDER_UNAME, 'avnoor123')
#server.sendmail(SENDER_UNAME ,     RECIPIENTS_,        email_text)
                #sender             #reciever         #email text
app = flask.Flask(__name__)
app.config["DEBUG"] = True
print('red -----------------------------------------')

@app.route('/home', methods=['GET'])
def home():
    print('something happened')
    server.sendmail(SENDER_UNAME ,     RECIPIENTS_,        email_text)

    return "<h1>THIS IS RESPONSE FROM RASPBERRY PI -- Distant Reading Archive</h1><p>This site is a prototype API response for email trigger.</p>"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8000)
