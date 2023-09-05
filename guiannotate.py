import os
import sys
import xml.etree.ElementTree as ET

from parse import get_gui_boxes
from annotate import annotate_boxes


# Get directory and verify existence

assert len(sys.argv == 2), "Program expects one argument"
directory = sys.argv[1]
assert os.path.isdir(directory), f"{directory} is not a valid directory"

# Get screen names in directory

# Removal of file extension from Stack Overflow: https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python
screens = [filename.rsplit(".", maxsplit=1)[0] for filename in os.listdir(directory)]

# Filter annotated screens
screens = filter(lambda screen: "_ANNOTATED" not in screen, screens)

# Annotate all screens
for screen in screens:
    xml_path = os.path.join(directory, screen + ".xml")
    screenshot_path = os.path.join(directory, screen + ".png")
    output_path = os.path.join(directory, screen + "_ANNOTATED.png")

    # Make sure we have both input files for each package
    if not (os.path.isfile(xml_path) and os.path.isfile(screenshot_path)):
        print(f"[WARNING] screen '{screen}' is missing one input file")
        continue

    # Annotate screen
    tree = ET.parse(xml_path)
    root = tree.getroot()

    boxes = get_gui_boxes(root)
    annotate_boxes(screenshot_path, boxes, output_path)
