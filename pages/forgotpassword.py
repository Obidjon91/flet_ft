from flet import * 
from utils.colors import blue


class ForgotPassword(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = blue