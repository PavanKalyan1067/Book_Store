response_code = {
    200: "Success",
    201: "Created",
    202: "Updated",
    203: "Ok",
    300: "Validation error",
    301: "Error occurred while sending activation email",
    302: "User account is verified",
    303: "Email user does not exists",
    304: "Token Expired",
    305: "Error occur while redirecting",
    306: "Insufficient data",
    307: "Invalid Token",
    308: "Password Reset Successfully",
    309: "Password Reset link send. Please check your Email",
    400: "Bad Request",
    401: "Username already exists",
    403: "Password didnt matched",
    404: "Provide valid email",
    405: "Invalid data",
    406: "Please enter alpha numeric, least 8 digit password",
    407: "Token does not exists",
    408: "Email already exists in registered user",
    409: "Does not exists",
    410: "Logout first",
    411: "Verify email first",
    412: "Wrong password",
    413: "Login first",
    414: "Invalid operation",
    415: "Enter upcoming time",
    416: "Something went wrong. Please Try again",
    417: "User Logged out Successfully!!",
    418: "User already Blacklisted",
    419: "Tokens Generated Successfully"
}


class DoesNotExist:
    pass


class CustomExceptions:
    @classmethod
    def CartDoesNotExist(cls, param, param1):
        pass

    @classmethod
    def BookAlreadyExists(cls, param, param1):
        pass


class CartDoesNotExist(CustomExceptions):
    pass
