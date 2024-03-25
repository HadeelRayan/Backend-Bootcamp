from PIL import Image
import time


def main():

    image_path = 'img1.jpg'
    original_image = Image.open(image_path)
    start_time = time.time()

    # Perform the color inversion
    inverted_image = Image.eval(original_image, lambda x: 255 - x)

    end_time = time.time()
    execution_time_single_thread = end_time - start_time

    inverted_image.save('inverted_img1.jpg')

    print(execution_time_single_thread)


if __name__ == "__main__":
    main()