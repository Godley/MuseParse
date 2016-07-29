import unittest

from MuseParse.classes.ObjectHierarchy.TreeClasses import BaseTree


class testTree(unittest.TestCase):

    def setUp(self):
        self.item = BaseTree.Tree()

    def testAddNode(self):
        elem = BaseTree.Node()
        self.item.AddNode(elem)
        self.assertEqual(elem, self.item.root)

    def testAddInvalidNode(self):
        elem = BaseTree.Node()
        self.item.AddNode(elem)
        self.assertRaises(
            BaseTree.CannotAddToTreeException,
            self.item.AddNode,
            BaseTree.Node())

    def testAddTwoValidNodes(self):
        elem = BaseTree.Node(rules=[BaseTree.EmptyNode, BaseTree.IndexedNode])
        self.item.AddNode(elem)
        self.item.AddNode(BaseTree.EmptyNode(0))
        self.assertEqual(1, len(elem.children))

    def testAddNodeOverLimit(self):
        elem = BaseTree.Node(
            rules=[
                BaseTree.EmptyNode,
                BaseTree.IndexedNode],
            limit=-1)
        self.item.AddNode(elem)
        self.assertRaises(
            BaseTree.CannotAddToTreeException,
            self.item.AddNode,
            BaseTree.EmptyNode(0))

    def testAddNodeAddsToNextLevel(self):
        # this test confirms that with a parent who allows 1 child which has to be empty or indexed, Next is it's child
        # and third is a child of next.
        elem = BaseTree.Node(
            rules=[
                BaseTree.EmptyNode,
                BaseTree.IndexedNode],
            limit=1)
        next = BaseTree.EmptyNode(0, rules=[BaseTree.Node])
        third = BaseTree.Node()
        self.item.AddNode(elem)
        self.item.AddNode(next)
        self.item.AddNode(third)
        self.assertEqual(next.GetChild(0), third)

    def testAddNodeAddsToNextLevelWithExpandedLimit(self):
        # this test confirms the above still happens when the limit is 2
        elem = BaseTree.Node(
            rules=[
                BaseTree.EmptyNode,
                BaseTree.IndexedNode],
            limit=2)
        next = BaseTree.EmptyNode(0, rules=[BaseTree.Node])
        third = BaseTree.Node()
        self.item.AddNode(elem)
        self.item.AddNode(next)
        self.item.AddNode(third)
        self.assertEqual(next.GetChild(0), third)

    def testAddNodeAddsToCurrentLevelWithRelevantRuleAndLimit(self):
        # this test confirms the first spot for third to land in is a second child of elem, because elem lets you have
        # node as a child and can have 2 children.
        elem = BaseTree.Node(
            rules=[
                BaseTree.EmptyNode,
                BaseTree.Node],
            limit=2)
        next = BaseTree.EmptyNode(0, rules=[BaseTree.Node])
        third = BaseTree.Node()
        self.item.AddNode(elem)
        self.item.AddNode(next)
        self.item.AddNode(third)
        self.assertEqual(elem.GetChild(1), third)

    def testAddNodeWithIndex(self):
        elem = BaseTree.IndexedNode(rules=[BaseTree.EmptyNode], limit=1)
        second_elem = BaseTree.EmptyNode(0)
        self.item.AddNode(elem)
        self.item.AddNode(second_elem, index=2)
        self.assertEqual(elem.GetChild(2), second_elem)

    def testAddNodeToSecondNode(self):
        elem = BaseTree.Node(rules=[BaseTree.EmptyNode])
        self.item.AddNode(elem)
        second = BaseTree.EmptyNode(0)
        self.item.AddNode(second)
        third = BaseTree.EmptyNode(0, rules=[BaseTree.Node])
        self.item.AddNode(third)
        fourth = BaseTree.Node()
        self.item.AddNode(fourth)
        self.assertEqual(third.GetChild(0), fourth)

    def testAddNodeToThirdNode(self):
        elem = BaseTree.Node(rules=[BaseTree.EmptyNode])
        self.item.AddNode(elem)
        second = BaseTree.EmptyNode(0)
        self.item.AddNode(second)
        third = BaseTree.EmptyNode(0)
        self.item.AddNode(third)
        fourth = BaseTree.EmptyNode(0, rules=[BaseTree.Node])
        self.item.AddNode(fourth)
        fifth = BaseTree.Node()
        self.item.AddNode(fifth)
        self.assertEqual(fourth.GetChild(0), fifth)

    def testFindFirstNode(self):
        elem = BaseTree.Node()
        self.item.AddNode(elem)
        self.assertEqual(self.item.FindNode(type(elem), 1), elem)

    def testFindSecondNode(self):
        elem = BaseTree.Node(rules=[BaseTree.Node])
        self.item.AddNode(elem)
        second = BaseTree.Node()
        self.item.AddNode(second)
        node = self.item.FindNode(type(elem), 2)
        self.assertEqual(node, second)

    def testFindFirstEmptyNodeOnFirstChild(self):
        elem = BaseTree.Node(rules=[BaseTree.Node])
        self.item.AddNode(elem)
        second = BaseTree.Node(rules=[BaseTree.EmptyNode])
        self.item.AddNode(second)
        third = BaseTree.EmptyNode(0)
        self.item.AddNode(third)
        node = self.item.FindNode(BaseTree.EmptyNode, 1)
        self.assertEqual(node, third)

    def testFindEmptyNodeOnSecondChild(self):
        elem = BaseTree.Node(rules=[BaseTree.Node])
        self.item.AddNode(elem)
        second = BaseTree.Node()
        self.item.AddNode(second)
        third = BaseTree.Node(rules=[BaseTree.EmptyNode])
        self.item.AddNode(third)
        fourth = BaseTree.EmptyNode(0)
        self.item.AddNode(fourth)
        node = self.item.FindNode(BaseTree.EmptyNode, 1)
        self.assertEqual(node, fourth)

    def testFailure(self):
        elem = BaseTree.Node(rules=[BaseTree.Node])
        self.item.AddNode(elem)
        second = BaseTree.Node()
        self.item.AddNode(second)
        third = BaseTree.Node(rules=[BaseTree.EmptyNode])
        self.item.AddNode(third)
        with self.assertRaises(BaseTree.CannotFindInTreeException):
            self.item.FindNode(BaseTree.EmptyNode, 1)

    def testAddNodeWithStringIndex(self):
        elem = BaseTree.IndexedNode(rules=[BaseTree.Node])
        self.item.AddNode(elem)
        second = BaseTree.Node()
        self.item.AddNode(second, "P1")
        self.assertEqual(elem.GetChild("P1"), second)

    def testFindNodeWithStringIndex(self):
        elem = BaseTree.IndexedNode(rules=[BaseTree.Node])
        self.item.AddNode(elem)
        second = BaseTree.Node()
        self.item.AddNode(second, "P1")
        self.assertEqual(self.item.FindNodeByIndex("P1"), second)

    def testFindNodeWithStringIndexOnSecondLevel(self):
        elem = BaseTree.Node(rules=[BaseTree.IndexedNode])
        self.item.AddNode(elem)
        second = BaseTree.IndexedNode(rules=[BaseTree.Node])
        self.item.AddNode(second)
        third = BaseTree.Node()
        self.item.AddNode(third, "S")
        self.assertEqual(self.item.FindNodeByIndex("S"), third)

    def testFindNodeWithStringIndexOnSecondLevelWhereFirstLevelIsIndexed(self):
        elem = BaseTree.IndexedNode(rules=[BaseTree.IndexedNode])
        self.item.AddNode(elem)
        second = BaseTree.IndexedNode(rules=[BaseTree.Node])
        self.item.AddNode(second, "A")
        third = BaseTree.Node()
        self.item.AddNode(third, "B")
        self.assertEqual(self.item.FindNodeByIndex("B"), third)
