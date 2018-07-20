# coding: utf-8

from .exceptions import UnableToLoadPageException
from .wait import CustomWebDriverWait


def ensure_on_page(inner):
    def wrapper(page, *args, **kwargs):
        for _ in range(2):
            if page.driver.current_url.startswith(page.page_url):
                break
            page.driver.get(page.page_url)
        else:
            raise UnableToLoadPageException(page.page_url)
        return inner(page, *args, **kwargs)
    return wrapper


def detect_captcha(inner):
    def wrapper(page, *args, **kwargs):
        page.handle_captcha()
        return inner(page, *args, **kwargs)
    return wrapper
