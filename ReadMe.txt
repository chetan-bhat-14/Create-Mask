Overview:
    Creating a mask with a Python script that checks if the pixel values in all three channels
    are larger than 200 and returns the number of pixels with values greater than 200
    while processing images in parallel

Requirements:
    Python 3.9
    Run the command below by opening the command prompt in the current path
	Note that this command cannot be executed without Python being installed
	python -m pip install -r ./requirements.txt

Folder Structure:
    inputs
        Folder consisting of sample images
    outputs
        Folder consisting of masked images
    Mask.py
        Python script to create masks
    Readme.txt
    requirements.txt

Usage:
    Provide input images path at "line 47"
    You can change the threshold value on "line 29" (200 is set by default)
    Save the changes and open up a command terminal and type the below command
    python Mask.py