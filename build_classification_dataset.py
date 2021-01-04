# -*- coding: utf-8 -*-
from functions import *
'''
Detect the coins in classification images for trainning the model
2 input parms:
    
<input_classification_path>
<output_classification_path>

'''


#detect  circles in image files and crop a rectangle
def detect_classification_coins(image_files,output_path):
    for j,i in zip(tqdm(range(0, len(image_files)),desc ="Building dataset progress: "),image_files):
    #for i in image_files:
        img = cv.imread(str(i))
        output = img.copy()
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        gray = cv.medianBlur(gray,5)
        circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,25,param1=10,param2=40,minRadius=30,maxRadius=45)
        if (type(circles).__name__ == "NoneType"):
            continue
        detected_circles = np.uint16(np.around(circles))
        for (x,y,r) in detected_circles[0,:]:
            cv.circle(output,(x,y),2,3)
            
            #draw circle - visualization
            #cv.circle(output,(x,y),r,(0,255,0),3)
            #cv.circle(output,(x,y),2,(0,255,255),3)
            #cv.circle(output,(x,y),r,3)

        #To validate we are not cross the boundries
        #x and y is small
        if(x<r+10 and y<r+10):
            output = output[0:y+r+1, 0:x+r+1]
        #x and y is big
        elif(y+r+10>480 and x+r+10>640):
            output = output[y-r-1:480, x-r-1:640]
            #x is small and y is big

        elif(x<r+10 and y+r+10>480):
            output = output[y-r-1:480, 0:x+r+1]
            #x is big and y is small
        elif(x+r+10>640 and y<r+10 ):
            output = output[0:y+r+1, x-r-1:640]
        #y is big
        elif((y+r+10>480 and x-r-10>0 ) or (y+r+10>480 and x+r+10<640)):
            output = output[y-r-1:480, x-r-1:x+r+1]
            #y is small
        elif((y<r+10 and x-r-10>0) or (y<r+10 and x+r+10<640)):
            output = output[0:y+r+1, x-r-1:x+r+1]
        #x is big
        elif((x+r+10>640 and y-r-10>0) or( x+r+10>640 and y+r+10<480)):
            output = output[y-r-1:y+r+3, x-r-1:640]
        #x is small
        elif((x<r+10 and y-r-10>0 ) or (x<r+10 and y+r+10<480)):
            output = output[y-r-1:y+r+1, 0:x+r+1]
        else:

            output = output[y-r-1:y+r+1, x-r-1:x+r+1]

        #for visualize only
        #cv.imshow('output',output)
        #cv.waitKey(0)
        #cv.destroyAllWindows()

        # Get target
        target = int(i.stem.split('_')[0])


        #choose your path for crop the coins in classification coins

        cv.imwrite(output_path +'\\' + i.stem + '.jpg', output)


if __name__ == "__main__":
    
    input_classification_path = Path(r'C:\Users\asafs\OneDrive\Desktop\brazilian coins\classification_dataset\all')
    output_classification_path = r'C:\Users\asafs\OneDrive\Desktop\brazilian coins\valid_classification_dataset'
    image_files = list(input_classification_path.glob('*.jpg'))
    
    detect_classification_coins(image_files,output_classification_path)