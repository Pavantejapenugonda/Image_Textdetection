import cv2
import pytesseract
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--folder_path',
                    help="Provide path of the folder contains images")
args = parser.parse_args()
path_folder = args.folder_path

end_strings = (".jpeg", ".jpg", ".png")
image_paths = os.listdir(path_folder)
for path in image_paths:
    if path.endswith(end_strings):
        image_path = path_folder.replace("\\", "\\")+'\\' + path
        img = cv2.imread(image_path)
        text = pytesseract.image_to_string(img)
        print('For Image {0} text is : {1}'.format(path, text))
    else:
        print(f'Its not a image path {0}'.format(path))
