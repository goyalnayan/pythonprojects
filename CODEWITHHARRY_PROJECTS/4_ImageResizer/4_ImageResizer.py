# alt + shift + above

import cv2
src = cv2.imread("nayan.jpg", cv2.IMREAD_UNCHANGED)
cv2.imshow("title", src)
cv2.waitKey(0)


import cv2
# Configurable Parameters
source = "nayan.jpg"
destination = "newImage.jpeg"
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", src)

# percent by which the image is resized

# calculate the 50 percent of dimensional dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

#resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0)

