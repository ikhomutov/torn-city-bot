# coding: utf-8


def ensure_on_page(inner):
    def wrapper(page, *args, **kwargs):
        if not page.driver.current_url.startswith(page.page_url):
            page.driver.get(page.page_url)
        return inner(page, *args, **kwargs)
    return wrapper
