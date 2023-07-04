import cv2

# Step 1: Read or create an image
image = cv2.imread('C:\\Users\\patha\\OneDrive\\Pictures\\lakshmi.png')

# Step 2: Define the rectangle parameters
top_left = (100, 200)   
bottom_right = (300, 250)  

# Step 3: Draw the rectangle
color = (0, 255, 0)  
thickness = 2       
cv2.rectangle(image, top_left, bottom_right, color, thickness)

# Step 4: Display the image with the rectangle
cv2.imshow('Rectangle', image)

# Step 5: Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
