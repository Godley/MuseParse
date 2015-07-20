from MuseParse.classes.ObjectHierarchy.ItemClasses import BaseClass


class Barline(BaseClass.Base):

    def __init__(self, **kwargs):
        if "style" in kwargs:
            if kwargs["style"] is not None:
                self.style = kwargs["style"]
        if "repeat" in kwargs:
            if kwargs["repeat"] is not None:
                self.repeat = kwargs["repeat"]
        if "ending" in kwargs:
            if kwargs["ending"] is not None:
                self.ending = kwargs["ending"]
        if "repeatNum" in kwargs:
            if kwargs["repeatNum"] is not None:
                self.repeatNum = kwargs["repeatNum"]
            else:
                self.repeatNum = 2
        else:
            self.repeatNum = 2
        BaseClass.Base.__init__(self)

    def toLily(self):
        lilystring = ""
        if not hasattr(self, "ending") and not hasattr(self, "repeat"):
            lilystring += " \\bar \""
            if hasattr(self, "style"):
                options = {
                    "light-light": "||",
                    "heavy-light": ".|",
                    "light-heavy": "|.",
                    "heavy-heavy": "..",
                    "dotted": ";",
                    "dashed": "!",
                    "none": "",
                    "tick": "'"}
                if self.style in options:
                    lilystring += options[self.style]
                else:
                    lilystring += "|"
                lilystring += "\""
            else:
                lilystring += "\""
        else:

            if hasattr(self, "repeat"):
                if self.repeat == "forward":
                    lilystring = " \\repeat volta " + \
                        str(self.repeatNum) + " {"
                if self.repeat == "backward" and not hasattr(self, "ending"):
                    lilystring += "}"
                if self.repeat == "forward-barline":
                    lilystring = " \\bar \".|:\""
                if self.repeat == "backward-barline":
                    lilystring = " \\bar \":|.\""
                if self.repeat == "backward-barline-double":
                    lilystring = " \\bar \":|.|:\""
            if hasattr(self, "ending"):
                lilystring += self.ending.toLily()

        return lilystring


class EndingMark(BaseClass.Base):

    def __init__(self, **kwargs):
        if "number" in kwargs:
            self.number = kwargs["number"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        BaseClass.Base.__init__(self)

    def toLily(self):
        lilystring = ""
        if hasattr(self, "number"):
            if self.number == 1:
                lilystring = "\\alternative {\n"

        else:
            lilystring = "\\alternative {"
        if not hasattr(
                self,
                "type") or (
                self.type != "discontinue" and self.type != "stop"):
            lilystring += "{"
        if hasattr(self, "type"):
            if self.type == "stop":
                lilystring = "}"
            if self.type == "discontinue":
                lilystring = "}\n}"
        return lilystring


class Transposition(BaseClass.Base):

    def __init__(self, **kwargs):
        BaseClass.Base.__init__(self)
        if "diatonic" in kwargs:
            self.diatonic = kwargs["diatonic"]
        if "chromatic" in kwargs:
            self.chromatic = kwargs["chromatic"]
        if "octave" in kwargs:
            self.octave = kwargs["octave"]
