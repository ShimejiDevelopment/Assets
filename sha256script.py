import os, hashlib

for dir in os.listdir():
    if os.path.isdir(dir) and not dir.startswith('.'):
        for dirpath,dirnames,filenames in os.walk(dir):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                if os.path.isfile(file_path) and not file_path.endswith('.sha256'):
                    with open(file_path, "rb") as f:
                        bytes = f.read() 
                        readable_hash = hashlib.sha256(bytes).hexdigest();
                    with open(file_path + ".sha256", "w") as hash_file:
                        hash_file.write(f"{readable_hash}")