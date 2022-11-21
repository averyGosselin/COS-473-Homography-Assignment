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
Before running, you should replace the images in the to_correct folder with your desired data set. The file names should not matter, so long as they are JPEG format. Once you have all of your desired data here, you may proceed to the next step.

### Running the Program
Once you have stored your desired data, you may then run the program by typing 'python main.py'. Currently, the workflow is: 
1. Select 4 points (corners of PVC square) in displayed uncorrected image, you MUST choose from top left to bottom right, as you would read a book. Press 0 once complete.
2. Corrected image presented to user and saved in data/corrected_images with original file name (press 0 to continue to next image).

**If you would like to restart your point selection for an image**, press 0 key TWICE with either more or less than 4 points in the point list, which will be printed to the console. This will reset the selected points and the image.

Yes it is weird, no it is not that sensible, but it WORKS.

## Sources
- All uncorrected images sourced from Dr. Ken Bundy and Dr. Peter Nelson of the Schoodic Institute

