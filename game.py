from random import *
from turtle import *

from freegames import vector
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

with mp_pose.Pose(min_detection_confidence=0, min_tracking_confidence=0) as pose:
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

        if angle1 < 184 and angle2 < 165:
            print ("left")
        if angle1 > 200 and angle2 > 175:
            print("right")

     except:
         pass



     # print(results)
     mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)

     cv2.imshow('Mediapipe feed',image)

     if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

bird = vector(0, 0)
balls = []


def tap(x, y):
    """Move bird up in response to screen tap."""
    up = vector(0, 30)
    bird.move(up)


def inside(point):
    """Return True if point on screen."""
    return -200 < point.x < 200 and -200 < point.y < 200


def draw(alive):
    """Draw screen objects."""
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()


def move():
    """Update object positions."""
    bird.y -= 5

    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            return

    draw(True)
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()