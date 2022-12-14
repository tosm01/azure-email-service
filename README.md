# Azure Email Service
A service for sending Emails created with the Azure Communication Services Python Email SDK built using Django and hosted on Azure App Service. Link to guide: https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/send-email?pivots=programming-language-python

![System Architecture](EmailServiceArchitecture.png)

Below is a list of available api endpoints.

## POST /api/v1/email
To send emails to a specified recipient. Parameters are passed in using a JSON object.

#### Parameters

|          Name | Type   | Description                                                                                                                                                           |
| -------------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `subject` | string  | The subject of the Email                                                       |
|     `body` | string  | The body of the Email
|     `recipients` | array  | A list of the recipients of the Email
|     `sender` | string  | The Azure registered Email address that will send the Email

#### Sample Email
![Sample Email](SampleEmail.png)
