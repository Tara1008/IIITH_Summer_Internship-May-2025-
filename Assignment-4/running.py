import zipfile
import os

zip_path = ' '  # path to your ZIP file
extract_to = '  '  # folder where you want to extract


with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f'Extracted to {extract_to}')
