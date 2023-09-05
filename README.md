# CSCI-435-Skills-Test

### Setup

This tool requires that you are running an updated version of Python 3.
The only library you need to install to user this is PIL, Python's Imaging library. Use the command below to install it:

```pip install pillow```


### How to use this tool

Use the command below to annotate all screens in a given directory. Each screen must have a screenshot and XML document of the same name. If one is missing, a warning will be produced.

```python guiannotate.py <directory>```

The annotated screenshots will be the original name with '_ANNOTATED' added to the end. Screens containing the _ANNOTATED suffix will be ignored as inputs in future usages of GUIAnnotate.

### Description of implementation

First, the program gets a single string input as the directory argument, and verifies that it exists. Then, it iterates through all screen files within the directory, filtering out those that appear to be already annotated.

For each screen, the program verifies that both the XML heirarchy and PNG screenshot exist. If this is not the case, the screen is ignored and a warning is given.

Then, the XML file is recursively parse to get those node elements that have no children. These leafs are filtered against a constant tuple of resource-id's that are general Android elements (such as task bars) that are not relevant specifically to the app. This allows a user to add their own resource-id's later, or adapt easily to name changes within Android. These leaf nodes then have their bounding boxes extracted and parsed into an (x1, y1, y2, y2) format which is usable by PIL later.

The bounding boxes are then drawn onto the specified screenshot in width 10, yellow lines to make them the most visible. Yellow was chosen both because it was used in the original example, but also due its general lack of use in UI designs. However, a further improvement of thise program would be to add a argument for color specification.

### Miscellaneous design choices

Ideally, an in-house solution would be used for the annotation since it is a relatively simple operation, however it seemed unecessarily complicated in this situation. However, PIL is still a stable and widely used library, so this program is still relatively dependent-free. In addition, PIL would make it easier to accept other screenshot formats in the future if PNGs were no longered favored for some reason.

Warnings were preferred over errors in this program since the issues they announce don't prevent all inputs from being processed, so it isn't necessary to avoid all processing because of one isolated issue.

Python as the programming language was chosen mostly because I am very familiar with it, and it excels at the iterative nature of this particular assignment. Also, its strong libraries make it very useful for fast implementation of a tool that doesn't need bleeding speeds, but can focus on stability and easy modification or expansion for different use cases.