
# Object Recognition With Yolov5
>This project uses deep learning to create an image recognition program. The objects used in training and testing the model are: Pikachu, Pichu, multirotor drones, people, cats, and dogs. 
>By adding Pichu, we elevated the model’s complexity given that Pikachu is the evolution after Pichu. 
The criteria for this project for ECEN4273 is for the model to take in a short video file (.mp4) and output a video file (.mp4) that has bounding boxes around the recognizable objects (Pikachu, Pichu, people, etc.). Overall, the model needed to test at a minimum of 75% accuracy.


|Classes  |
| --------|
| Cat     |
| Dog     |
| Drone   |
| Person  |
| Pichu   |
| Pikachu |

## How to Run 

  
### PC Version

* The weights for this model are already trained for the classes above
* To use the detection for images, videos, etc. run the code below


  ```
  python detect.py --weights runs/train/exp/weights/best.pt --source 0  # webcam
                                                                     img.jpg  # image
                                                                     vid.mp4  # video
                                                                     path/  # directory
                                                                     'path/*.jpg'  # glob
                                                                     'https://youtu.be/Zgi9g1ksQHc'  # YouTube
  ```              
                
* Output will be saved to 'runs/detect/exp/'


## How to Create Your Own Classification Model

### Gathering Dataset

>Instead of using online datasets, we decided to scrap the internet to create our own. We used an open source Google Image Scraper on GitHub where we mainly manipulated the parameters for a keyword and number of images. For our scenario we wanted 100 images for each dataset (600 images total), and the script found and renamed the images based on the keyword (Pikachu, Pichu, people, etc.). 

The GitHub repository is linked below.

https://github.com/ohyicong/Google-Image-Scraper`

### Annotating Dataset

>Labelme is a python image annotation resource found on GitHub. This program allowed us to upload our directory/datasets to create handmade, labeled bounding boxes around what objects are needed in the photo. We annotated our 600 images through this program with the rectangle bounding boxes. The GitHub respiratory is linked below.

To install Labelme, run this command in the terminal
```
pip install labelme
```
And to run the application, enter 'labelme' into the terminal to launch the gui.
Or use the Github repository linked below.

https://github.com/wkentaro/labelme

### Formatting Dataset

>Roboflow is a dataset creation software with multiple features such as image resizing and augmentation. Using this site we were able to generate extra images for training while resizing every image to a 640 x 640 size while keeping the aspect ratio. A link to this projects dataset is linked below.

https://app.roboflow.com/oklahoma-state-university/software-engineering-project-2/overview 

### Training Dataset

>With the dataset formatted, we can just use the integrated training script that yolov5 provides. It will save the weights so you can train off of it later or use it for detection like we did above.

* Weights are saved in 'runs/train/exp/weights/'

```
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5n.yaml  --batch-size 128
                                                                 yolov5s                    64
                                                                 yolov5m                    40
                                                                 yolov5l                    24
                                                                 yolov5x                    16
```


https://github.com/charliebobmiller/ECEN4273-Project2