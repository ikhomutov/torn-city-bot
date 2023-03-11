from selenium.webdriver.support import expected_conditions

from tornbot.pages.base import locators
from tornbot.wait import CustomWebDriverWait

from .base import BaseCaptchaSolver


class DummyCaptchaSolver(BaseCaptchaSolver):
    """Не решает каптчу, а ждет когда ее решат."""

    def solve(self):
        CustomWebDriverWait(self.driver, 0).infinite_until(
            expected_conditions.invisibility_of_element_located(locators.CAPTCHA)
        )
