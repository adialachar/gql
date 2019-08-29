from django.core.mail import EmailMessage


def send_email(subject, body, to):
    email = EmailMessage(subject, body, 'citrushack@gmail.com', to)
    email.send(fail_silently=False)


def send_application_email(recipient):
    subject = "Thank you for applying to Cutie Hack 2019!"
    body = "Thank you for applying to Cutie Hack this fall. Make sure to check this email for updates from us. We hope to see you there! \n \n Sincerely, \n The Cutie Hack Team"
    to = [recipient]

    send_email(subject=subject,body=body,to=to)

