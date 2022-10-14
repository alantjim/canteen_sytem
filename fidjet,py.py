from turtle import *
import cv2
import mediapipe as mp
import numpy as np
x="null"

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
cap= cv2.VideoCapture(0)
def calculate_angle2(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Midq
    c = np.array(c)  # End

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    ##f angle > 180.0:
       # angle = 360 - angle

    return angle
state = {'turn': 0}


def spinner():
    """Draw fidget spinner."""
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()


def animate():
    """Animate fidget spinner."""
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def fk():
 with mp_pose.Pose(min_detection_confidence=0, min_tracking_confidence=0) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            # print(landmarks)

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

            angle2 = calculate_angle2(shoulder2, elbow2, wrist2)

            cv2.putText(image, str(angle1),
                        tuple(np.multiply(elbow1, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )
            cv2.putText(image, str(angle2),
                        tuple(np.multiply(elbow2, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )

            if angle2 > 195:
                state['turn'] += 150
            if angle2 < 170:
                state['turn'] += 150

        except:
            pass

        # print(results)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.imshow('Mediapipe feed', image)

        if cv2.waitKey(10) and 0xFF == ord('q'):
            break

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
fk()
listen()
animate()
done()
cap.release()
cv2.destroyAllWindows()

