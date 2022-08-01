class ApiError(Exception):
    code = 500
    message = ""

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
