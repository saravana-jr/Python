import os
import cv2
import imageio
import json
import tkinter as tk
from tkinter import filedialog

def detectfaces(img_path,display=False):
    try:
        if img_path.lower().endswith('.jpg'):
            color_img=cv2.imread(img_path)
        elif img_path.lower().endswith('.gif'):
            color_img=imageio.mimread(img_path)[0]
            color_img=cv2.cvtColor(color_img,cv2.COLOR_BGR2RGB)
    except Exception as e:
        raise e

    h=color_img.shape[0]
    w=color_img.shape[1]
    if (w/h)>(1280/720):
        color_img=cv2.resize(color_img,(1280,int(h*1280/w)))
    else:
        color_img=cv2.resize(color_img,(int(w*720/h),720))


    gray_img=cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY).copy()


    cascade= cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
    faces=cascade.detectMultiScale(gray_img)
    print("found{0} face{1} in {2}".format(len(faces),'s'if(len(faces) > 1) else'',os.path.basename(img_path)))

    if display:
        for(x,y,w,h) in faces:
            cv2.rectangle(color_img,(x,y),(x+w,y+h),(0,255,2),3)


        cv2.imshow("Facial detection",color_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return json.dumps({'countfaces': len(faces),
                       'imagelocation': img_path})

def main():
    root = tk.Tk()
    root.withdraw()
    img_path=filedialog.askopenfilename(initialdir = 'F:\Engagement=23.06.2020',title="Choose image",filetypes=(('JPEG','*.jpg;*.jpeg'),
                                                       ('GIF','*.gif'),
                                                       ('PNG','*.png'),
                                                       ('all files','*.*')))
                    
    output= detectfaces(img_path,display=True)
    json_path=(".").join(img_path.split(".")[:-1]) + '.json'
    x=input("save result to{} [y/n]:".format(os.path.basename(json_path)))
    if x.lower() in ("y","yes"):
        f=open(json_path,'w')
        f.write(output)
        f.close()
        print("saved result to{}".format(os.path.basename(json_path)))

if __name__ == "__main__": main()

    


