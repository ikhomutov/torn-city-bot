# coding: utf-8


class UnableToLoadPageException(Exception):
    def __init__(self, page_url):
        message = 'Cannot load page: %s' % page_url
        super().__init__(message)


CAPTCHA_MESSAGE = 'Captcha detected. Please solve it and start the bot again'

class CaptchaDetectedException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(CAPTCHA_MESSAGE, *args, **kwargs)
