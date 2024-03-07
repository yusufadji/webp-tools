import os


src_folder = "src"
dst_folder = "dst"
orig_folder = "orig"


if not os.path.exists(src_folder):
    os.makedirs(src_folder)
else:
    print(f"{src_folder} directory already exists.")
    
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)
else:
    print(f"{dst_folder} directory already exists.")

if not os.path.exists(orig_folder):
    os.makedirs(orig_folder)
else:
    print(f"{orig_folder} directory already exists.")