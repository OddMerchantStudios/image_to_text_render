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

# take the unmodified greyscale array and render it with a sliding scale of characters\

# this could be modified significantly to be able to pass in a custom scale and iterate over each potential "color"

def render_gs_array(gs_array, output_path, characters = ['...', ',,,' , 'ooo', '888', '&&&'], 
                    thresholds = {'black': 35, 'dark gray': 75, 'gray': 150, 'light gray': 215}):
    
    output_str = ""
    for row in gs_array:
        for i in row:
            if i > thresholds['light gray']:
                output_str += characters[0]
            elif i > thresholds['gray']:
                output_str += characters[1]
            elif i > thresholds['dark gray']:
                output_str += characters[2]
            elif i > thresholds['black']:
                output_str += characters[3]
            elif i < thresholds['black']:
                output_str += characters[4]
        output_str += "\n"
    
    with open(output_path, "w") as f:
        f.write(output_str)



#sample output:

#binary_array = image_to_binary("./image.png")
#render_binary_arr(binary_array, "./binary_output.txt")

gs_arr = image_to_grayscale('image.png')
render_gs_array(gs_arr, 'gs_output.txt')
