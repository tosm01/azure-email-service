# azure-email-service
A wrapper service created with the Azure Communication Services Python Email SDK to send Email messages. Built using Django and hosted on Azure App Services.

Below is a list of available api endpoints.

## POST
https://myazureemailservice.azurewebsites.net/api/v1/email

### POST api/v1/email
To send emails to specified recipients. Parameters are passed in using a JSON object.

**Parameters**

|          Name | Type   | Description                                                                                                                                                           |
| -------------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `subject` | string  | The subject of the Email                                                       |
|     `body` | string  | The body of the Email
|     `recipient` | string  | The recipient of the Email
|     `sender` | string  | The Azure registered Email address that will send the Email
