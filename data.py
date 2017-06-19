import cv2
import numpy as np
import os
import re

train_images_dir = '../images/train/'

inputs = []
outputs = []

def load_image(filename):
	im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
	im = cv2.threshold(im, 127, 1, cv2.THRESH_BINARY_INV)[1]
	return np.matrix(im.flatten()).T

for f in os.listdir(train_images_dir):
	m = re.match(r'(\d+)d.png', f)
	if m is not None:
		code = int(m.group(1))
		im = load_image(train_images_dir + f)
		inputs.append(im)
		oo = np.zeros((7,1))
		oo[code * 7 // 18, 0] = 1
		outputs.append(np.matrix(oo))

validation = []
validate_images_dir = '../images/validate/'
for f in os.listdir(validate_images_dir):
	m = re.match(r'(.*)\.png', f)
	if m is not None:
		name = m.group(1)
		validation.append([name, load_image(validate_images_dir + f)])
