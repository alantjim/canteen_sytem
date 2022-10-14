import cv2
import mediapipe as mp
import numpy as np
from tkinter import *
from random import *
import tkinter.messagebox

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



class ScoreBoard():

    def __init__(self, parent):
        self.parent = parent
        self.initGUI()
        self.reset()

    def initGUI(self):
        # Lives
        self.livesVar = IntVar()
        Label(self.parent, text="Lives:", font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=35, pady=100,
                                                                               sticky=N + W)
        Label(self.parent, textvariable=self.livesVar, font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=60,
                                                                                            pady=150, sticky=N + W)

        # Score
        self.scoreVar = IntVar()
        Label(self.parent, text="Score:", font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=35, pady=250,
                                                                               sticky=N + W)
        Label(self.parent, textvariable=self.scoreVar, font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=50,
                                                                                            pady=300, sticky=N + W)

        # High score
        self.highScoreVar = IntVar()
        Label(self.parent, text="Highest Score:", font=("Helvetica", 16, "bold")).grid(row=1, column=2, padx=0,
                                                                                       pady=400, sticky=N + W)
        Label(self.parent, textvariable=self.highScoreVar, font=("Helvetica", 16, "bold")).grid(row=1, column=2,
                                                                                                padx=50, pady=450,
                                                                                                sticky=N + W)

    def reset(self):
        self.lives = 100
        self.score = 0
        self.highScore = self.loadScore()

        self.livesVar.set(self.lives)
        self.scoreVar.set(self.score)
        self.highScoreVar.set(self.highScore)

    def loadScore(self):
        with open("high-score.txt", "r") as data:
            return int(data.read())

    def saveScore(self):
        if self.score > self.highScore:
            with open("high-score.txt", "w") as data:
                data.write(str(self.score))

    def gameOver(self):
        self.saveScore()
        tkinter.messagebox.showinfo("G0t R3kT M8 ?", "U Ju5t G0t R3kT M8 !")
        if tkinter.messagebox.askyesno("G0t R3kT M8 ?", "Pl4y Ag41n ?"):
            self.reset()
        else:
            exit()

    def updateBoard(self, livesStatus, scoreStatus):
        self.lives += livesStatus;
        self.score += scoreStatus
        if self.lives < 0: self.gameOver()
        self.livesVar.set(self.lives);
        self.scoreVar.set(self.score)


class ItemsFallingFromSky():

    def __init__(self, parent, canvas, player, board):
        self.parent = parent  # root form
        self.canvas = canvas  # canvas to display
        self.player = player  # to check touching
        self.board = board  # score board statistics

        self.fallSpeed = 50  # falling speed
        self.xPosition = randint(50, 750)  # random position
        self.isgood = randint(0, 1)  # random goodness

        self.goodItems = ["ananas.gif", "apple.gif", "orange.gif"]
        self.badItems = ["candy1.gif", "candy2.gif", "lollypop.gif"]

        # create falling items
        if self.isgood:
            self.itemPhoto = tkinter.PhotoImage(file="images/{}".format(choice(self.goodItems)))
            self.fallItem = self.canvas.create_image((self.xPosition, 50), image=self.itemPhoto, tag="good")
        else:
            self.itemPhoto = tkinter.PhotoImage(file="images/{}".format(choice(self.badItems)))
            self.fallItem = self.canvas.create_image((self.xPosition, 50), image=self.itemPhoto, tag="bad")

        # trigger falling item movement
        self.move_object()

    def move_object(self):
        # dont move x, move y
        self.canvas.move(self.fallItem, 0, 15)

        if (self.check_touching()) or (self.canvas.coords(self.fallItem)[1] > 650):  # [ x0, y0, x1, y1 ]
            self.canvas.delete(self.fallItem)  # delete if out of canvas
        else:
            self.parent.after(self.fallSpeed, self.move_object)  # after some time move object

    def check_touching(self):
        # find current coordinates
        x0, y0 = self.canvas.coords(self.fallItem)
        x1, y1 = x0 + 50, y0 + 50

        # get overlapps
        overlaps = self.canvas.find_overlapping(x0, y0, x1, y1)

        if (self.canvas.gettags(self.fallItem)[0] == "good") and (len(overlaps) > 1) and (
                self.board.lives >= 0):  # gettags : ("good",)
            self.board.updateBoard(0, 100)  # (lives, score)s
            return True  # touching yes

        elif (self.canvas.gettags(self.fallItem)[0] == "bad") and (len(overlaps) > 1) and (
                self.board.lives >= 0):  # gettags : ("bad",)
            self.board.updateBoard(-1, 0)  # (lives, score)
            return True  # touching yes

        return False  # touching not


class TheGame(ItemsFallingFromSky, ScoreBoard):



    def __init__(self, parent):
        self.parent = parent

        # windows form
        self.parent.geometry("1024x650")
        self.parent.title("G0t R3kT M8 ?")

        # canvas window
        self.canvas = Canvas(self.parent, width=800, height=600)
        self.canvas.config(background="#98D0E3")
        self.canvas.bind("<Key>", self.keyMoving)  # take keyboard input as movement
        self.canvas.focus_set()
        self.canvas.grid(row=1, column=1, padx=25, pady=25, sticky=W + N)

        # player character
        self.playerPhoto = tkinter.PhotoImage(file="images/{}".format("jew.gif"))
        self.playerChar = self.canvas.create_image((457, 500), image=self.playerPhoto, tag="player")

        # define score board
        self.personalboard = ScoreBoard(self.parent)

        # start poping falling items
        self.createEnemies()

    def keyMoving(self, event):

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


                    if  angle2 >195:
                        x = "right"
                    if angle2 < 170:
                        x = "left"

                except:
                    pass

                # print(results)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                cv2.imshow('Mediapipe feed', image)
                if (cv2.waitKey(10) &  0xFF == ord('q'))or 0xFF == ord('a' ) :
                    break


        print(x)
        if (x == 'left') and (self.canvas.coords(self.playerChar)[0] > 50):
            self.canvas.move(self.playerChar, -50, 0)
        if (x == 'right') and (self.canvas.coords(self.playerChar)[0] < 750):
            self.canvas.move(self.playerChar, 50, 0)
  def createEnemies(self):
        ItemsFallingFromSky(self.parent, self.canvas, self.playerChar, self.personalboard)
        self.parent.after(1100, self.createEnemies)


if __name__ == "__main__":
    root = Tk()
    TheGame(root)
    root.mainloop()
cap.release()
cv2.destroyAllWindows()