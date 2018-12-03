from Picture import open_image, save_image, convert_grayscale

image = open_image('./images/GrayscaleTest.png');

newImage = convert_grayscale(image)

save_image(newImage, './images/GrayScaleOut.png')