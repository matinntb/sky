import cv2
import time
import numpy as np
from pygame import mixer

mixer.init()
mixer.music.load('piano1.mp3')
mixer.music.play()
font1 = cv2.FONT_HERSHEY_SIMPLEX
################## stars ####################
w,h = 640,480
stars = np.random.uniform(-1200,1200,(200,3)) 
############### Background ##################
canvas=np.zeros((700,700,3),dtype="uint8")
c=(180,180,0)
################## Sun ######################

img2 = cv2.imread("sun.png", -1)

def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(282,280))

################### Mercury #################

#Mercury line
cv2.circle(canvas,(350,350),70,(94,91,90),thickness=0)

img2 = cv2.imread("mercury.png", -1)

def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(345,398))

################### Venus ###################

# Venus line
cv2.circle(canvas,(350,350),100,(94,91,90),thickness=0)

#venus
img2 = cv2.imread("venus.png", -1)

def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(260,400))

################### Earth ####################

# Earth line
cv2.circle(canvas,(350,350),140,(94,91,90),thickness=0)

#earth
img2 = cv2.imread("earth.png", -1)
def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(460,290))
################### Mars ######################

# Mars line
cv2.circle(canvas,(350,350),183,(94,91,90),thickness=0)

# Mars 
img2 = cv2.imread("mars.png", -1)
def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(320,143))

################## Jupiter ####################

# Jupiter line
cv2.circle(canvas,(350,350),230,(94,91,90),thickness=0)

# Jupiter
img2 = cv2.imread("jupiter.png", -1)
def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(120,186))
################### Saturn ###################

# Saturn line
cv2.circle(canvas,(350,350),270,(94,91,90),thickness=0)

# Saturn
img2 = cv2.imread("Saturn.png", -1)
def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(489,148))

################### Uranus ######################
# Uranus line
cv2.circle(canvas,(350,350),310,(94,91,90),thickness=0)

# Uranus

img2 = cv2.imread("Uranus.png", -1)

def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(515,550))

#################### Neptune #####################

#Neptune line
cv2.circle(canvas,(350,350),350,(94,91,90),thickness=0)

#Neptune
img2 = cv2.imread("neptune.png", -1)

def AddImage(img1,img2,pos):

    x_offset=pos[0]
    y_offset=pos[1]

    y1, y2 = y_offset, y_offset + img2.shape[0]
    x1, x2 = x_offset, x_offset + img2.shape[1]

    alpha_s = img2[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        img1[y1:y2, x1:x2, c] = (alpha_s * img2[:, :, c] + alpha_l * img1[y1:y2, x1:x2, c])
    return img1
canvas = AddImage(canvas,img2,(180,645))

######################################################
num_rows, num_cols = canvas.shape[:2]
######################################################
i=0
while True:
    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), i+0.1, 1)
    img_rotation = cv2.warpAffine(canvas, rotation_matrix, (num_cols, num_rows))
    stars[:,2] = (stars[:,2] - 0.01) % 5.0
    for x,y,z in stars:        
        c = int(255/(z+1))
        cv2.circle(img_rotation, (int(x/z+w/2),int(y/z+h/2)), int(1.0/z+1), (255,255,255), thickness=-1) 
    t = time.strftime('%H:%M:%S')
    textsize = cv2.getTextSize(t, font1, 1, 2)[0]
    img = cv2.putText(img_rotation,t,(img_rotation.shape[1]-120,img_rotation.shape[0] - 10),font1,0.7,(255,255, 255),2)  
    img = cv2.putText(img,"Nematbakhsh",(10,img_rotation.shape[0] - 10),font1,0.7,(255,255, 255),2)
    cv2.rectangle(img, (562, 667), (694, 696),(187,189,191))
    cv2.rectangle(img, (5, 667), (166, 696),(187,189,191))
    
    cv2.imshow('sky', img)
    i+=0.3
    k=cv2.waitKey(150)
    if k==13:
        break 
mixer.music.pause()
cv2.destroyAllWindows()