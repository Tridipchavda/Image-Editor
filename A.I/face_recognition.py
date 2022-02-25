import cv2

face_file = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



def detect_file():
    file = input("Enter the file name :")
    if(file != ''):
        if(file.endswith(".jpg")):
            try:
                img = cv2.imread(f"C:/Users/tridip/Desktop/A.I/read_faces/{file}")

                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

                faces = face_file.detectMultiScale(img,1.1,11)

                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255, 0, 0),2)

                cv2.imshow('gray',gray)
                cv2.imshow('img',img)
                cv2.waitKey()
            except Exception as e:
                print('File Does not exist')
            else:
                print("Please Enter an existed file")
                detect_file()
        else:
            print("Please Enter the extention also (.jpg,.jpeg,.png)")
            detect_file()
    else:
        print("Please enter the file name")
        detect_file()

detect_file()
