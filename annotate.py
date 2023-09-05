from PIL import Image, ImageDraw


def annotate_boxes(screenshot_path, boxes, output_path):
    screenshot = Image.open(screenshot_path)
    draw = ImageDraw.Draw(screenshot)

    for box in boxes:
        draw.rectangle(box, width=10, outline="yellow")

    screenshot.save(output_path)
