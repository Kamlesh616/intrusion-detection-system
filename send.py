from twilio.rest import Client

account_sid = 'your_actual_account_sid'
auth_token = 'your_actual_auth_token'
client = Client(account_sid, auth_token)

def sendSms(image_path):
    # Ensure you replace 'your_image_url' with the actual URL where your image is hosted.
    image_url = f'https://your-server.com/{image_path}'

    message = client.messages.create(
        from_='+15076657219',
        body='Alert! Image of the detected intrusion is attached.',
        media_url=image_url,  # URL of the image to be sent
        to='+919021356110'
    )

    print(message.sid)