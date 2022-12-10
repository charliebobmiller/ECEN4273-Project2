
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

### How to Run 

  
### PC Version

* The weights for this model are already trained for the classes above
*To use the detection for images, videos, etc. run the code below


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



https://github.com/charliebobmiller/ECEN4273-Project2