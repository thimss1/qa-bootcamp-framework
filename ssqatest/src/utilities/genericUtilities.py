
import logging as logger
import random
import string
from html.parser import HTMLParser


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password.")

    if not domain:
        domain = 'supersqa.com'
    if not email_prefix:
        email_prefix = 'testuser'

    random_email_sting_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_sting_length))

    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20
    password_string = ''.join(random.choices(string.ascii_letters, k=password_length))

    random_info = {'email': email, 'password': password_string}
    logger.debug(f"Randomly generated email and password: {random_info}")

    return random_info

def generate_random_string(length=10, prefix=None, suffix=None):

    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))

    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = random_string + suffix

    return random_string

def generate_random_coupon_code(sufix=None, length=10):

    code = ''.join(random.choices(string.ascii_uppercase, k=length))
    if sufix:
        code += sufix

    return code

def convert_html_to_text(input_html_string):
    # define a class used to convert html to text
    class HTMLFilter(HTMLParser):
        text = ""

        def handle_data(self, data):
            self.text += data

    f = HTMLFilter()
    f.feed(input_html_string)
    return f.text
