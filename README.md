# Emotion Recognition using OpenCV and DeepFace

This repository contains Python scripts for recognizing the emotions of a person in a picture using OpenCV and DeepFace.

## Files

- **EmotionRecognizer.py**: Python code to detect emotions in the input image.
- **EmotionRecognizer.ipynb**: Jupyter notebook with slight changes in the code for interactive exploration.

Both programs follow the same approach: reading the input image, detecting faces in the image, determining the dominant emotions, age, gender, and race of the person, writing the results as text on the image, and finally displaying the image.

## Packages

- **opencv-python**: Used for reading the image, adding text, drawing bounding boxes, and using the frontal face haarcascade classifier.
- **DeepFace**: Used for detecting the dominant emotion, age, race, and gender of the person in the image. Throws an error if it does not detect a person's face.

**Note**: Using this script with pet pictures is not recommended. 😄

## Contents

- **happy_girl.jpg**: Sample input image.
- **haarcascade_frontalface_default.xml**: Pre-trained object detection model for face detection. This repository also contains other haarcascade models like QR code detector and number plate detector that can be useful for other projects.



If you enjoyed this project, you might be interested in my other project on  [converting an image to a pencil sketch](https://github.com/ask-1710/PencilSketch.git).

Feel free to explore, contribute, and share your feedback!

---

If you found this project useful, don't forget to give it a ⭐!
