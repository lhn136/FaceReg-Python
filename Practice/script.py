import os
import cv2

# print(os.walk(path))
directory = ("/Users/LocNguyen/Documents/Jupyter Notebook/FaceReg-Python/Practice/sample-images")
for image_name in os.listdir(directory):
    if "jpg" in image_name[-4:]:
        # print(filename)
        # image_name =(os.path.join(directory, filename).split('/')[-1])
        # print("sample-images/"+image_name)
        img=cv2.imread("sample-images/"+image_name,1)
        resized_image=cv2.resize(img,(100,100))
        name = image_name.split(".")[0]
        cv2.imwrite("sample-images/output/"+name+"-100x100.jpg",resized_image)
