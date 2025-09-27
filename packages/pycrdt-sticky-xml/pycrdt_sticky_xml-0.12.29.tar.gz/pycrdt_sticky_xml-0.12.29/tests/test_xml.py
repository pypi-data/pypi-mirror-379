import pytest
from pycrdt_sticky_xml import Array, Assoc, Doc, Map, XmlElement, XmlFragment, XmlText, StickyIndex


def test_plain_text():
    doc1 = Doc()
    frag = XmlFragment()
    doc1["test"] = frag
    with doc1.transaction():
        frag.children.append("Hello")
        with doc1.transaction():
            frag.children.append(", World")
        frag.children.append("!")

    assert str(frag) == "Hello, World!"


def test_api():
    doc = Doc()
    frag = XmlFragment(
        [
            XmlText("Hello "),
            XmlElement("em", {"class": "bold"}, [XmlText("World")]),
            XmlText("!"),
        ]
    )

    with pytest.raises(RuntimeError) as excinfo:
        frag.integrated
    assert str(excinfo.value) == "Not integrated in a document yet"

    with pytest.raises(RuntimeError) as excinfo:
        frag.doc
    assert str(excinfo.value) == "Not integrated in a document yet"

    with pytest.raises(ValueError):
        frag.to_py()

    doc["test"] = frag
    assert frag.parent is None
    assert str(frag) == 'Hello <em class="bold">World</em>!'
    assert len(frag.children) == 3
    assert str(frag.children[0]) == "Hello "
    assert str(frag.children[1]) == '<em class="bold">World</em>'
    assert str(frag.children[2]) == "!"
    assert list(frag.children) == [frag.children[0], frag.children[1], frag.children[2]]
    assert frag.children[0].parent == frag
    assert hash(frag.children[0].parent) == hash(frag)
    assert frag != object()

    frag.children.insert(1, XmlElement("strong", None, ["wonderful"]))
    frag.children.insert(2, " ")
    assert str(frag) == 'Hello <strong>wonderful</strong> <em class="bold">World</em>!'
    assert len(frag.children) == 5

    el = frag.children[3]
    assert el.tag == "em"
    assert len(el.attributes) == 1
    assert el.attributes.get("class") == "bold"
    assert el.attributes["class"] == "bold"
    assert "class" in el.attributes
    assert el.attributes.get("non-existent") is None
    assert "non-existent" not in el.attributes
    with pytest.raises(KeyError):
        el.attributes["non-existent"]
    assert list(el.attributes) == [("class", "bold")]

    del frag.children[2]
    del frag.children[1]
    assert str(frag) == 'Hello <em class="bold">World</em>!'


def test_text():
    text = XmlText("Hello")
    assert text.to_py() == "Hello"

    doc = Doc()

    with pytest.raises(ValueError):
        doc["test"] = XmlText("test")

    doc["test"] = XmlFragment([text])

    assert str(text) == "Hello"
    assert text.to_py() == "Hello"
    assert len(text) == len("Hello")

    text.clear()
    assert str(text) == ""

    text += "Goodbye"
    assert str(text) == "Goodbye"

    text.insert(1, " ")
    assert str(text) == "G oodbye"
    del text[1]
    assert str(text) == "Goodbye"

    text.insert(1, "  ")
    del text[1:3]
    assert str(text) == "Goodbye"

    assert text.diff() == [("Goodbye", None)]
    text.format(1, 3, {"bold": True})
    assert text.diff() == [
        ("G", None),
        ("oo", {"bold": True}),
        ("dbye", None),
    ]

    text.insert_embed(0, b"PNG!", {"type": "image"})
    assert text.diff() == [
        (b"PNG!", {"type": "image"}),
        ("G", None),
        ("oo", {"bold": True}),
        ("dbye", None),
    ]

    text.insert(len(text), " World!", {"href": "some-url"})
    assert text.diff() == [
        (b"PNG!", {"type": "image"}),
        ("G", None),
        ("oo", {"bold": True}),
        ("dbye", None),
        (" World!", {"href": "some-url"}),
    ]

    del text[0]
    assert text.diff() == [
        ("G", None),
        ("oo", {"bold": True}),
        ("dbye", None),
        (" World!", {"href": "some-url"}),
    ]

    del text[0:3]
    assert text.diff() == [
        ("dbye", None),
        (" World!", {"href": "some-url"}),
    ]

    with pytest.raises(RuntimeError):
        del text[0:5:2]
    with pytest.raises(RuntimeError):
        del text[-1:5]
    with pytest.raises(RuntimeError):
        del text[1:-1]
    with pytest.raises(TypeError):
        del text["invalid"]

    doc["test2"] = XmlFragment([XmlText()])


