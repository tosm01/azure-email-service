from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailRecipients, EmailMessage
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class EmailAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Connect to the email client
            email_client = EmailClient.from_connection_string(
                request.data.get('connectionString'))

            # Email details
            content = EmailContent(
                subject=request.data.get('subject'),
                plain_text=request.data.get('body')
            )
            address = EmailAddress(email=request.data.get('recipient'))
            recipient = EmailRecipients(to=[address])
            message = EmailMessage(
                sender=request.data.get('sender'),
                content=content,
                recipients=recipient
            )

            response = email_client.send(message)
            return HttpResponse(status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)