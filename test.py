import cv2 as cv
import os
import cvzone as cvz
bluemarker = cv.imread(os.path.abspath("inmapapp/static/inmapapp/MarkerBlue.png"),cv.IMREAD_UNCHANGED)
redmarker = cv.imread(os.path.abspath("inmapapp/static/inmapapp/MarkerRed.png"),cv.IMREAD_UNCHANGED)
bluemarker = cv.resize(bluemarker, (50, 50), None, 0.3, 0.3)
redmarker = cv.resize(redmarker, (50, 50), None, 0.3, 0.3)
base_img = cv.imread(os.path.abspath(f'inmapapp/static/inmapapp/floor1.png'))
redmarkerplot = cvz.overlayPNG(base_img , redmarker, [327,111])
cv.imwrite(os.path.abspath(f'inmapapp/static/inmapapp/modfloor1.png'), redmarkerplot)