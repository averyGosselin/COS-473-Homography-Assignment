# Homographinder

## Description
This project was completed by Avery Gosselin for an assignment in COS 473 at the University of Maine in Orono. With this tool, users will be able to compile a list of images to be corrected (homographized into a square) following a simply, marginally intuitive process.

## Installation
### Dependencies
- OpenCV (4.6)
- Numpy (1.23.4)

To install this program, clone the repository and ensure that the dependencies are installed. This may or may not work with other versions of both OpenCV and Numpy, I am not sure (let me know!).

## Usage
### Setup
Before running, you should replace the images in the to_correct folder with your desired data set. The file names should not matter, so long as they are JPEG format. Once you have all of your desired images here, you may proceed to the next step.

### Running the Program
Once you have stored your desired data, you may then run the program by typing 'python main.py'. Currently, the workflow is: 
1. The system will present an image to the user
2. User should select the 4 corners of the PVC square **from top left to bottom right (as you would read a book)**. 
    - IF YOU WOULD LIKE TO RESTART, select more or less than 4 points (the number of points will be written to the console while running) and press the 0 key twice. This will reset the point list and allow you to reselect the points in the image.
3. Once 4 points have been selected, press 0.
4. The system will display the corrected image and automatically save it to the data/corrected_images folder
5. After appreciating the beauty of the corrected image, press 0 to proceed to the next image.
6. Loop until all images from the to_correct folder have been corrected (or kill the process to stop)

## Sources
- All uncorrected images sourced from Dr. Ken Bundy and Dr. Peter Nelson of the Schoodic Institute

