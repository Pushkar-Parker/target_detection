# importing modules

import cv2
import face_mesh_module as fmm
import time
import os
from pathlib import Path

# defining function to generate a video from the saved captured images
def img_to_video(images_path: str, save_path: str):

    # creating the directory
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    video_name = f'video_1.mp4' # defining the video name
    video_path = save_path # defining the save path

    filename = os.path.join(video_path, video_name) # combining the save path and the filename

    # sorting the images to generate a video in an ordered manner
    sorted_images = [] # creating an empty list to store the sorted image names
    img_path = Path(images_path) # accessing the image paths
    images = list(img_path.glob('*.jpg')) # accessing the image files by the extension

    # looping over the image files, putting them in an empty list and sorting the list
    # the list will contain only names without extension
    for image in images:
        sorted_images.append(int(image.stem))
        sorted_images.sort()

    image_files = [] # creating empty list to save the image names with extensions

    # looping over sorted images name and adding the extension to them
    for name in sorted_images:
        file_name = f'{name}.jpg'
        filepath = os.path.join(img_path, file_name)
        image_files.append(filepath)

    # Grabbing the first image for the shape of the image
    first_img = cv2.imread(image_files[0])

    size = list(first_img.shape)
    del size[2]
    size.reverse()

    # initiating video writer 
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(filename, fourcc, 20, size)

    # generating video using the saved images
    for image in image_files:
        frame = cv2.imread(image)
        video.write(frame)
        
    print(f'video saved in {save_path} as {video_name}')

    video.release()
    cv2.destroyAllWindows()

# defining function to save the captured images
def main(image_path: str, save_path : str, save_video=True, save_image= True):

    # initialising initial conditions
    
    # initialising the image capture using the web cam
    cap = cv2.VideoCapture(r'face_detection\9710114-uhd_3840_2160_25fps.mp4')

    run = True

    # defining width and hight
    new_width, new_height = 800, 500
    
    # inintialising the face detection module
    detector = fmm.Face_detector_mesh()
    
    pTime, cTime = 0, 0
    
    count = 0

    # looping to capture images
    while run and cap.grab():
        
        ret, img = cap.read() # initialising image capturing
        
        if ret:
            
            # Performing image operations 
            img = cv2.resize(img, (new_width, new_height)) # resizing the image
            img = cv2.flip(img, 1) # flipping the image
            img = detector.face_detector(img) # detected the face 
            img = detector.tracking_point(img, track_point=9) # tracking the target point

            # tracking the frames per second
            pTime = time.time()
            fps = f'FPS: {int(1/(pTime-cTime))}'
            cTime = pTime

            # putting the FPS on the image
            img = cv2.putText(img, fps, (5, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

            # displaying the image
            cv2.imshow('feed', img)

            # saving image if condition meets
            if save_image:

                filename = f'{count}.jpg'
                file_path = r'D:\software\mediapipe\target'

                file = os.path.join(file_path, filename)

                cv2.imwrite(file, img)

                print(f'{filename} saved in {file_path}')

                count+= 1
    
            k = cv2.waitKey(1)

            # qutting the loop if 'q' is pressed
            if k == ord('q'):
                
                if save_video:
                    img_to_video(images_path=image_path, save_path=save_path)
                
                run = False
    
    img_to_video(images_path=image_path, save_path=save_path)

# inititating main function
main(image_path=r'D:\software\mediapipe\target', save_path= r'D:\software\mediapipe\target\video', save_video= True, save_image= True)