import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap= cv2.VideoCapture(0)

counter1 = 0
counter2 = 0
stage1 = None
stage2 = None

def calculate_angle1(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Midq
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    ##f angle > 180.0:
       # angle = 360 - angle

    return angle

def calculate_angle2(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Midq
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    ##f angle > 180.0:
       # angle = 360 - angle

    return angle

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
 while cap.isOpened():
     ret,frame=cap.read()
     image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
     image.flags.writeable = False

     results = pose.process(image)

     image.flags.writeable = True
     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

     try:
        landmarks=results.pose_landmarks.landmark
        #print(landmarks)

        shoulder1 = [landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y]
        elbow1 = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        wrist1 = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                 landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]

        shoulder2 = [landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y]
        elbow2 = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                  landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
        wrist2 = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                  landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]



        angle1 = calculate_angle1(shoulder1, elbow1, wrist1)
        angle2 = calculate_angle2(shoulder2, elbow2, wrist2)



        cv2.putText(image, str(angle1),
                    tuple(np.multiply(elbow1, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    )
        cv2.putText(image, str(angle2),
                    tuple(np.multiply(elbow2, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    )

        if angle1 < 184:
            stage1 = "down"
        if angle1 > 200 and stage1 == 'down':
            stage1 = "up"
            counter1 += 1
            print(counter1)

        if angle2 < 160:
          stage2 = "down1"
        if angle2 > 175 and stage2 == 'down1':
              stage2 = "up1"
              counter2 += 1
              print(counter2)

     except:
         pass
     cv2.rectangle(image, (0, 0), (225, 73), (245, 117, 16), -1)

     cv2.putText(image, 'REPS', (15, 12),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
     cv2.putText(image, str(counter1),
                 (10, 60),
                 cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)

     cv2.putText(image, 'STAGE', (65, 12),
                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
     cv2.putText(image, stage1,
                 (60, 60),
                 cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)


     # print(results)
     mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)

     cv2.imshow('Mediapipe feed',image)

     if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

