import cv2

def capture_photo(folder_path, file_name):
    # Open the camera
    camera = cv2.VideoCapture(0)

    # Capture a frame
    _, frame = camera.read()

    # Release the camera
    camera.release()

    # Save the image
    file_path = f"{folder_path}/{file_name}.jpg"
    cv2.imwrite(file_path, frame)

    print(f"Photo saved at: {file_path}")

# Prompt the user for folder path and file name
folder_path = input("Enter the folder path to save the photo: ")
file_name = input("Enter the file name for the photo: ")

# Capture and save the photo
capture_photo(folder_path, file_name)
