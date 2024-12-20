import os
import cv2
from deepface import DeepFace
from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)

# Path to your known faces directory
KNOWN_FACES_DIR = "./known_faces"

# Face information dictionary
FACE_INFO = {
    "random_face": {"age": 19, "crime": "Gang Activities"},
}

def generate_frames():
    video_capture = cv2.VideoCapture(0)
    known_faces = [os.path.splitext(face)[0] for face in os.listdir(KNOWN_FACES_DIR)]

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            current_frame_path = "current_face.jpg"
            cv2.imwrite(current_frame_path, face)

            try:
                results = DeepFace.find(current_frame_path, db_path=KNOWN_FACES_DIR, model_name="VGG-Face", enforce_detection=False)
                
                matched_name = None
                if results and isinstance(results, list) and len(results) > 0:
                    matched_face = results[0]
                    matched_name = os.path.basename(matched_face['identity'][0]).split('.')[0]

                    if matched_name == "random_face":
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box
                        # Zoom in on the detected face
                        zoomed_face = cv2.resize(face, (150, 150))
                        frame[0:150, 0:150] = zoomed_face

                        # Display details
                        details_x_offset = 160
                        cv2.putText(frame, f"Name: {matched_name}", (details_x_offset, 30), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
                        cv2.putText(frame, f"Age: {FACE_INFO[matched_name]['age']}", (details_x_offset, 60), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
                        cv2.putText(frame, f"Crime: {FACE_INFO[matched_name]['crime']}", (details_x_offset, 90), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
                    else:
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red box
                        cv2.putText(frame, "Name: Unknown", (x, y - 10), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
                else:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red box
                    cv2.putText(frame, "Name: Unknown", (x, y - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
            except Exception as e:
                print(f"Error during face recognition: {e}")

        # Encode the frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    video_capture.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), 
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/known_faces')
def get_known_faces():
    known_faces = [os.path.splitext(face)[0] for face in os.listdir(KNOWN_FACES_DIR)]
    return jsonify(known_faces)

if __name__ == '__main__':
    app.run(debug=True)
