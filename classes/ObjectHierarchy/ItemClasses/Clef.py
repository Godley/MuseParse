
__author__ = 'charlotte'
clef_type = {"GG": "GG",
             "TENORG": "tenorG",
             "C": "C",
             "F": "F",
             "G2": "treble",
             "G1": "french",
             "F4": "bass",
             "F3": "varbaritone",
             "F5": "subbass",
             "C3": "alto",
             "PERCUSSION": "percussion",
             "C4": "tenor",
             "C5": "baritone",
             "C2": "mezzosoprano",
             "C1": "soprano",
             "VARC": "varC",
             "VARC3": "altovarC",
             "VARC4": "tenorvarC",
             "VARC5": "baritonevarC"}


class Clef(object):

    def __init__(self, **kwargs):
        if "sign" in kwargs:
            self.sign = kwargs["sign"]
        else:
            self.sign = None

        if "line" in kwargs:
            self.line = kwargs["line"]
        else:
            self.line = None
        if "octave_change" in kwargs:
            self.octave_change = kwargs["octave_change"]

    def __str__(self):
        name = ""
        index = self.sign + str(self.line)
        if index in clef_type:
            name = clef_type[index]
        else:
            name += index
        if hasattr(self, "octave_change") and self.octave_change is not None:
            name += "shifted " + str(self.octave_change) + " octave(s)"
        return name

    def toLily(self):
        val = "\clef "
        clef = ""
        if hasattr(self, "sign") and self.sign is not None:
            key = self.sign.upper()
            if key == "TAB":
                return "\clef moderntab"
            if hasattr(self, "line") and self.line is not None:
                key += str(self.line)
            if key in clef_type:
                clef = clef_type[key]
            else:
                val = ""
        else:
            val = ""
        if hasattr(self, "octave_change") and self.octave_change is not None:
            options = {1: "^8", 2: "^15", -1: "_8", -2: "_15"}
            if self.octave_change in options:
                clef = "\"" + clef + options[self.octave_change] + "\""
        val += clef
        return val
