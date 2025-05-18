import os
import json

# Set the folder where your images live
image_folder = "assets/images"

# Valid image file extensions
valid_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp'}

# List all image files
image_files = [
    filename for filename in os.listdir(image_folder)
    if os.path.splitext(filename)[1].lower() in valid_extensions
]

# Output path
output_path = os.path.join("assets", "imageList.json")

# Save the list
with open(output_path, 'w') as json_file:
    json.dump(image_files, json_file, indent=2)

print(f"✅ Found {len(image_files)} image(s). Saved to {output_path}")
