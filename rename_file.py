import os
import re
from pathlib import Path

# Target directory (current working directory)
target_dir = Path('.')

# Regular expression to match the format: ml1.x.xxx (x can be an integer or a decimal)
pattern = re.compile(r'^ml1\.(\d+(?:\.\d+)?)(\..+)$')

# Start processing
for file in target_dir.iterdir():
    if file.is_file():
        match = pattern.match(file.name)
        if match:
            number_part, ext = match.groups()  
            new_name = f"ml1-1.{number_part}{ext}" # Modify "ml1-1"
            new_path = file.with_name(new_name)

            print(f"Renaming: {file.name} → {new_name}")
            file.rename(new_path)
