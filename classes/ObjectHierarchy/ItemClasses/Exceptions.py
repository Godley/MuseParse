class NoScorePartException(BaseException):

    """ERROR! NO SCORE PART ID FOUND"""


class NoPartCreatedException(BaseException):

    """ERROR! PART NOT CREATED"""


class NoMeasureIDException(BaseException):

    """ERROR! NO MEASURE FOUND"""


class TabNotImplementedException(BaseException):

    """ERROR: this application doesn't care for tab staff"""


class DrumNotImplementedException(BaseException):

    """ERROR: this application doesn't care for drum tab staff"""
