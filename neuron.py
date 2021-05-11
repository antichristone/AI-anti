import cv2
import numpy as np

from libs import reshape, facemod, detector
from skimage import io as photo
from scipy.spatial import distance


class AI():
    def __init__(self, color=None):
        self.mesh_color = (0, 255, 234)

        if color not in [None]:
            self.mesh_color = color

    def face_id(self, data):
        img = photo.imread(data)
        dets = detector(img, 1)
        for k, dec in enumerate(dets):
            shape = reshape(img, dec)
            face_descriptor_one = facemod.compute_face_descriptor(img, shape)

        return face_descriptor_one

    def face_comparison(self, data_one, data_two):
        search = distance.euclidean(data_one, data_two)
        return search

    def creating_a_photo(self, file=None):
        frame = cv2.imread(file)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)

        for face in faces:
            landmarks = reshape(gray, face); mesh = {}
            for number in range(0, 68):
                try:
                    mesh[number] = (landmarks.part(number).x, landmarks.part(number).y)
                except Exception as e:
                    print(f"ERROR: {e}")

            self.mesh_face(mesh=mesh, frame=frame)

        cv2.imwrite(f'{file}.jpg', frame)
        cv2.destroyAllWindows()

        return 'done'

    def creating_a_video(self, display_image=None, file=None):
        video_data = cv2.VideoCapture(file)
        output = cv2.VideoWriter(f'{file}.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (int(video_data.get(3)), int(video_data.get(4))))

        while True:
            cache, frame = video_data.read()

            try:
                search_faces = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            except Exception as error:
                break

            for face in detector(search_faces):

                landmarks = reshape(search_faces, face); mesh = {}

                for number in range(0, 68):
                    try:
                        mesh[number] = (landmarks.part(number).x, landmarks.part(number).y)
                    except Exception as e:
                        print(f"ERROR: {e}")

                self.mesh_face(mesh=mesh, frame=frame)

            if display_image == True:
                cv2.imshow('frame', frame)

            output.write(frame)

        video_data.release()
        output.release()
        cv2.destroyAllWindows()
        cv2.destroyAllWindows()

        return 'done'

    def mesh_face(self, mesh, frame):
        try:
            cv2.line(frame,  mesh[27],  mesh[28],  self.mesh_color, 1)
            cv2.line(frame,  mesh[28],  mesh[29],  self.mesh_color, 1)
            cv2.line(frame,  mesh[29],  mesh[30],  self.mesh_color, 1)
            cv2.line(frame,  mesh[31],  mesh[32],  self.mesh_color, 1)
            cv2.line(frame,  mesh[32],  mesh[33],  self.mesh_color, 1)
            cv2.line(frame,  mesh[33],  mesh[34],  self.mesh_color, 1)
            cv2.line(frame,  mesh[34],  mesh[35],  self.mesh_color, 1)
            cv2.line(frame,  mesh[31],  mesh[27],  self.mesh_color, 1)
            cv2.line(frame,  mesh[35],  mesh[27],  self.mesh_color, 1)
            cv2.line(frame,  mesh[31],  mesh[30],  self.mesh_color, 1)
            cv2.line(frame,  mesh[35],  mesh[30],  self.mesh_color, 1)
            cv2.line(frame,  mesh[33],  mesh[30],  self.mesh_color, 1)
            cv2.line(frame,  mesh[27],  mesh[21],  self.mesh_color, 1)
            cv2.line(frame,  mesh[27],  mesh[22],  self.mesh_color, 1)
            cv2.line(frame,  mesh[27],  mesh[39],  self.mesh_color, 1)
            cv2.line(frame,  mesh[21],  mesh[39],  self.mesh_color, 1)
            cv2.line(frame,  mesh[27],  mesh[42],  self.mesh_color, 1)
            cv2.line(frame,  mesh[22],  mesh[42],  self.mesh_color, 1)
            cv2.line(frame,  mesh[0],  mesh[36],  self.mesh_color, 1)
            cv2.line(frame,  mesh[1],  mesh[36],  self.mesh_color, 1)
            cv2.line(frame,  mesh[17],  mesh[36],  self.mesh_color, 1)
            cv2.line(frame,  mesh[17],  mesh[37],  self.mesh_color, 1)
            cv2.line(frame,  mesh[18],  mesh[37],  self.mesh_color, 1)
            cv2.line(frame,  mesh[19],  mesh[37],  self.mesh_color, 1)
            cv2.line(frame,  mesh[20],  mesh[37],  self.mesh_color, 1)
            cv2.line(frame,  mesh[38],  mesh[20],  self.mesh_color, 1)
            cv2.line(frame,  mesh[21],  mesh[38],  self.mesh_color, 1)
            cv2.line(frame,  mesh[22],  mesh[43],  self.mesh_color, 1)
            cv2.line(frame,  mesh[23],  mesh[43],  self.mesh_color, 1)
            cv2.line(frame,  mesh[23],  mesh[44],  self.mesh_color, 1)
            cv2.line(frame,  mesh[24],  mesh[44],  self.mesh_color, 1)
            cv2.line(frame,  mesh[44],  mesh[26],  self.mesh_color, 1)
            cv2.line(frame,  mesh[26],  mesh[45],  self.mesh_color, 1)
            cv2.line(frame,  mesh[44],  mesh[25],  self.mesh_color, 1)
            cv2.line(frame,  mesh[45],  mesh[16],  self.mesh_color, 1)
            cv2.line(frame,  mesh[45],  mesh[15],  self.mesh_color, 1)
            cv2.line(frame,  mesh[48],  mesh[1],  self.mesh_color, 1)
            cv2.line(frame,  mesh[48],  mesh[7],  self.mesh_color, 1)
            cv2.line(frame,  mesh[54],  mesh[15],  self.mesh_color, 1)
            cv2.line(frame,  mesh[54],  mesh[9],  self.mesh_color, 1)
            cv2.line(frame,  mesh[54],  mesh[35],  self.mesh_color, 1)
            cv2.line(frame,  mesh[48],  mesh[31],  self.mesh_color, 1)
            cv2.line(frame,  mesh[50],  mesh[32],  self.mesh_color, 1)
            cv2.line(frame,  mesh[50],  mesh[31],  self.mesh_color, 1)
            cv2.line(frame,  mesh[32],  mesh[30],  self.mesh_color, 1)
            cv2.line(frame,  mesh[34],  mesh[30],  self.mesh_color, 1)
            cv2.line(frame,  mesh[52],  mesh[34],  self.mesh_color, 1)
            cv2.line(frame,  mesh[52],  mesh[35],  self.mesh_color, 1)
            cv2.line(frame,  mesh[31],  mesh[41],  self.mesh_color, 1)
            cv2.line(frame,  mesh[35],  mesh[46],  self.mesh_color, 1)
            cv2.line(frame,  mesh[1],  mesh[41],  self.mesh_color, 1)
            cv2.line(frame,  mesh[15],  mesh[46],  self.mesh_color, 1)
            cv2.line(frame,  mesh[57],  mesh[8],  self.mesh_color, 1)
            cv2.line(frame,  mesh[48],  mesh[5],  self.mesh_color, 1)
            cv2.line(frame,  mesh[48],  mesh[4],  self.mesh_color, 1)
            cv2.line(frame,  mesh[48],  mesh[3],  self.mesh_color, 1)
            cv2.line(frame,  mesh[7],  mesh[2],  self.mesh_color, 1)
            cv2.line(frame,  mesh[54],  mesh[12],  self.mesh_color, 1)
            cv2.line(frame,  mesh[54],  mesh[10],  self.mesh_color, 1)
            cv2.line(frame,  mesh[54],  mesh[11],  self.mesh_color, 1)
            cv2.line(frame,  mesh[9],  mesh[14],  self.mesh_color, 1)
            cv2.line(frame,  mesh[3],  mesh[31],  self.mesh_color, 1)
            cv2.line(frame,  mesh[3],  mesh[27],  self.mesh_color, 1)
            cv2.line(frame,  mesh[0],  mesh[31],  self.mesh_color, 1)
            cv2.line(frame,  mesh[39],  mesh[30],  self.mesh_color, 1)
            cv2.line(frame,  mesh[13],  mesh[35],  self.mesh_color, 1)
            cv2.line(frame,  mesh[13],  mesh[27],  self.mesh_color, 1)
            cv2.line(frame,  mesh[16],  mesh[35],  self.mesh_color, 1)
            cv2.line(frame,  mesh[30],  mesh[42],  self.mesh_color, 1)
            cv2.line(frame,  mesh[36],  mesh[37],  self.mesh_color, 1)
            cv2.line(frame,  mesh[37],  mesh[38],  self.mesh_color, 1)
            cv2.line(frame,  mesh[38],  mesh[39],  self.mesh_color, 1)
            cv2.line(frame,  mesh[39],  mesh[40],  self.mesh_color, 1)
            cv2.line(frame,  mesh[40],  mesh[41],  self.mesh_color, 1)
            cv2.line(frame,  mesh[41],  mesh[36],  self.mesh_color, 1)
            cv2.line(frame,  mesh[42],  mesh[43],  self.mesh_color, 1)
            cv2.line(frame,  mesh[43],  mesh[44],  self.mesh_color, 1)
            cv2.line(frame,  mesh[44],  mesh[45],  self.mesh_color, 1)
            cv2.line(frame,  mesh[45],  mesh[46],  self.mesh_color, 1)
            cv2.line(frame,  mesh[46],  mesh[47],  self.mesh_color, 1)
            cv2.line(frame,  mesh[47],  mesh[42],  self.mesh_color, 1)
            cv2.line(frame,  mesh[48],  mesh[49],  self.mesh_color, 1)
            cv2.line(frame,  mesh[49],  mesh[50],  self.mesh_color, 1)
            cv2.line(frame,  mesh[50],  mesh[51],  self.mesh_color, 1)
            cv2.line(frame,  mesh[51],  mesh[52],  self.mesh_color, 1)
            cv2.line(frame,  mesh[52],  mesh[53],  self.mesh_color, 1)
            cv2.line(frame,  mesh[53],  mesh[54],  self.mesh_color, 1)
            cv2.line(frame,  mesh[54],  mesh[55],  self.mesh_color, 1)
            cv2.line(frame,  mesh[55],  mesh[56],  self.mesh_color, 1)
            cv2.line(frame,  mesh[56],  mesh[57],  self.mesh_color, 1)
            cv2.line(frame,  mesh[57],  mesh[58],  self.mesh_color, 1)
            cv2.line(frame,  mesh[58],  mesh[59],  self.mesh_color, 1)
            cv2.line(frame,  mesh[59],  mesh[48],  self.mesh_color, 1)
            cv2.line(frame,  mesh[60],  mesh[61],  self.mesh_color, 1)
            cv2.line(frame,  mesh[61],  mesh[62],  self.mesh_color, 1)
            cv2.line(frame,  mesh[62],  mesh[63],  self.mesh_color, 1)
            cv2.line(frame,  mesh[63],  mesh[64],  self.mesh_color, 1)
            cv2.line(frame,  mesh[64],  mesh[65],  self.mesh_color, 1)
            cv2.line(frame,  mesh[65],  mesh[66],  self.mesh_color, 1)
            cv2.line(frame,  mesh[66],  mesh[67],  self.mesh_color, 1)
            cv2.line(frame,  mesh[67],  mesh[60],  self.mesh_color, 1)
            cv2.line(frame,  mesh[20],  mesh[21],  self.mesh_color, 1)
            cv2.line(frame,  mesh[19],  mesh[20],  self.mesh_color, 1)
            cv2.line(frame,  mesh[18],  mesh[19],  self.mesh_color, 1)
            cv2.line(frame,  mesh[17],  mesh[18],  self.mesh_color, 1)
            cv2.line(frame,  mesh[0],  mesh[17],  self.mesh_color, 1)
            cv2.line(frame,  mesh[0],  mesh[1], self.mesh_color, 1)
            cv2.line(frame,  mesh[1],  mesh[2], self.mesh_color, 1)
            cv2.line(frame,  mesh[2],  mesh[3],  self.mesh_color, 1)
            cv2.line(frame,  mesh[3],  mesh[4],  self.mesh_color, 1)
            cv2.line(frame,  mesh[4],  mesh[5],  self.mesh_color, 1)
            cv2.line(frame,  mesh[5],  mesh[6],  self.mesh_color, 1)
            cv2.line(frame,  mesh[6],  mesh[7],  self.mesh_color, 1)
            cv2.line(frame,  mesh[7],  mesh[8],  self.mesh_color, 1)
            cv2.line(frame,  mesh[21],  mesh[22],  self.mesh_color, 1)
            cv2.line(frame,  mesh[25],  mesh[26],  self.mesh_color, 1)
            cv2.line(frame,  mesh[24],  mesh[25],  self.mesh_color, 1)
            cv2.line(frame,  mesh[23],  mesh[24],  self.mesh_color, 1)
            cv2.line(frame,  mesh[22],  mesh[23],  self.mesh_color, 1)
            cv2.line(frame,  mesh[8],  mesh[9],  self.mesh_color, 1)
            cv2.line(frame,  mesh[9],  mesh[10],  self.mesh_color, 1)
            cv2.line(frame,  mesh[10],  mesh[11],  self.mesh_color, 1)
            cv2.line(frame,  mesh[11],  mesh[12],  self.mesh_color, 1)
            cv2.line(frame,  mesh[12],  mesh[13],  self.mesh_color, 1)
            cv2.line(frame,  mesh[13],  mesh[14],  self.mesh_color, 1)
            cv2.line(frame,  mesh[14],  mesh[15],  self.mesh_color, 1)
            cv2.line(frame,  mesh[15],  mesh[16],  self.mesh_color, 1)
            cv2.line(frame,  mesh[16],  mesh[26],  self.mesh_color, 1)
        except Exception as e:
            pass
