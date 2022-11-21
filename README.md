<h1>Homographinder</h1>

<br>
<h2>Description</h2>
<p>This project was completed by Avery Gosselin for an assignment in COS 473 at the University of Maine in Orono. With this tool, users will be able to compile a list of images to be corrected (homographized into a square) following a simply, marginally intuitive process.</p>

<br>
<h2>Installation</h2>
<h3>Dependencies</h3>
<ul>
    <li>OpenCV (4.6)</li>
    <li>Numpy (1.23.4)</li>
</ul>
<p>To install this program, clone the repository and ensure that the dependencies are installed. This may or may not work with other versions of both OpenCV and Numpy, I am not sure (let me know!).</p>

<br>
<h2>Usage</h2>
<h3>Set Up</h3>
<p>Before running, you should replace the images in the to_correct folder with your desired data set. The file names should not matter, so long as they are JPEG format (or maybe other formats, I haven't tested very much...). Once you have all of your desired data here, you may proceed to the next step.</p>
<h3>Running the Program</h3>
<p>Once you have stored your desired data, you may then run the program by typing <code>python main.py</code>. Currently, the workflow is: 
<ol>
    <li>Select 4 points (corners of PVC square) in displayed uncorrected image, you MUST choose from top left to bottom right, as you would read a book. Press 0 once complete.</li>
    <li>Corrected image presented to user and saved in data/corrected_images with original file name (press 0 to continue to next image).</li>
</ol>

<strong>If you would like to restart your point selection for an image</strong>, press 0 key TWICE with either more or less than 4 points in the point list, which will be printed to the console. This will reset the selected points and the image.

Yes it is weird, no it is not that sensible, but it WORKS.
</p>

<h2>Sources</h2>
<ul>
    <li>All uncorrected images sourced from Dr. Ken Bundy and Dr. Peter Nelson of the Schoodic Institute</li>
</ul>