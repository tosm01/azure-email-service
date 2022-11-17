from azure.identity import DefaultAzureCredential
from azure.communication.identity import CommunicationIdentityClient
from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailRecipients, EmailMessage
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from env import REGISTERED_SENDERS_LIST

class EmailAPI(APIView):
    def post(self, request, *args, **kwargs):
        sender = request.data.get('sender')
        recipients = request.data.get('recipients')
        
        if sender not in REGISTERED_SENDERS_LIST:
            return HttpResponse(content="Sender is not registered", status=status.HTTP_400_BAD_REQUEST)
        elif not all(recipient in REGISTERED_SENDERS_LIST[sender]["allowed_recipients_list"] for recipient in recipients):
            return HttpResponse(content="You are not allowed to send an email to one or more of the specified recipient(s)", status=status.HTTP_400_BAD_REQUEST)

        try:
            # Connect to the email client
            email_client = EmailClient.from_connection_string(REGISTERED_SENDERS_LIST[sender]["connection_string"])

            # Email details
            content = EmailContent(
                subject=request.data.get('subject'),
                plain_text=request.data.get('body')
            )
            addresses = [EmailAddress(email=recipient) for recipient in recipients]
            recipients = EmailRecipients(to=addresses)
            message = EmailMessage(
                sender=sender,
                content=content,
                recipients=recipients
            )

            response = email_client.send(message)
            return HttpResponse(status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)