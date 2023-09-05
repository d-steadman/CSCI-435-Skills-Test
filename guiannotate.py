import os.path
import sys
import xml.etree.ElementTree as ET

from parse import get_gui_boxes
from annotate import annotate_boxes

tree = ET.parse("Programming-Assignment-Data/com.yelp.android.xml")
root = tree.getroot()

boxes = get_gui_boxes(root)

annotate_boxes("Programming-Assignment-Data/com.yelp.android.png", boxes)

# Get directory and verify existence

directory = sys.argv[1]
assert os.path.isdir(directory), f"{directory} is not a valid directory"
