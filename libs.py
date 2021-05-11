import dlib

reshape = dlib.shape_predictor('face_landmarks.dat')
facemod = dlib.face_recognition_model_v1('face_model.dat')
detector = dlib.get_frontal_face_detector()
