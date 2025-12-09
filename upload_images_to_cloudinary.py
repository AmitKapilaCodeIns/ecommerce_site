import os
import cloudinary
import cloudinary.uploader

# ✅ Configure Cloudinary
cloudinary.config(
    cloud_name="dra4ze9d3",       # your cloud name
    api_key="822456757969153",     # your API key
    api_secret="8T5hIRhlMtLgvra-T8R25bZ2SMY",  # your API secret
    secure=True
)

# ✅ Directory with your local images
MEDIA_DIR = "./media"

# ✅ Supported image extensions
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}

# ✅ Dictionary to store filename → public_id mapping
mapping = {}

print("Uploading images...\n")

for filename in os.listdir(MEDIA_DIR):
    filepath = os.path.join(MEDIA_DIR, filename)

    # Skip hidden or non-image files
    if filename.startswith(".") or os.path.splitext(filename.lower())[1] not in IMAGE_EXTENSIONS:
        print(f"Skipping non-image file: {filename}")
        continue

    print(f"Uploading: {filename}")

    # Use the filename (without extension) as Cloudinary public_id
    public_id = f"products/{os.path.splitext(filename)[0]}"

    result = cloudinary.uploader.upload(
        filepath,
        public_id=public_id,
        overwrite=True,
        unique_filename=False
    )

    mapping[filename] = result["public_id"]
    print(f"Uploaded: {filename} → public_id={result['public_id']}")

# ✅ Print mapping for use in products.json
print("\n--- FILE NAME → CLOUDINARY PUBLIC_ID MAPPING ---")
for local_file, public_id in mapping.items():
    print(f"{local_file} → {public_id}")

