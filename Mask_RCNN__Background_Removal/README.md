# Mask R-CNN for Background Removal from Images.

This is a Keras implementation of Mask R-CNN that is in large parts based on Matterport's Mask_RCNN. The model generates bounding boxes and segmentation masks for each instance of an object in the image. It's based on Feature Pyramid Network (FPN) and a ResNet101 backbone.

The repository includes:
* Source code of Mask R-CNN built on FPN and ResNet101.
* Training code for MS COCO
* Pre-trained weights for MS COCO
* A Flask application to remove background from image given its file path or image URL.
* A Docker file to run the whole Flask application as a container.

# Getting Started
* [demo.ipynb](samples/demo.ipynb) Is the easiest way to start. It shows an example of using a model pre-trained on MS COCO to segment objects in your own images.
It includes code to run object detection and instance segmentation on arbitrary images.

* ([model.py](mrcnn/model.py), [utils.py](mrcnn/utils.py), [config.py](mrcnn/config.py)): These files contain the main Mask RCNN implementation. 

* [application.py](Mask_RCNN_Background_Removal/application.py): This is the main file to run the Flask application. The routes to send image path or URL are passed in this file.

* [helper_methods.py](Mask_RCNN_Background_Removal/helper_methods.py): This file contains the various helper methods to run the main application file.

* [view.html](templates/view.html), [index.html](templates/index.html): These are the frontend files.

* [requirements.txt]: Packages necessary for the application.

* [Dockerfile]: Dockerfile to set up the Docker container for the application.

#### The model can be improved by retraining the weights on a specific dataset which has human images along with their masks and bounding boxes.

### [Output Images after Background Removal](samples)


## Installation
1. Clone this repository
2. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```
3. Download pre-trained COCO weights (mask_rcnn_coco.h5) from the [releases page](https://github.com/matterport/Mask_RCNN/releases).
4. Install Docker and build a Docker image in the same folder as Dockerfile.
5. Run the Docker container that is built to run the Flask app.
