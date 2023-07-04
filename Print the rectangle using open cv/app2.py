import cv2
image = cv2.imread('C:\\Users\\patha\\OneDrive\\Pictures\\lakshmi.png')
image_height, image_width, _ = image.shape
rectangle_width = 200
rectangle_height = 100
bottom_left_x = image_width - rectangle_width
bottom_left_y = image_height // 2 + rectangle_height // 2
top_right_x = image_width
top_right_y = image_height // 2 - rectangle_height // 2
color = (0, 255, 0)
thickness = 2
cv2.rectangle(image, (bottom_left_x, bottom_left_y), (top_right_x, top_right_y), color, thickness)
cv2.imshow('Rectangle on Right Side', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
