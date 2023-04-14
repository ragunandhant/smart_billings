import pywhatkit
from pywhatkit.whats import sendwhatmsg_instantly,sendwhats_image
# Phone number (including country code) and message
def sendMessage(phone):
    try:
        phone_num = "+91 "+phone
        message = "Enjoy your meals"
        image_path = "F:\smart_billing_try\media\images\qr.png"
            # Send the message with the image immediately\
        sendwhats_image(phone_num,image_path,tab_close=True,caption="*Our chef has prepared a special dish for you today. Enjoy!*",close_time=100
                        )
        return True
    except Exception:
        return False