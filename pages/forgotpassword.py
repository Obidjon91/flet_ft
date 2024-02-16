from flet import *

from utils.colors import blue
from utils.validation import Validator


class ForgotPassword(Container):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.bgcolor = blue
        self.alignment = alignment.center
        self.validator = Validator()
        self.error = border.all(width=1, color='red')
        self.email_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, left=20, right=20
                ),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Enter email address...',
                cursor_color='858796',
                text_style=TextStyle(size=14, color='black'),
            ),
            border=border.all(width=1, color='#bdcbf4'),
            border_radius=30
        )

        self.content = Column(
            alignment='center',
            horizontal_alignment='center',
            controls=[
                Container(
                    width=500,
                    border_radius=12,
                    padding=40,
                    bgcolor='white',
                    content=Column(
                        alignment='center',
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value='Forgot Your Password?',
                                size=20,
                                color='black',
                                text_align='center'
                            ),
                            Text(
                                value='Enter your email address and we will send you a link to reset your password.',
                                size=16,
                                color='#858796',
                                text_align='center'
                            ),
                            Container(height=0),
                            self.email_box,
                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(
                                    value='Reset Password',
                                ),
                                on_click=self.reset_password
                            ),
                            Container(height=20),

                            Container(
                                content=Text(
                                    value='Create an Account!',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda e: page.go('/signup')
                            ),
                            Container(
                                content=Text(
                                    value='Already have an account?',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda e: page.go('/login')
                            ),
                        ]
                    )
                )
            ]
        )

    def reset_password(self, e):
        if not self.validator.is_validate_email(self.email_box.content.value):
            self.email_box.border = self.error
            self.email_box.update()
