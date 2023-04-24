from django.utils.text import slugify

import string
import random


def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))

    return res



allowed_chars = ''.join((string.ascii_letters, string.digits))
unique_id = ''.join(random.choice(allowed_chars) for _ in range(5))


def generate_slug(text):
    new_slug = slugify(text)
    from home.models import BlogModel                # ye circuler import k karan yaha import karana pada 
    if BlogModel.objects.filter(slug = new_slug).first():
        # return generate_slug(text + generate_random_string(5))
        return generate_slug(text + unique_id)         # but abhi bhi random number add ho k nahi aa rha hai
    return new_slug



from django.conf import settings
from django.core.mail import send_mail


# def send_mail_to_user(token, email):
#     subject = f"Your accounts need to be verified"
#     message = f"paste the link link to verify account http://127.0.0.1:8000/verify/{token}"
#     email_form = settings.EMAIL_HOST_USER
#     recipient_list = [email] 
#     send_mail(subject, message, email_form, recipient_list)
#     return True