import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob


def intersect(r1, r2, percentage):
    [ax1, ay1, ax2, ay2] = r1
    [bx1, by1, bx2, by2] = r2
    dx = min(ax2, bx2) - max(ax1, bx1)
    dy = min(ay2, by2) - max(ay1, by1)
    if (dx >= 0) and (dy >= 0):
        s1 = (ax2-ax1)*(ay2-ay1)
        if dx*dy > percentage*s1:
            return [min(ax1, bx1), min(ay1, by1), max(ax2, bx2), max(ay2, by2)]
    return None


tm = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

#cv2.namedWindow("Image", cv2.WINDOW_NORMAL) 

template = cv2.imread('../reference/logo7.jpg', 0)
template = cv2.resize(template, (500, 500))
(tH, tW) = template.shape[:2]

for imagePath in glob.glob('../data' + "/*.jpg"):
    image = cv2.imread(imagePath)
    if (image.shape[1] > 800) or (image.shape[0] > 800):
        image = cv2.resize(image, (800, int(image.shape[0]*(800/image.shape[1]))))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    i_edges = cv2.Canny(gray, 50, 200)
    cv2.imshow("edges", i_edges)
    found = None

    # loop over the scales of the image
    rect_list = []
    rect_count = {}
    for scale in np.linspace(0.03, 1.0, 300)[::-1]:
        resized = cv2.resize(template, (int(tW * scale), int(tH * scale)))
        r = float(resized.shape[1]) / template.shape[1]
        if resized.shape[0] > gray.shape[0] or resized.shape[1] > gray.shape[1]:
            continue

        t_edges = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(i_edges, t_edges, tm[3]) # 1-0.1, 3-0.2
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
        if maxVal > 0.35:
            #print(maxVal, scale)
            (x1, y1) = (maxLoc[0], maxLoc[1])
            (x2, y2) = (maxLoc[0] + resized.shape[0], maxLoc[1] + resized.shape[1])
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            exist = False
            for i in range(len(rect_list)):
                new_rect = intersect([x1, y1, x2, y2], rect_list[i], 0.5)
                if new_rect is not None:
                    rect_count[i] += 1
                    rect_list[i] = new_rect
                    if rect_count[i] >= 3:
                        cv2.rectangle(image, (new_rect[0], new_rect[1]), (new_rect[2], new_rect[3]), (0, 255, 0), 2)
                    exist = True
                    break
            if not exist:
                rect_list.append([x1, y1, x2, y2])
                rect_count[rect_list.index([x1, y1, x2, y2])] = 1
                
                    
            #if found is None or maxVal > found[0]:
            #    found = (maxVal, maxLoc, r)
            #cv2.imshow("Image", image)
        #cv2.imshow("template", t_edges)
        #k = cv2.waitKey(1) & 0xff
        #if k == ord('q'):
        #    exit()
    #count = []
    #for (val, loc, r) in rect_list:
    #    #(startX, startY) = (int(loc[0]), int(loc[1]))
    #    #(endX, endY) = (int((loc[0] + tW*r)), int((loc[1] + tH*r)))
    #    #count.append()
    #    cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

    #cv2.resizeWindow('Image', int(image.shape[1]/3), int(image.shape[0]/3))
    cv2.imshow("Image", image)
    k = cv2.waitKey(0) & 0xff
    if k == ord('q'):
        exit()
