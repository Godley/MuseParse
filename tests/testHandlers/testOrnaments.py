from museparse.tests.testHandlers.testHandleNotesAndPitches import notes
from museparse.classes.ObjectHierarchy.ItemClasses import Note, Ornaments
from museparse.classes.Input import MxmlParser


class testArpeggiates(notes):

    def setUp(self):
        notes.setUp(self)
        self.handler = MxmlParser.HandleArpeggiates
        self.data = {}
        self.data["note"] = Note.Note()

    def testArpeggiate(self):
        self.tags.append("arpeggiate")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "wrap"), Note.Arpeggiate)

    def testArpeggiateDirection(self):
        self.tags.append("arpeggiate")
        self.attrs["arpeggiate"] = {"direction": "down"}
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertTrue(
            hasattr(self.data["note"].GetNotation(-1, "wrap"), "direction"))
        self.assertEqual("down", self.data[
                         "note"].GetNotation(-1, "wrap").direction)

    def testNonArpeggiate(self):
        self.tags.append("non-arpeggiate")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "wrap"), Note.NonArpeggiate)

    def testNonArpeggiateType(self):
        self.tags.append("non-arpeggiate")
        self.attrs["non-arpeggiate"] = {"type": "bottom"}
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertTrue(
            hasattr(self.data["note"].GetNotation(-1, "wrap"), "type"))
        self.assertEqual("bottom", self.data[
                         "note"].GetNotation(-1, "wrap").type)


class testSlides(notes):

    def setUp(self):
        notes.setUp(self)
        self.instance = Note.Slide
        self.handler = MxmlParser.HandleSlidesAndGliss
        self.tags.append("slide")

        self.notation_type = "post"
        self.data = {}
        self.data["note"] = Note.Note()

    def testSlide(self):
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, self.notation_type), self.instance)

    def testSlideType(self):
        self.attrs[self.tags[-1]] = {"type": "start"}
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertTrue(
            hasattr(self.data["note"].GetNotation(-1, self.notation_type), "type"))
        self.assertEqual("start",
                         self.data["note"].GetNotation(-1,
                                                       self.notation_type).type)

    def testSlideLineType(self):
        self.attrs[self.tags[-1]] = {"line-type": "solid"}
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.notation_type = "wrap"
        self.assertTrue(
            hasattr(self.data["note"].GetNotation(-1, self.notation_type), "lineType"))
        self.assertEqual("solid",
                         self.data["note"].GetNotation(-1,
                                                       self.notation_type).lineType)

    def testSlideNumber(self):
        self.attrs[self.tags[-1]] = {"number": "1"}
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)

        self.assertTrue(
            hasattr(self.data["note"].GetNotation(-1, self.notation_type), "number"))
        self.assertEqual(1,
                         self.data["note"].GetNotation(-1,
                                                       self.notation_type).number)


class testGliss(testSlides):

    def setUp(self):
        testSlides.setUp(self)
        self.tags.remove("slide")
        self.tags.append("glissando")
        self.data["note"] = Note.Note()
        self.instance = Note.Glissando
        self.notation_type = "wrap"


class testOrnaments(notes):

    def setUp(self):
        notes.setUp(self)
        self.handler = MxmlParser.handleOrnaments
        self.data["note"] = Note.Note()
        self.tags.append("ornaments")

    def testIMordent(self):
        self.tags.append("inverted-mordent")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "post"), Ornaments.InvertedMordent)

    def testMordent(self):
        self.tags.append("mordent")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "post"), Ornaments.Mordent)

    def testTrill(self):
        self.tags.append("trill-mark")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "post"), Ornaments.Trill)

    def testTrillWithLine(self):
        self.tags.append("wavy-line")
        self.attrs["wavy-line"] = {"type": "start"}
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertEqual(
            self.data["note"].GetNotation(-1, "post").line, "start")

    def testTurn(self):
        self.tags.append("turn")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "post"), Ornaments.Turn)

    def testInvertedTurn(self):
        self.tags.append("inverted-turn")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "post"), Ornaments.InvertedTurn)

    def testTremolo(self):
        self.tags.append("tremolo")
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertIsInstance(
            self.data["note"].GetNotation(-1, "pre"), Ornaments.Tremolo)

    def testTremoloType(self):
        self.tags.append("tremolo")
        self.attrs["tremolo"] = {"type": "single"}
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertEqual("single", self.data[
                         "note"].GetNotation(-1, "pre").type)

    def testTremoloValue(self):
        self.tags.append("tremolo")
        self.chars["tremolo"] = "1"
        self.handler(self.tags, self.attrs, self.chars, self.piece, self.data)
        self.assertEqual(1, self.data["note"].GetNotation(-1, "pre").value)
