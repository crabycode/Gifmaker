import os
import imageio.v3 as iio

image_dir = "D:\\coding\\Python\\GIF"
filenames = os.listdir(image_dir)
images = []
for file in filenames:
    if file.endswith('.png'):
        full_path = os.path.join(image_dir, file)
        try:
            images.append(iio.imread(full_path))
        except Exception as e:
            print("Error reading " + file + ": " + str(e))
if images:
    output_filename = "amogus2.gif"
    full_output_path = os.path.join(image_dir, output_filename)
    try:
        iio.imwrite(full_output_path, images, duration=1.0, loop=0)
        print("GIF saved successfully at " + full_output_path)
    except Exception as e:
        print("Failed to save GIF: " + str(e))
else:
    print("No images were processed.")