import os
import cv2 as cv
import numpy as np
import multiprocessing as mp


def fetch_file_names(path):
    """
    Function to fetch relative filepaths of each file
    :param path: Input path where the files are stored
    :return: List consisting of all filepaths
    """
    file_names = []
    for files in os.listdir(path):
        if files.endswith(('.png', '.jpg', '.jpeg')):
            file_paths = os.path.join(path, files)
            file_names.append(file_paths)

    return file_names


def process_mask_images(input_images_path):
    """
    Function to process each image to implement a mask
    :param input_images_path: File path of each image
    :return: Pixel counts of each with value 255
    """
    output_dir = "outputs"
    threshold = 200
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    image_data = cv.imread(input_images_path)
    # Mask to check if all 3 channels are greater than 200
    mask = np.all(image_data > threshold, axis=2).astype(np.uint8) * 255
    # Fetch the file name
    image_name = input_images_path.split('\\')[-1].split('.')[0]
    cv.imwrite('{}.png'.format(os.path.join(output_dir, image_name)), mask)

    # Calculate total number of pixels with value 255
    pixel_counts = np.sum(mask == 255)

    return pixel_counts


if __name__ == '__main__':
    images_path = r'.//inputs'
    image_files = fetch_file_names(images_path)
    # Process images paralleling
    with mp.Pool() as pool:
        mask_pixels = pool.map(process_mask_images, image_files)

    # Calculate sum of all pixel counts of each image
    total_pixels = sum(mask_pixels)
    print("Total pixel counts with mask values 255: {}".format(str(total_pixels)))
