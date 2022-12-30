import cv2

# Doc anh Foreground
fg = cv2.imread('./Images/bird-thumbnail.jpg');
print(fg.shape);

# Doc anh effect
eff = cv2.VideoCapture("./Images/200w.gif");

# 