def test_element_with_any_attribute():
    doc = Doc()

    doc["test"] = frag = XmlFragment()
    el = XmlElement("div")
    frag.children.append(el)
    el.attributes["class"] = {"a": True}
    assert el.attributes["class"] == {"a": True}
    assert list(el.attributes) == [("class", {"a": True})]
    assert len(el.attributes) == 1


def test_element():
    doc = Doc()

    with pytest.raises(ValueError):
        doc["test"] = XmlElement("test")

    with pytest.raises(ValueError):
        XmlElement()

    doc["test"] = frag = XmlFragment()

    el = XmlElement("div", {"class": "test"})
    frag.children.append(el)
    assert str(el) == '<div class="test"></div>'

    el = XmlElement("div", [("class", "test")])
    frag.children.append(el)
    assert str(el) == '<div class="test"></div>'

    el = XmlElement("div", None, [XmlText("Test")])
    frag.children.append(el)
    assert str(el) == "<div>Test</div>"

    el = XmlElement("div")
    frag.children.append(el)
    assert str(el) == "<div></div>"

    with pytest.raises(ValueError):
        el.to_py()

    el.attributes["class"] = "test"
    assert str(el) == '<div class="test"></div>'
    assert "class" in el.attributes
    assert el.attributes["class"] == "test"
    assert el.attributes.get("class") == "test"
    assert len(el.attributes) == 1
    assert list(el.attributes) == [("class", "test")]

    del el.attributes["class"]
    assert str(el) == "<div></div>"
    assert "class" not in el.attributes
    assert el.attributes.get("class") is None
    assert len(el.attributes) == 0
    assert list(el.attributes) == []

    node = XmlText("Hello")
    el.children.append(node)
    assert str(el) == "<div>Hello</div>"
    assert len(el.children) == 1
    assert str(el.children[0]) == "Hello"
    assert list(el.children) == [node]

    el.children[0] = XmlText("Goodbye")
    assert str(el) == "<div>Goodbye</div>"

    del el.children[0]
    assert str(el) == "<div></div>"

    el.children.append(XmlElement("foo"))
    el.children.append(XmlElement("bar"))
    el.children.append(XmlElement("baz"))
    assert str(el) == "<div><foo></foo><bar></bar><baz></baz></div>"

    del el.children[0:2]
    assert str(el) == "<div><baz></baz></div>"

    with pytest.raises(TypeError):
        del el.children["invalid"]
    with pytest.raises(IndexError):
        el.children[1]

    text = XmlText("foo")
    el.children.insert(0, text)
    assert str(el) == "<div>foo<baz></baz></div>"

    el2 = XmlElement("bar")
    el.children.insert(1, el2)
    assert str(el) == "<div>foo<bar></bar><baz></baz></div>"

    with pytest.raises(IndexError):
        el.children.insert(10, "test")
    with pytest.raises(ValueError):
        el.children.append(text)
    with pytest.raises(ValueError):
        el.children.append(el2)
    with pytest.raises(TypeError):
        el.children.append(object())


