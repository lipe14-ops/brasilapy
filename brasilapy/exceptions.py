class ProcessorException(Exception):
    def __init__(
        self,
        status_code: int,
        response_text: str,
        message: str = "A problem occured when processing your request",
    ):
        self.status_code = status_code
        self.response_text = response_text
        self.message = message

    def __str__(self):
        return f"STATUS_CODE: {self.status_code} - {self.response_text}"
