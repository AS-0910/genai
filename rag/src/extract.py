## read through the entire computer and extract all the data
import os


def extract_data_from_computer(computer_path):
    extracted_data = {}
    for root, dirs, files in os.walk(computer_path):
        for file in files:
            # Only process PDF files
            if file.lower().endswith('.pdf'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'rb') as f:
                        data = f.read()
                        extracted_data[file_path] = data
                except (PermissionError, IsADirectoryError, FileNotFoundError):
                    # Skip files that can't be read
                    pass
    return extracted_data


if __name__ == "__main__":
    # drives = ["C:\\", "D:\\", "E:\\", "F:\\"]
    drives = ["D:\sampleFiles"]
    all_data = {}
    
    for drive in drives:
        if os.path.exists(drive):
            print(f"Extracting from {drive}...")
            data = extract_data_from_computer(drive)
            all_data[drive] = data
            print(f"Extracted {len(data)} files from {drive}")
        else:
            print(f"{drive} does not exist")
    
    print(f"\nTotal data extracted from all drives:")
    for drive, data in all_data.items():
        print(f"{drive}: {data} files")


