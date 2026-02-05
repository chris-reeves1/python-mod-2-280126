class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def get_password_rating(self):
        has_upper = False
        has_lower= False
        has_number = False
        has_special= False

        for x in self.password:
            if x.isupper():
                has_upper = True
            if x.islower():
                has_lower = True
            if x.isnumeric():
                has_number = True
            if x.isalnum():
                has_special = True
            
        
        common_passwords = ["qwerty", "password", "1234", "admin"]
        if self.password in common_passwords:
            return "very weak"

        if len(self.password) < 12:
            return "very weak"
        elif len(self.password) < 16 and (not has_upper or not has_number or not has_special):
            return "weak"
        elif len(self.password) < 16 and has_upper and has_number:
            return "strong"
        elif len(self.password) > 16:
            return "very strong"
        else:
            return "moderate"