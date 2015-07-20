import math

from MuseParse.classes.ObjectHierarchy.ItemClasses import BaseClass, Mark, Ornaments


class Tie(BaseClass.Base):

    def __init__(self, type):
        if type is not None:
            self.type = type

    def toLily(self):
        lily = ""
        if hasattr(self, "type"):
            if self.type == "start":
                lily = "~"
        return lily


class Notehead(BaseClass.Base):

    def __init__(self, filled=False, type=""):
        self.filled = filled
        self.type = type

    def toLily(self):
        pre_note = "\n\\tweak #'style #'"
        if self.type != "":
            ignore = [
                "slashed",
                "back slashed",
                "inverted triangle",
                "arrow up",
                "arrow down",
                "normal"]
            if self.type == "diamond":
                val = "\\harmonic"
                return [val]
            if self.type == "x":
                val = "\\xNote"
                return [val, ""]
            options = {
                "diamond": "harmonic",
                "x": "cross",
                "circle-x": "xcircle"}
            if self.type in options:
                pre_note += options[self.type]
            elif self.type not in ignore:
                pre_note += self.type
            if self.type in ignore:
                pre_note = ""
                val = ""
        else:
            pre_note = ""

        return [pre_note + "\n", ""]


class Stem(BaseClass.Base):

    def __init__(self, type):
        if type is not None:
            self.type = type
        BaseClass.Base.__init__(self)

    def __str__(self):
        return self.type

    def toLily(self):
        val = "\n\stem"
        if not hasattr(self, "type"):
            val += "Neutral"
        else:
            val += self.type[0].upper() + self.type[1:len(self.type)]
        return val


class Pitch(BaseClass.Base):

    def __init__(self, **kwargs):
        if "alter" in kwargs:
            self.alter = kwargs["alter"]
        if "octave" in kwargs:
            self.octave = int(kwargs["octave"])
        if "step" in kwargs:
            self.step = kwargs["step"]
        if "accidental" in kwargs:
            self.accidental = kwargs["accidental"]
        if "unpitched" in kwargs:
            self.unpitched = True
        BaseClass.Base.__init__(self)

    def __str__(self):
        st = ""
        alter = {1: "sharp", -
                 1: "flat", 0: "", 2: "double-sharp", -
                 2: "double-flat"}
        if hasattr(self, "unpitched"):
            st += "unpitched"
        if hasattr(self, "step"):
            st += self.step

        if hasattr(self, "alter"):
            st += alter[int(self.alter)]
        if hasattr(self, "accidental"):
            st += "(" + self.accidental + ")"
        if hasattr(self, "octave"):
            st += self.octave
        return st

    def toLily(self):
        val = ""
        if not hasattr(self, "step"):
            val += "c"
        else:
            val += self.step.lower()
        if hasattr(self, "alter"):
            if self.alter == 1:
                val += "is"
            elif self.alter == -1:
                val += "es"
        if hasattr(self, "accidental"):
            names = {
                "three-quarters-sharp": "isih",
                "three-quarters-flat": "eseh",
                "quarter-sharp": "ih",
                "quarter-flat": "eh",
                "flat-flat": "eses",
                "double-sharp": "isis"}
            if self.accidental in names:
                val += names[self.accidental]
        if not hasattr(self, "octave"):
            val += "'"
        else:
            oct = int(self.octave)
            if oct > 3:
                for i in range(oct - 3):
                    val += "'"
            elif oct < 3:
                counter = 3 - oct
                while counter != 0:
                    val += ","
                    counter -= 1

        return val


