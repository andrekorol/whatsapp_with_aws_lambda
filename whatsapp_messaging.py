from twilio.rest import Client
import authentication
import contacts


def msg_mom_and_dad(event=None, context=None):

    twilio_sid = authentication.sid
    auth_token = authentication.auth_token

    whatsapp_client = Client(twilio_sid, auth_token)

    contact_directory = {
        'dad': contacts.dad,
        'mom': contacts.mom
    }

    for key, value in contact_directory.items():
        whatsapp_client.messages.create(
            body='good morning {} !'.format(key),
            from_='whatsapp:+14155238886',
            to='whatsapp:' + value)
