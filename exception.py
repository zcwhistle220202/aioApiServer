# -*- coding:utf-8 -*-

class warningException(Exception,):
    """Exception raised for custom warning"""
    def __init__(self, status_code: int = 0, message: str = '', data: dict = {},) -> None:
        self.status_code = status_code

        self.message = message

        self.data = data

class finishException(Exception,):
    """Exception raised for custom finish"""
    def __init__(self, status_code: int = 0, message: str = '', data: dict = {},) -> None:
        self.status_code = status_code

        self.message = message

        self.data = data