import os

def write_files(files, base_dir="output"):
    os.makedirs(base_dir, exist_ok=True)

    for name, content in files.items():
        with open(os.path.join(base_dir, name), "w") as f:
            f.write(content)