class Note(BaseClass.Base):

    def __init__(self, **kwargs):
        BaseClass.Base.__init__(self)
        self.ties = []
        self.beams = {}
        if "rest" in kwargs:
            self.rest = kwargs["rest"]
        else:
            self.rest = False
        if "dots" in kwargs:
            self.dots = kwargs["dots"]
        else:
            self.dots = 0
        if "pitch" in kwargs:
            self.pitch = kwargs["pitch"]
        if "chord" in kwargs and kwargs["chord"] is not None:
            self.chord = kwargs["chord"]
        if "type" in kwargs and kwargs["type"] is not None:
            self.SetType(kwargs["type"])
        elif "duration" in kwargs:
            self.duration = kwargs["duration"]
        if "divisions" in kwargs and kwargs["divisions"] is not None:
            self.divisions = float(kwargs["divisions"])
        self.prenotation = []
        self.wrap_notation = []
        self.postnotation = []
        self.closing_notation = []
        self.has_tremolo = False

    def AddSlur(self, item):
        if not hasattr(self, "slurs"):
            self.slurs = []
        self.slurs.append(item)

    def GetAllNotation(self):
        return self.prenotation, self.wrap_notation, self.postnotation

    def GetNotation(self, id, type):
        if type == "post":
            if (id == -
                1 and len(self.postnotation) > 0) or (id != -
                                                      1 and len(self.postnotation) > id):
                return self.postnotation[id]
        if type == "pre":
            if (id == -
                1 and len(self.prenotation) > 0) or (id != -
                                                     1 and len(self.postnotation) > id):
                return self.prenotation[id]
        if type == "wrap":
            if (id == -
                1 and len(self.wrap_notation) > 0) or (id != -
                                                       1 and len(self.postnotation) > id):
                return self.wrap_notation[id]

    def FlushNotation(self):
        self.prenotation = []
        self.wrap_notation = []
        self.postnotation = []
        self.closing_notation = []

    def GetClosingNotationLilies(self):
        lstring = ""
        for notation in self.closing_notation:
            result = notation.toLily()
            if type(result) == list:
                result = "".join(result)
            lstring += result
        return lstring

    def addNotation(self, obj):
        add = True
        wrap_notation = [
            Arpeggiate,
            NonArpeggiate,
            Slide,
            Glissando,
            Mark.Caesura,
            Mark.BreathMark,
            GraceNote]
        # method to handle addition of notation: done here to avoid repetitive
        # code in main parser
        if isinstance(obj, Ornaments.Tremolo) or isinstance(obj, Tuplet):
            if isinstance(obj, Ornaments.Tremolo):
                options = {1: 2, 2: 4, 3: 8}
                if hasattr(obj, "value"):
                    self.trem_length = options[obj.value]
            if hasattr(obj, "type"):
                if isinstance(obj, Ornaments.Tremolo) and obj.type != "single":
                    self.trem_length *= 2
                if obj.type == "stop":
                    self.closing_notation.append(obj)
                else:
                    self.prenotation.append(obj)
                return
            else:
                self.prenotation.append(obj)
                return
        if type(obj) in wrap_notation:
            if type(obj) == Slide and not hasattr(obj, "lineType"):
                self.postnotation.append(obj)
                return
            else:
                self.wrap_notation.append(obj)
                return
        if hasattr(obj, "type") and len(self.postnotation) > 0:
            duplicate_check = [
                True for thing in self.postnotation if hasattr(
                    thing,
                    "type") and thing.type == obj.type]
            if len(duplicate_check) > 0:
                add = False
        if len(self.postnotation) == 0 or add:
            self.postnotation.append(obj)

    def SetType(self, vtype):
        self.val_type = vtype
        options = {
            "128th": 128,
            "64th": 64,
            "32nd": 32,
            "16th": 16,
            "eighth": 8,
            "quarter": 4,
            "half": 2,
            "whole": 1,
            "h": 8,
            "long": "\\longa",
            "breve": "\\breve"}
        if vtype in options:
            self.duration = options[self.val_type]

    def CheckDivisions(self, measure_div):
        if hasattr(self, "val_type"):
            self.divisions = 1
        else:
            self.divisions = measure_div

    def __str__(self):
        if hasattr(self, "divisions") and hasattr(self, "duration"):
            self.duration = self.duration / self.divisions
        st = BaseClass.Base.__str__(self)
        return st

    def addDot(self):
        self.dots += 1

    def handlePreLilies(self):
        val = ""
        if hasattr(self, "chord"):
            if self.chord == "start":
                val += "<"
        if hasattr(self, "grace"):
            val += self.grace.toLily() + " "
        tuplet = self.Search(Tuplet, 1)
        if tuplet is None and hasattr(self, "timeMod") and self.timeMod.first:
            val += "\once \override TupletBracket.bracket-visibility = ##f\n"
            val += "\omit TupletNumber\n"
            val += "\\tuplet " + self.timeMod.toLily() + " {"
        for item in self.prenotation:
            lilystring = item.toLily()
            if isinstance(item, Tuplet):
                if hasattr(self, "timeMod"):
                    lilystring += " " + self.timeMod.toLily()
                    lilystring += " {"

            if isinstance(item, Ornaments.Tremolo):
                if not hasattr(self, "trem_length"):
                    self.trem_length = lilystring[1]
                    lilystring = lilystring[0]
            val += lilystring

        return val

    def GetBeams(self):
        if hasattr(self, "beams"):
            return self.beams

    def getLilyDuration(self):
        # method to calculate duration of note in lilypond duration style
        value = ""
        if not hasattr(self, "val_type"):
            if hasattr(self, "duration") and self.duration is not None:
                value = (self.duration / self.divisions)
                value = (1 / value)
                value *= 4

                if value >= 1:
                    if math.ceil(value) == value:
                        if hasattr(self, "trem_length"):
                            value *= self.trem_length
                        value = int(value)

                    else:
                        rounded = math.ceil(value)
                        if hasattr(self, "trem_length"):
                            rounded *= self.trem_length
                        value = int(rounded)
                else:
                    if value == 0.5:
                        value = "\\breve"
                    if value == 0.25:
                        value = "\longa"
        else:
            value = self.duration
            if hasattr(self, "trem_length"):
                value *= self.trem_length
        if type(value) is not str:
            value = int(value)
        if value != "":
            value = str(value)
        return value

    def addBeam(self, id, beam):
        if not hasattr(self, "beams"):
            self.beams = {}
        result = [True for b in self.beams if self.beams[b].type == beam.type]
        if len(result) < 1:
            self.beams[id] = beam

    def AddTie(self, type):
        add = True
        for tie in self.ties:
            if tie.type == type:
                add = False
                break
        if add:
            self.ties.append(Tie(type))

    def toLily(self):
        val = ""
        value = ""
        if hasattr(self, "print") and not self.print:
            val += "\n\\hideNotes\n"
        val += self.handlePreLilies()
        if hasattr(self, "pitch") and not self.rest:
            val += self.pitch.toLily()

        if self.rest:
            if not hasattr(self, "MeasureRest") or not self.MeasureRest:
                val += "r"
        if hasattr(
                self,
                "duration") and (
                not hasattr(
                self,
                "MeasureRest") or not self.MeasureRest):
            if not hasattr(self, "chord"):
                val += self.getLilyDuration()
                for dot in range(self.dots):
                    val += "."
        val += self.handlePostLilies()
        value = self.LilyWrap(val)
        if hasattr(self, "print"):
            value += "\n\\unHideNotes"
        if hasattr(self, "close_timemod") and self.close_timemod:
            value += "}"
        return value

    def LilyWrap(self, value):
        prefixes = ""
        wrapped_notation_lilystrings = [
            wrap.toLily() for wrap in self.wrap_notation]
        if hasattr(self, "notehead"):
            wrapped_notation_lilystrings.append(self.notehead.toLily())

        prefixes += "".join([wrapper[0] +
                             " " for wrapper in wrapped_notation_lilystrings if wrapper is not None and len(wrapper) > 1])
        prefixes_and_current = prefixes + value
        postfixes = "".join(
            [wrapper[-1] for wrapper in wrapped_notation_lilystrings if wrapper is not None and len(wrapper) > 0])
        lilystring = prefixes_and_current + postfixes
        return lilystring

    def handlePostLilies(self):
        val = ""
        if hasattr(self, "chord") and self.chord == "stop":
            val += ">"
            val += self.getLilyDuration()
            for dot in range(self.dots):
                val += "."
        if not hasattr(self, "chord") or self.chord == "stop":
            if hasattr(
                self,
                "beams") and (
                not hasattr(
                    self,
                    "autoBeam") or not self.autoBeam):
                val += "".join([self.beams[beam].toLily()
                                for beam in self.beams])
            if hasattr(self, "slurs"):
                val += "".join([slur.toLily() for slur in self.slurs])
            val += "".join([tie.toLily() for tie in self.ties])
        val += "".join([value.toLily()
                        for value in self.postnotation if type(value.toLily()) is str])
        val += "".join([value.toLily()[0] for value in self.postnotation if type(
            value.toLily()) is list and len(value.toLily()) > 0])

        return val

    def Search(self, cls_type, list_id=-1):
        options = {
            "pre": self.prenotation,
            "post": self.postnotation,
            "wrap": self.wrap_notation}
        if list_id in options:
            for item in options[list_id]:
                if type(item) == cls_type:
                    return item
        else:
            for item in self.prenotation:
                if type(item) == cls_type:
                    return item
            for item in self.wrap_notation:
                if item.__class__.__name__ == cls_type.__name__:
                    return item
                else:
                    print(item.__class__.__name__, cls_type.__name__)
            for item in self.postnotation:
                if type(item) == cls_type:
                    return item


