import cv2 as cv
import numpy as np
import os

#######################################################################################
#   Author: Avery Gosselin
#   Date: Nov/21/2022
#   Course: COS 473
#   Assignment: 4
#
#   Description: This is my program to enable the cleaning of the data collected in the
#       Quadrat project. Users may select the four points constituting the corners of an
#       imaged PVC square from top left to bottom right, and then save the corrected image
#       to the data/corrected_images folder.
#######################################################################################

def click(event, x, y, flags, param):
    global cur_point 

    if event == cv.EVENT_LBUTTONDOWN:
        print("click!")
        cur_point = (x,y)
        print(cur_point)

        cv.circle(img, cur_point, 10, (0,0,255), 10)
        cv.imshow(images[0], img)

        pts.append(cur_point)
        print(pts)

def get_images(path):
    full_list = os.listdir(path)
    for i in range(0, len(full_list)):
        full_list[i] = path + full_list[i]
    return full_list

def homography(pts, goal, img):
    pts = np.array([pts])
    h, status = cv.findHomography(pts, goal)
    out = cv.warpPerspective(img, h, (img.shape[1], img.shape[0]))
    return out

def crop(img):
    return img[512:2512, 1016:3016]

def save_img(img):
    path = "data/corrected_images" + images[0][15:]
    cv.imwrite(path, img)


cur_point = (0,0)
#img = None
pts = []
images = get_images('data/to_correct/')
goal_points = np.array([[1016, 512], [3016, 512], [1016, 2512], [3016, 2512]])

while(1):
    if len(images) > 0:
        img = cv.imread(images[0])
        cv.imshow(images[0], img)
        cv.setMouseCallback(images[0], click)

        print("Click 0 key when 4 points selected, to restart, click 0 with more or less than 4 points selected")
        cv.waitKey(0)

        if len(pts) == 4:
            print(pts)
            corrected = homography(pts, goal_points, img)
            corrected = crop(corrected)
            cv.imshow("Corrected", corrected)
            save_img(corrected)
            images = images[1:]

        else:
            print("ERROR: need exactly four points, resetting, please reselect four points.")


        print("Click 0 to continue")
        pts = []
        cv.waitKey(0)
        cv.destroyAllWindows()
    
    else:
        print("No more images to correct!")
        break

cv.destroyAllWindows()