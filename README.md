# AlexaServiceRequest
Create Service Request for the Sugar Land Public Works, using Alexa

Developing Custom Skills for Alexa

* This is a tentative to use Flask Framework to develop for Alexa Custom Skills

Important Notes:
1) Flask-Ask temporarily substitute web hosting
2) In order to make it work with Alexa, necessary to use Ngrok to create available https Endpoint
obs.: every time you wish to test, necessary to repeat the following steps
    2a) using Powershell:
    .\ngrok.exe http 5000

    2b) copy the last https generated url
    2c) on www.developer.amazon/alexa, under Endpoint:
        Select HTTP
        paste generated url from Ngrok
        SSL certification: select "Sub-domain with wild card authehtication"

Once Flask-ask stop running, the custom skill will no longer be available!

Once development is complete, consider deploy using AWS lambda:
    * Using Zappa as compiler
    * Uploading a zip folder with all files and dependencies

