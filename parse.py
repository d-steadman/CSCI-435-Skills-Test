def get_leafs(root):
    """Recursive generator to get leaf nodes from the root of an ET element."""

    # Only return leaf nodes that apply to the target package
    if len(root) == 0 and \
       root.attrib.get("resource-id").startswith(root.attrib.get("package")):
        yield root

    else:
        for child in root:
            yield from get_leafs(child)


def get_gui_boxes(root):
    """Extract bounding boxes from GUI leaf nodes."""

    bounds = [node.attrib["bounds"] for node in get_leafs(root)]

    # NOTE: no need for regex parsing, bounds format is very predictable
    # EX: "[100,200][200,300]"
    boxes = []

    for bounds_text in bounds:
        coords = bounds_text[1:-1].replace("][", ",")  # Combine coord numbers into one list
        box = [int(n) for n in coords.split(",")]
        boxes.append(box)

    return boxes
