

import os

def delete_files_in_directory(directory_path, ignore=[]):
   try:
     files = os.listdir(directory_path)
     filtered_files = C = list(set(files) - set(ignore))
     for file in filtered_files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
     print(f"\nAll files in path [{directory_path}] were deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")