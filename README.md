# Azure Email Service
A service wrapper for sending Emails created with the Azure Communication Services Python Email SDK built using Django and hosted on Azure App Service. Link to guide: https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/email/send-email?pivots=programming-language-python

![System Architecture](EmailServiceArchitecture.png)

Below is a list of available api endpoints.

## POST
https://myazureemailservice.azurewebsites.net/api/v1/email

### POST api/v1/email
To send emails to a specified recipient. Parameters are passed in using a JSON object.

#### Parameters

|          Name | Type   | Description                                                                                                                                                           |
| -------------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `subject` | string  | The subject of the Email                                                       |
|     `body` | string  | The body of the Email
|     `recipient` | string  | The recipient of the Email
|     `sender` | string  | The Azure registered Email address that will send the Email

#### Sample Email
![Sample Email](SampleEmail.png)

## Future Work
- [ ] Replace connection strings with service principals for server-side authentication.
- [ ] Enforce API keys so that clients have to provide authentication credentials to use the service. (Note: Currently access is restricted via CORS policies)
- [ ] Add multi-recipients functionality
