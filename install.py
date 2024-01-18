import os
import launch

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

req_file = os.path.join(BASE_PATH, "requirements.txt")

with open(req_file) as file:
    for lib2 in file:
        lib2 = lib2.strip()
        if not launch.is_installed(lib2):
            launch.run_pip(
                f"install {lib2}",
                f"sd-webui-segment-anything requirement: {lib2}")