def test_observe():
    doc = Doc()
    doc["test"] = fragment = XmlFragment(["Hello world!"])
    events = []

    def callback(event):
        nonlocal fragment
        with pytest.raises(RuntimeError) as excinfo:
            fragment.children.append("text")
        assert (
            str(excinfo.value)
            == "Read-only transaction cannot be used to modify document structure"
        )
        events.append(event)

    sub = fragment.observe_deep(callback)  # noqa: F841

    fragment.children.append(XmlElement("em", None, ["This is a test"]))
    assert len(events) == 1
    assert len(events[0]) == 1
    assert events[0][0].children_changed is True
    assert str(events[0][0].target) == "Hello world!<em>This is a test</em>"
    assert events[0][0].path == []
    assert len(events[0][0].delta) == 2
    assert events[0][0].delta[0]["retain"] == 1
    assert str(events[0][0].delta[1]["insert"][0]) == "<em>This is a test</em>"

    events.clear()
    fragment.children[0].format(1, 3, {"bold": True})

    assert len(events) == 1
    assert len(events[0]) == 1
    assert str(events[0][0].target) == "H<bold>el</bold>lo world!"
    assert events[0][0].delta[0] == {"retain": 1}
    assert events[0][0].delta[1] == {"retain": 2, "attributes": {"bold": True}}


def test_xml_in_array():
    doc = Doc()
    array = doc.get("testmap", type=Array)
    frag = XmlFragment()
    array.append(frag)
    frag.children.append("Test XML!")

    assert len(array) == 1
    assert str(array[0]) == "Test XML!"

    with pytest.raises(TypeError):
        array.append(XmlText())
    with pytest.raises(TypeError):
        array.append(XmlElement("a"))
    assert len(array) == 1


def test_xml_in_map():
    doc = Doc()
    map = doc.get("testmap", type=Map)
    frag = map["testxml"] = XmlFragment()
    frag.children.append("Test XML!")

    assert len(map) == 1
    assert "testxml" in map
    assert str(map["testxml"]) == "Test XML!"

    with pytest.raises(TypeError):
        map["testtext"] = XmlText()
    with pytest.raises(TypeError):
        map["testel"] = XmlElement("a")


def test_xml_text_sticky_index():
    doc = Doc()
    frag = doc.get("frag", type=XmlFragment)
    text = XmlText("0123456789")
    frag.children.append(text)

    idx_after = text.sticky_index(5, Assoc.AFTER)
    idx_before = text.sticky_index(5, Assoc.BEFORE)

    text.insert(5, "XXX")

    assert idx_after.get_index() == 8  # 5 + 3
    assert idx_before.get_index() == 5

    idx_start = text.sticky_index(0, Assoc.BEFORE)
    text.insert(0, "AAA")

    assert idx_start.get_index() == 0

    current_len = len(text)
    idx_end = text.sticky_index(current_len - 1, Assoc.AFTER)
    text.insert(current_len, "ZZZ")

    assert idx_end.get_index() == current_len - 1


def test_xml_element_sticky_index():
    doc = Doc()
    frag = doc.get("frag", type=XmlFragment)

    elem = XmlElement("div", None, [
        XmlText("first"),
        XmlText("second"),
        XmlText("third")
    ])

    frag.children.append(elem)

    idx_after = elem.sticky_index(1, Assoc.AFTER)
    idx_before = elem.sticky_index(1, Assoc.BEFORE)

    elem.children.insert(1, XmlText("inserted"))

    assert idx_after.get_index() == 2
    assert idx_before.get_index() == 1

    idx_start = elem.sticky_index(0, Assoc.BEFORE)
    elem.children.insert(0, XmlText("zero"))

    assert idx_start.get_index() == 0

def test_xml_fragment_sticky_index_basic():
    doc = Doc()
    frag = doc.get("root", type=XmlFragment)

    # Start with three children
    frag.children.append(XmlText("A"))
    frag.children.append(XmlText("B"))
    frag.children.append(XmlText("C"))

    # Create sticky indices at the fragment level
    idx_after_0 = frag.sticky_index(0, Assoc.AFTER)    # after position 0 (gap between A and B)
    idx_before_1 = frag.sticky_index(1, Assoc.BEFORE)  # before B (element at index 1)

    # Insert at the front
    frag.children.insert(0, XmlText("X"))
    # Now children: [X, A, B, C]
    assert idx_after_0.get_index() == 1  # stays at gap after original position 0

    # Insert at position 1
    frag.children.insert(1, XmlText("Y"))
    # Now children: [X, Y, A, B, C]
    assert idx_before_1.get_index() == 3  # follows B which moved from index 1 to 3

    # Sanity: string rendering still stable
    assert str(frag) == "XYABC"


