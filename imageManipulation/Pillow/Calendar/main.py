from PIL import Image
import os


def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()


arr = os.listdir('img/')

for path in arr:
  crop('img/'+path, (398, 155, 398 + 952, 155 + 760), 'output/'+path)

# crop('img/Calendar1.png', (398, 155, 398 + 952, 155 + 760), 'crop.png')