import os

def create_folders_and_files_from_md(md_file):
    try:
        with open(md_file, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    base_dir = None
    current_path = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if base_dir is None:
            base_dir = line.split('/')[0]
            os.makedirs(base_dir, exist_ok=True)
            print(f"Created base directory: {base_dir}")
            current_path.append(base_dir)
            continue

        depth = line.count('│')
        parts = line.split('── ')

        if len(parts) < 2:
            continue
        
        item = parts[1].strip().split(' # ')[0]

        if depth < len(current_path) - 1:
            current_path = current_path[:depth + 1]
        elif depth > len(current_path) - 1:
            print(f"Error: Invalid structure in line: '{line}'")
            continue
        
        current_dir = os.path.join(*current_path)

        if '.' in item:
            file_path = os.path.join(current_dir, item)
            try:
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        pass
                print(f"Created file: {file_path}")
            except Exception as e:
                print(f"An unexpected error occurred while creating file '{file_path}': {e}")
        
        else:
            current_path.append(item)
            dir_path = os.path.join(current_dir, item)
            try:
                os.makedirs(dir_path, exist_ok=True)
                print(f"Created directory: {dir_path}")
            except Exception as e:
                print(f"An unexpected error occurred while creating directory '{dir_path}': {e}")

if __name__ == '__main__':
    create_folders_and_files_from_md('folder_structure.md')