def test_xml_fragment_sticky_index_end_and_bounds():
    doc = Doc()
    frag = doc.get("root", type=XmlFragment)

    frag.children.append(XmlText("A"))
    frag.children.append(XmlText("B"))

    # Yrs behavior at end position (index == len):
    # - BEFORE(len) succeeds and creates a sticky index at position len
    # - AFTER(len) fails, so fallback creates AFTER(len-1)
    end_index = len(frag.children)  # 2
    idx_end_before = frag.sticky_index(end_index, Assoc.BEFORE)
    idx_end_after = frag.sticky_index(end_index, Assoc.AFTER)
    
    # BEFORE(2) points to 2, AFTER(2) falls back to AFTER(1) which points to 1
    assert idx_end_before.get_index() == 2
    assert idx_end_after.get_index() == 1

    # Append an element
    frag.children.append(XmlText("C"))  # children: [A, B, C]
    
    # BEFORE stays at 2 (now points before C)
    # AFTER stays at 1 (still points after A, before B)
    assert idx_end_before.get_index() == 2
    assert idx_end_after.get_index() == 1

    # Out of bounds should raise (len + 1 is invalid)
    with pytest.raises(IndexError):
        frag.sticky_index(len(frag.children) + 1, Assoc.AFTER)


def test_xml_fragment_sticky_index_insert_middle():
    doc = Doc()
    frag = doc.get("root", type=XmlFragment)
    for ch in ["A", "B", "C", "D"]:
        frag.children.append(XmlText(ch))
    # children: [A, B, C, D]

    idx_after_1 = frag.sticky_index(1, Assoc.AFTER)   # after position 1
    idx_before_2 = frag.sticky_index(2, Assoc.BEFORE) # before C (element at position 2)

    # Insert at index 1 (between A and B)
    frag.children.insert(1, XmlText("X"))
    # children: [A, X, B, C, D]
    assert idx_after_1.get_index() == 2   # stays at the gap after original position 1
    assert idx_before_2.get_index() == 3  # follows C which moved from index 2 to 3


def test_xml_fragment_sticky_index_json_and_binary_roundtrip():

    doc = Doc()
    frag = doc.get("frag", type=XmlFragment)
    for tag in ["p", "em", "strong"]:
        frag.children.append(XmlElement(tag))

    # Create a sticky index at index 1 (between p and em)
    si = frag.sticky_index(1, Assoc.AFTER)

    # Binary round-trip
    encoded = si.encode()
    si_decoded = StickyIndex.decode(encoded, frag)
    assert si_decoded.get_index() == si.get_index()
    assert si_decoded.assoc == si.assoc

    # JSON round-trip
    as_json = si.to_json()
    si_json = StickyIndex.from_json(as_json, frag)
    assert si_json.get_index() == si.get_index()
    assert si_json.assoc == si.assoc

    # Mutate: insert a node at the front; all three should track consistently
    frag.children.insert(0, XmlElement("header"))
    assert si.get_index() == 2
    assert si_decoded.get_index() == 2
    assert si_json.get_index() == 2


def test_xml_fragment_sticky_index_assoc_semantics():
    doc = Doc()
    frag = doc.get("frag", type=XmlFragment)
    frag.children.append(XmlText("A"))
    frag.children.append(XmlText("B"))

    idx_before = frag.sticky_index(1, Assoc.BEFORE)
    idx_after = frag.sticky_index(1, Assoc.AFTER)

    # Insert an element exactly at index 1; check stickiness
    frag.children.insert(1, XmlText("X"))  # [A, X, B]
    assert idx_before.get_index() == 1  # still before the original "B" slot
    assert idx_after.get_index() == 2   # after the boundary, now after inserted "X"
