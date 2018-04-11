import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail (location, concern_category, description, name, phoneNumber ):
    # Gmail account login info
    user = 'sugarlandtmc@gmail.com'
    password = 'tr9ff1cS1gn9l$01'

    # Connection SMTP with Gmail
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com')
    server_ssl.ehlo()
    server_ssl.login(user,password)

    # Email settings
    sent_from = user
    # to = ['jturner@sugarlandtx.gov', 'JVAUGHN@sugarlandtx.gov','ccase@sugarlandtx.gov', 'mvictorino@sugarlandtx.gov']
    to = ['mvictorino@sugarlandtx.gov']

    msg = MIMEMultipart()
    msg['From'] = sent_from
    msg['To'] = ", ".join(to)
    msg['Subject'] = "[Alexa] Service Request - {}".format(name)

    body_txt = """\
        <html>
          <head></head>
          <body>
            <p>Hi,<br><br>
               The following information was provided by a resident using Alexa Digital Assistant. Please, create a Service Request if appropriate:<hr><br>
               
               <b>Issue Category</b>: {0} <br>
               <b>Issue Location</b>: {1} <br>
               <b>Full issue Description</b>: {2} <br><br>

               <u><b>Resident Info:</b></u> <br>
               <b>Name</b>: {3} <br>
               <b>Phone Number</b>: {4} <br><br>

               Best regards,<br>
               Python & Alexa!
            </p>
          </body>
        </html>
        """.format(concern_category, location, description, name, phoneNumber)

    msg.attach(MIMEText(body_txt, 'html')) #this makes sure the formatting will remain

    text = msg.as_string()

    # Actually sending the email
    server_ssl.sendmail(sent_from, to, text)

    server_ssl.close()

    return print('Email sent')