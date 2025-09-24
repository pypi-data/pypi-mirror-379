import zipfile
import sys
import site
import shutil
import os

def install_wheel(wheel_path):
    print(f"Installing wheel: {wheel_path}")
    with zipfile.ZipFile(wheel_path, 'r') as zip_ref:
        temp_dir = os.path.join(os.getcwd(), "_modfinder_temp")
        zip_ref.extractall(temp_dir)

    site_packages = site.getusersitepackages()
    for item in os.listdir(temp_dir):
        src = os.path.join(temp_dir, item)
        dst = os.path.join(site_packages, item)

        if os.path.exists(dst):
            print(f"Skipped: {item} (already exists)")
        else:
            shutil.move(src, dst)
            print(f"Installed: {item}")

    shutil.rmtree(temp_dir)
    print("Installation complete!")