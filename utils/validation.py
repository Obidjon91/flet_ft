import re


class Validator:
    def __init__(self):
        pass

    def is_correct_name(self, name: str):
        if not isinstance(name, str):
            return None
        if len(name.strip()) < 2:
            return None
        if not all(c.isalpha() or c.isspace() or c in "-'," for c in name):
            return None
        return True
    def is_validate_email(self, email: str):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(pattern, email) is not None
    def is_validate_passwort(self, password: str):
        if not isinstance(password, str):
            return False
        if len(password) < 8:
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not re.search("[@_!#$%^&*()<>?/\|}{~:]", password):
            return False
        return True
