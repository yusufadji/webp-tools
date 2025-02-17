import os


# workspace setup
orig_folder = "orig"
src_folder = "src"


# preferences
compression_quality = 50


if not os.path.exists(src_folder):
    os.makedirs(src_folder)


file_list = [file for file in os.listdir(orig_folder) if file.endswith((".jpg", ".jpeg", ".png", ".webp"))]


for file in file_list:
    input_path = os.path.join(orig_folder, file)
    output_path = os.path.join(src_folder, os.path.splitext(file)[0] + ".webp")


    command = f"cwebp -q {compression_quality} {input_path} -o {output_path}"
    os.system(command)