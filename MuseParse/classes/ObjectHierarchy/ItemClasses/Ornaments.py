from MuseParse.classes.ObjectHierarchy.ItemClasses import BaseClass

"""
The following classes really are just stubs for ornament notations that could probably be merged into 1 class.
"""


class InvertedMordent(BaseClass.Base):

    def toLily(self):
        return "\prall"


class Mordent(BaseClass.Base):

    def toLily(self):
        return "\mordent"


class Trill(BaseClass.Base):

    def toLily(self):
        return "\\trill"


class TrillSpanner(BaseClass.Base):

    def __init__(self, **kwargs):
        BaseClass.Base.__init__(self)
        if "line" in kwargs:
            self.line = kwargs["line"]

    def toLily(self):
        val = ""
        if hasattr(self, "line") and self.line != "":
            val += "\\"
            val += self.line.lower()
            val += "TrillSpan\n"

        return val


class Turn(BaseClass.Base):

    def toLily(self):
        return "\\turn"


class InvertedTurn(BaseClass.Base):

    def toLily(self):
        return "\\reverseturn"


class Tremolo(BaseClass.Base):

    """
    Tremolo class.


    # Optional inputs:

        - type: whether this is a starting or stopping tremolo.

        - value: the number of lines/divisions to put into the note.
    """

    def __init__(self, **kwargs):
        self.preNote = True
        BaseClass.Base.__init__(self)
        if "type" in kwargs:
            if kwargs["type"] is not None:
                self.type = kwargs["type"]

        if "value" in kwargs:
            if kwargs["value"] is not None:
                self.value = kwargs["value"]
        else:
            self.value = 2

    def toLily(self):
        return_val = "\\repeat tremolo "
        num = ""
        if hasattr(self, "value"):
            options = {1: 2, 2: 4, 3: 8}
            num = str(options[self.value])

        if num != "":
            return_val += num + " "
        if hasattr(self, "type"):
            if self.type == "start":
                return_val += "{"
                return_val = return_val
            if self.type == "stop":
                return_val = "}"
                return_val = ["", return_val]

        return return_val
