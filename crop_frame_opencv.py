import cv2
DIMENSIONS = 640

# Read Input Image
img = cv2.imread("../_videos/c-08-frames-opencv/frame0-02-38.56.jpg")
rows = img.shape[0]
columns = img.shape[1]

row_start = int((rows - DIMENSIONS)/2)
row_end = row_start + DIMENSIONS
column_start = int((columns - DIMENSIONS)/2)
column_end = column_start + DIMENSIONS
cropped = img[row_start:row_end, column_start:column_end]



# Check the type of read image
print(type(img))
print(img.shape)
print(type(cropped))
print(cropped.shape)

# Display the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('cropped', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
