# importing modules
import mediapipe as mp
import cv2

# creating class
class Face_detector_mesh():

    def __init__(self):

        mpFace_mesh = mp.solutions.face_mesh
        self.Face_mesh = mpFace_mesh.FaceMesh(max_num_faces=3)
        mpDraw = mp.solutions.drawing_utils

    def face_detector(self, img):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.Face_mesh.process(imgRGB)

        return img
    
    def tracking_point(self, img, track_point: int, draw= True):

        ih, iw, _ = img.shape

        red_color = (0,0,255)
        blk_color = (0,0,0)

        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                for id, lm in enumerate(faceLms.landmark):
                    x, y = int(lm.x*iw), int(lm.y*ih)

                    if id==track_point:
                        
                        cv2.circle(img, (x,y), 10, blk_color, 2)
                        cv2.line(img, (x,0), (x,int(ih)), blk_color, 2)
                        cv2.line(img, (0,y), (int(iw), y), blk_color, 2)
                        cv2.circle(img, (x,y), 3, red_color, -1)

        return img