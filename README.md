# EmotionRecognizer
Python script to recognize the emotion of a person in the picture using Opencv and DeepFace

1. EmotionRecognizer.py -> python code to detect emotions in the input image. 
2. EmotionRecognizer.ipynb -> jupyter notebook with slight changes in the code.

  Both the programs follow the same approach of reading the image , detecting faces in the image , detecting the dominant emotions , age , gender and race of the person, writing the result as text on the image and finally displaying the image. 

  Packages : 
  opencv-python -> to read the image, add text and draw bounding boxes on the image and to use the frontal face haarcascade classifier.
  DeepFace -> to detect the dominant emotion, age, race and gender of the person in the image. Throws error if it does not detect an image. ( PS: Dont try it with your pet's pictures :D )

2. happy_girl.jpg    ->  input image
3. haarcascade_frontalface_default.xml -> pre-trained object detection models for face detection. You have many more haarcascade models like QR code detector and number plate detector which come of use in other mini-projects. Link to check it out : https://github.com/anaustinbeing/haar-cascade-files

If you liked it, you should probably check out my project on realtime emotion recognition. 
