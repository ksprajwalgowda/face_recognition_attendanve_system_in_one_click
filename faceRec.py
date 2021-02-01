import face_recognition
import cv2
import numpy as np
import time
from attendance import *
import os
li = os.listdir("C:\\Users\\Prajwal\\Desktop\\face_recognition_attendanve_system_in_one_click\\regface")

video_capture = cv2.VideoCapture(0)


known_face_encodings = []
known_face_names = []

for item in li:

    admin_image = face_recognition.load_image_file("regface\\"+item)
  
    known_face_encodings.append(face_recognition.face_encodings(admin_image)[0])
    known_face_names.append(item.rstrip(".jpg"))





def take():
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True
    t = 0
    

    while True:
        c = 0
        name = "Unknown"
        ret, frame = video_capture.read()

        
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    
        rgb_small_frame = small_frame[:, :, ::-1]

    
        if process_this_frame:
            
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
                name = "Unknown"

            
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                
                    
                face_names.append(name)
                if name in known_face_names:
                    
                    c = 1
                

        process_this_frame = not process_this_frame


        
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        
        cv2.imshow('Video', frame)
        if c == 1:
            
            rec(name)
      
            time.sleep(2)
            cv2.destroyAllWindows()
            return 1,name
     
        t=1+t
        
        if t > 150:
            cv2.destroyAllWindows()
            return 0,name

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        
       

    video_capture.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    while True:
        click = input("press \"Y\" to take attendence and \"N\" to exit ")
        if click.lower() == "y":
            
            print(take())
        elif click.lower() == "n":
            exit(0)
    
