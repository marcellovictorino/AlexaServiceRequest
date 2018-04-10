import smtplib

def sendEmail (location, concern_category, description, name, phoneNumber ):
    # Gmail account login info
    user = 'sugarlandtmc@gmail.com'
    password = '1TrafficSignals'

    # Connection SMTP with Gmail
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com')
    server_ssl.ehlo()
    server_ssl.login(user,password)

    # Email settings
    sent_from = user
    # to = ['jturner@sugarlandtx.gov', 'JVAUGHN@sugarlandtx.gov','ccase@sugarlandtx.gov', 'mvictorino@sugarlandtx.gov']
    to = ['mvictorino@sugarlandtx.gov']


    msg = "\r\n".join([
        "From: " + user,
        "To: " +  ';'.join(to),
        "Subject: [Alexa] Service Request - {3}",
        "",
        "Hi,\n\n" \
        "The following information was provided by a resident using Alexa Digital Assistant. Please, create a Service Request if appropriate: \n\n" \
        "Issue Category: {0} \n" \
        "Issue Location: {1} \n" \
        "Full issue Description: {2} \n\n"
        "Resident Info:\n" \
        "Name: {3}\n" \
        "Phone Number: {4} \n\n" \
        "Best regards, \n" \
        "Python & Alexa!".format(concern_category, location, description, name, phoneNumber)
        ])

    # Actually sending the email
    server_ssl.sendmail(sent_from, to, msg)

    server_ssl.close()

    return print('Email sent')