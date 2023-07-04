import cv2
image = cv2.imread('C:\\Users\\patha\\OneDrive\\Pictures\\lakshmi.png')
image_height, image_width, _ = image.shape
rectangle_width = 400
rectangle_height = 300
center_x = image_width // 2
center_y = image_height // 2
bottom_left_x = center_x - rectangle_width // 2
bottom_left_y = center_y + rectangle_height // 2
top_right_x = bottom_left_x + rectangle_width
top_right_y = bottom_left_y - rectangle_height
color = (0, 255, 0)
thickness = 2
cv2.rectangle(image, (bottom_left_x, bottom_left_y), (top_right_x, top_right_y), color, thickness)
cv2.imshow('Rectangle at Center', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
