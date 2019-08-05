import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib.pyplot as plt

# Root directory of the project
ROOT_DIR = os.path.abspath("")

# Import Mask RCNN
sys.path.append(ROOT_DIR) 
from mrcnn import utils
import mrcnn.model as modellib
from mrcnn import visualize
# Import COCO config
sys.path.append(os.path.join(ROOT_DIR, "samples/coco/"))
import coco

from mrcnn.config import Config


from PIL import Image
from io import BytesIO
import base64
import wget

ENCODING = 'utf-8'


def get_default_model():

    ROOT_DIR = os.path.abspath("")

    # Directory to save logs and trained model
    MODEL_DIR = os.path.join(ROOT_DIR, "logs")

    # Path to trained weights file
    COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

    if not os.path.exists(COCO_MODEL_PATH):
    	utils.download_trained_weights(COCO_MODEL_PATH)

    class InferenceConfig(coco.CocoConfig):

        GPU_COUNT = 1
        IMAGES_PER_GPU = 1

    config = InferenceConfig()

    config.display()

    # Create model object.
    model = modellib.MaskRCNN(mode="inference",model_dir=MODEL_DIR, config=config)

    # Load weights trained on MS-COCO
    model.load_weights(COCO_MODEL_PATH, by_name=True)

    # COCO Class names
    class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
                'bus', 'train', 'truck', 'boat', 'traffic light',
                'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
                'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
                'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
                'kite', 'baseball bat', 'baseball glove', 'skateboard',
                'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
                'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
                'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
                'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
                'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
                'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
                'teddy bear', 'hair drier', 'toothbrush']
    
    return model, class_names

def display_segmented_image(model,img_path):
	image = skimage.io.imread(img_path)

	# Run detection
	results = model.detect([image], verbose=1)
	r = results[0]
	mask = r['masks']
	mask = mask.astype(int)

	## To get masks where class is 'Person'
	idx = np.where(r['class_ids'] == 1)[0][0]

	temp = skimage.io.imread(img_path)

	for j in range(temp.shape[2]):
    	temp[:,:,j] = temp[:,:,j] * mask[:,:,idx]

    cur_img = Image.fromarray(temp)
	save_name = "result.jpg"
	cur_img.save(save_name)
	new_img_path = os.path.abspath('') + '/result.jpg'

	return new_img_path

