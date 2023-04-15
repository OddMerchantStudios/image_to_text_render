from PIL import Image
import numpy as np


# method to scan an image into an array

def image_to_binary(img_path, sensitivity = 100):

    img = Image.open(img_path)

    # convert the image to grayscale

    img = img.convert('L')

    # In grayscale images, each pixel is represented by a single value between 0 and 255, where 0 is black and 255 is white
    img_arr = np.array(img)
    # Every value in img_arr becomes 1 if it's above the sensitivity threshold, otherwise it's 0
    binary_arr = np.where(img_arr > sensitivity, 1, 0)

    return binary_arr

# method to scan an image into a greyscale array

def image_to_grayscale(img_path):
    img = Image.open(img_path)

    # convert the image to grayscale

    img = img.convert('L')

    # In grayscale images, each pixel is represented by a single value between 0 and 255, where 0 is black and 255 is white
    gs_arr = np.array(img)

    return gs_arr
    
# render binary array into a txt

def render_binary_arr(binary_arr, output_path, black = 'ooo', white = '...'):
    output_str = ""
    for row in binary_arr:
        for i in row:
            if i == 1:
                output_str += white
            else:
                output_str += black
        output_str += "\n"
    
    with open(output_path, "w") as f:
        f.write(output_str)

# next step would be to take the unmodified greyscale array and render it with a sliding scale of characters, much more comples than just b & w

# def render_gs_array(gs_array, output_path, characters = [], thresholds = []):
# ...



#sample output:

#binary_array = image_to_binary("./image.png")
#render_binary_arr(binary_array, "./rendered_image.txt")