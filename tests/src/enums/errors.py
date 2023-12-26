from enum import Enum


class ErrorMessages(Enum):

    WRONG_ANSWER = "The result does not match the expected one"
    INSTABILITY = "The result should not depend on the order of the input data"
    NON_UNIQUE = "The values are repeated"
    DEFORM_VALUE = "The values are distorted"
    WRONG_ORDER = "The order is incorrect"
    WRONG_STATUS_CODE = "Received status code is not equal to expected"
    FOLDER_NOT_FOUND = "Path dont exists"
    FOLDER_EXIST = "Path already exist"