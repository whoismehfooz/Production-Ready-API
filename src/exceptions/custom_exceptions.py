



class UserNotFoundException(Exception):
    def __init__(self):
        self.message = "User not found"
        super().__init__(self.message)
        

class UserAlreadyExistsException(Exception):
    def __init__(self):
        self.message = "User already exists"
        super().__init__(self.message)

class InvalidCredentialsException(Exception):
    def __init__(self):
        self.message = "Invalid credentials"
        super().__init__(self.message)

class InvalidTokenException(Exception):
    def __init__(self):
        self.message = "Invalid Token"
        super().__init__(self.message)