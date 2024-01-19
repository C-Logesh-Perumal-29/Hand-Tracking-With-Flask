from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def hand_tracking():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()

        results = hands.process(img)

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                                       mp_draw.DrawingSpec((41, 61, 51), 2, 2),
                                       mp_draw.DrawingSpec((170, 197, 194), 2, 2))

        _, jpeg = cv2.imencode('.jpg', img)
        frame = jpeg.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(hand_tracking(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
