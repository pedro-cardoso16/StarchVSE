import os
import zipfile

def build_zip(zip_name, nested=False):
    # Clean up old build if it exists
    if os.path.exists(zip_name):
        print(f"Removing old {zip_name}...")
        os.remove(zip_name)
        
    print(f"Generating {zip_name}...")
    
    files_to_include = [
        "blender_manifest.toml",
        "__init__.py",
        "LICENSE",
        "README.md"
    ]
    directories_to_include = [
        "src"
    ]
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        
        # 1. Add individual files
        for filename in files_to_include:
            if os.path.exists(filename):
                # If nested, place under 'starch_vse/' parent folder
                archive_path = os.path.join("starch_vse", filename) if nested else filename
                print(f"  -> {archive_path}")
                zip_file.write(filename, arcname=archive_path)
                
        # 2. Add source directory files
        for directory in directories_to_include:
            if os.path.exists(directory):
                for root, dirs, files in os.walk(directory):
                    for file in files:
                        if "__pycache__" in root or file.endswith(".pyc"):
                            continue
                            
                        full_filepath = os.path.join(root, file)
                        relative_filepath = os.path.relpath(full_filepath)
                        
                        # If nested, place under 'starch_vse/src/...'
                        archive_path = os.path.join("starch_vse", relative_filepath) if nested else relative_filepath
                        print(f"  -> {archive_path}")
                        zip_file.write(full_filepath, arcname=archive_path)

if __name__ == '__main__':
    # 1. Build the legacy package (Blender 4.1 and older)
    # Wraps everything in a 'starch_vse/' parent folder inside the zip
    build_zip("StarchVSE_legacy.zip", nested=True)
    
    print("-" * 50)
    
    # 2. Build the modern extension package (Blender 4.2+)
    # Keeps files flat at the root of the zip next to the manifest
    build_zip("StarchVSE_extension.zip", nested=False)
    
    print("\nAll builds compiled successfully!")