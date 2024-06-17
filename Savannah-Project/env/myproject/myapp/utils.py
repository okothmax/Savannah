# myapp/utils.py
import africastalking

africastalking.initialize('YOUR_USERNAME', 'YOUR_API_KEY')
sms = africastalking.SMS

def send_sms_notification(phone_number, message):
    response = sms.send(message, [phone_number])
    print(response)
