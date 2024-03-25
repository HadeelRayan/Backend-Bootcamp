from PIL import Image
import numpy as np
import time
from multiprocessing import Pool, cpu_count

# Adjust configuration to avoid DecompressionBombError
Image.MAX_IMAGE_PIXELS = None

def invert_segment(segment):
    # Invert the segment's colors and convert to an array
    return 255 - np.array(segment)

# Function to process the image using multiprocessing
def process_image_multiprocess(image, n_processes=None):
    # Determine the number of processes to use
    if n_processes is None:
        n_processes = cpu_count()

    # Calculate the height of each segment based on the number of processes
    width, height = image.size
    segment_height = height // n_processes

    # Define a list to hold data for each segment
    segments_data = []

    # Split the image into segments for processing
    for i in range(n_processes):
        left = 0
        top = i * segment_height
        right = width
        bottom = (i + 1) * segment_height if i < n_processes - 1 else height
        segment = image.crop((left, top, right, bottom))
        segments_data.append(segment)

    # Start the multiprocessing pool and map the invert_segment function to each image segment
    with Pool(processes=n_processes) as pool:
        result_segments = pool.map(invert_segment, segments_data)

    # Combine the segments back into a single image
    new_image = Image.new('RGB', (width, height))
    for i, segment_array in enumerate(result_segments):
        segment_image = Image.fromarray(segment_array.astype('uint8'), 'RGB')
        new_image.paste(segment_image, (0, i * segment_height))

    return new_image


def main():
    start_time_multi = time.time()
    original_image = Image.open('img1.jpg')
    processed_image_multi = process_image_multiprocess(original_image)
    end_time_multi = time.time()
    execution_time_multi = end_time_multi - start_time_multi

    inverted_image_multi_path = 'inverted_img1_multi.jpg'
    processed_image_multi.save(inverted_image_multi_path)

    print(execution_time_multi)


if __name__ == "__main__":
    main()