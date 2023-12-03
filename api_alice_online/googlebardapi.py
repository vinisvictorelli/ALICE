from bardapi import BardCookies
import requests
from bardapi import Bard, SESSION_HEADERS

def GoogleBard(question):
    cookie_dict = {
        "__Secure-1PSIDTS": "sidts-CjIBNiGH7syts39dClyn3ETqR7K6mRfimkBlAol0POKORDT-dZzzS4tDoB5Z7k6LesNQyhAA",
        "__Secure-1PAPISID": "6luxqVMqXpenXvQX/Aud4PFNdev5awalnJ",
        "__Secure-1PSID": "dQgC3RABj3ZTHOAfg6mWhCwT3tQLBZAEeUfe_-ma2gx0Dg3TP_UnSo6H6t4jwOahCoUwtA.",
        # Any cookie values you want to pass session object.
    }

    bard = BardCookies(cookie_dict=cookie_dict)
    response = bard.get_answer(question)['content']
    return response