class Tuplet(BaseClass.Base):

    def __init__(self, **kwargs):
        if "type" in kwargs:
            if kwargs["type"] is not None:
                self.type = kwargs["type"]
        if "bracket" in kwargs:
            if kwargs["bracket"] is not None:
                self.bracket = kwargs["bracket"]
        BaseClass.Base.__init__(self)

    def toLily(self):
        val = ""
        if hasattr(self, "bracket"):
            if self.bracket:
                val += "\once \override TupletBracket.bracket-visibility = ##t\n"
            else:
                val += "\once \override TupletBracket.bracket-visibility = ##f\n"
        val += "\\tuplet"
        val = val
        if hasattr(self, "type"):
            if self.type == "stop":
                val = "}"
        return val


class GraceNote(BaseClass.Base):

    def __init__(self, **kwargs):
        if "slash" in kwargs:
            self.slash = kwargs["slash"]
        if "first" in kwargs and kwargs["first"] is not None:
            self.first = kwargs["first"]
        BaseClass.Base.__init__(self)

    def toLily(self):
        val = "\grace"
        ending = ""
        if hasattr(self, "slash") and self.slash:
            val = "\slashedGrace"
        if hasattr(self, "first") and self.first:
            val += " {"
        else:
            val = ""
        if hasattr(self, "last") and self.last:
            ending = " }"
            if not hasattr(self, "first") or not self.first:
                return ending
        return [val, ending]


