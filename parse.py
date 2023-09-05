import xml.etree.ElementTree as ET

tree = ET.parse("Programming-Assignment-Data/com.yelp.android.xml")
root = tree.getroot()

def get_leafs(root):
    """Recursive generator to get leaf nodes from the root of an ET element."""
    if len(root) == 0:
        yield root

    else:
        for child in root:
            yield from get_leafs(child)


def get_gui_bounds(root):
    """Extract bounding boxes from GUI leaf nodes."""

    bounds = [node.attrib["bounds"] for node in get_leafs(root)]

    # NOTE: no need for regex parsing, bounds format is very predictable
    # EX: "[100,200][200,300]"
    boxes = []

    for bounds_text in bounds:
        coords = bounds_text[1:-1].replace("][", ",")   # Replaces parentheses with a comma for easy splitting
        box = [int(n) for n in coords.split(",")]
        boxes.append(box)

    return boxes
