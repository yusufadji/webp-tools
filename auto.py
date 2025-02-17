import os
import re
import subprocess


orig_folder = "orig"
dst_folder = "dst"
src_folder = "src"


def extract_number(file_name):
    numbers = re.findall(r'\d+', file_name)
    return int(numbers[0]) if numbers else 0


def compress_images(compression_quality):
    file_list = [file for file in os.listdir(
        orig_folder) if file.endswith((".jpg", ".jpeg", ".png", ".webp"))]
    file_list = sorted(file_list, key=extract_number)

    for file in file_list:
        input_path = os.path.join(orig_folder, file)
        output_path = os.path.join(
            src_folder, os.path.splitext(file)[0] + ".webp")

        command = f"cwebp -q {compression_quality} {input_path} -o {output_path}"
        os.system(command)


def make_webp():
    subprocess.run(["python", "aniwebpmaker.py"])


def get_file_size(file_path):
    return os.path.getsize(file_path)


def auto_compress():
    compression_quality = 50

    while True:
        compress_images(compression_quality)

        make_webp()

        file_list = [file for file in os.listdir(
            dst_folder) if file.endswith(".webp")]
        file_list = sorted(file_list, key=extract_number)
        print(file_list)
        webp_file_path = f"dst/{file_list[0]}"
        file_size = get_file_size(webp_file_path)

        if file_size > 500000:
            compression_quality -= 3
            if compression_quality < 1:
                print("Compression quality has reached below 1. Stopping program.")
                break
            print(f"compression_quality = {compression_quality}")
            os.remove(f"dst/{file_list[0]}")
        else:
            break


auto_compress()