class TimeModifier(BaseClass.Base):

    def __init__(self, **kwargs):
        BaseClass.Base.__init__(self)
        self.first = False
        if "first" in kwargs and kwargs["first"] is not None:
            self.first = kwargs["first"]
        if "normal" in kwargs:
            self.normal = kwargs["normal"]
        if "actual" in kwargs:
            self.actual = kwargs["actual"]

    def toLily(self):
        val = ""
        if hasattr(self, "actual"):
            val += str(self.actual)
        val += "/"
        if hasattr(self, "normal"):
            val += str(self.normal)
        return val


class Arpeggiate(BaseClass.Base):

    def __init__(self, **kwargs):
        self.wrapped = True
        BaseClass.Base.__init__(self)
        if "direction" in kwargs:
            self.direction = kwargs["direction"]
        if "type" in kwargs:
            self.type = kwargs["type"]
        else:
            self.type = "none"

    def toLily(self):
        var = "\\arpeggio"
        if not hasattr(self, "direction") or self.direction is None:
            var += "Normal"
        else:
            var += "Arrow" + self.direction.capitalize()
        if self.type == "start":
            return [var, ""]
        if self.type == "stop":
            return ["", "\\arpeggio"]
        if self.type == "none":
            return [""]


class Slide(BaseClass.Base):

    def __init__(self, **kwargs):
        self.wrapped = True
        BaseClass.Base.__init__(self)
        if "type" in kwargs:
            if kwargs["type"] is not None:
                self.type = kwargs["type"]
        if "lineType" in kwargs:
            if kwargs["lineType"] is not None:
                self.lineType = kwargs["lineType"]
        if "number" in kwargs:
            if kwargs["number"] is not None:
                self.number = kwargs["number"]

    def toLily(self):
        val = ""
        gliss = "\glissando"
        values = []
        if hasattr(self, "lineType"):
            if self.lineType == "wavy":
                val += "\override Glissando.style = #'zigzag"
                values.append(val)
        if hasattr(self, "type"):
            if self.type == "stop":
                values = []
            else:
                values.append(gliss)
        else:
            values.append(gliss)
        return values


class Glissando(Slide):

    def toLily(self):
        self.lineType = "wavy"
        vals = Slide.toLily(self)
        return vals


class NonArpeggiate(Arpeggiate):

    def __init__(self, **kwargs):

        Arpeggiate.__init__(self)
        if "type" in kwargs:
            self.type = kwargs["type"]

    def toLily(self):
        if self.type == "start":
            return ["\\arpeggioBracket", ""]
        if self.type == "stop":
            return ["", "\\arpeggio"]
        if self.type == "none":
            return [""]


class Beam(Stem):

    def toLily(self):
        val = ""
        if hasattr(self, "type"):
            if self.type == "begin":
                val = "["
            elif self.type == "end":
                val = "]"
        return val
