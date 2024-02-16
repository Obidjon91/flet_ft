from flet import * 
from utils.colors import *



class Login(Container):
    def __init__(self, page: Page):
        
        super().__init__()
        self.alignment = alignment.center
        self.expand = True
        self.bgcolor = blue
        # self.border_radius = border_radius=10
        
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
        
        self.password_box = Container(
            content=TextField(
                border=InputBorder.NONE,
                content_padding=padding.only(
                    top=0, bottom=0, left=20, right=20
                ),
                hint_style=TextStyle(
                    size=12, color='#858796'
                ),
                hint_text='Password...',
                cursor_color='858796',
                text_style=TextStyle(size=14, color='black'),
                password=True,
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
                    padding=40,
                    bgcolor='white',
                    border_radius=20,
                    content=Column(
                        
                        horizontal_alignment='center',
                        controls=[
                            Text(
                                value='Welcome',
                                size=16,
                                color='black',
                                text_align='center',
                            ),
                            self.email_box,
                            self.password_box,
                            
                            Container(height=0),
                            
                            Container(
                                alignment=alignment.center,
                                bgcolor='#4e73df',
                                height=40,
                                border_radius=30,
                                content=Text(value='Login'),
                                on_click=self.login    
                            ),
                            

                            Container(
                                content=Text(
                                    value='Forgot password?',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/forgotpassword')
                            ),
                            
                            Container(
                                content=Text(
                                    value='Create new Account',
                                    color='#4e73df',
                                    size=12
                                ),
                                on_click=lambda _: self.page.go('/forgotpassword')
                            ),
                            

                        
                        ]
                        
                        
                    )
                ),
            ]
        )
    
    def login(self, e):
        pass
    