import importlib
import subprocess
import GPUtil


def check_memory():
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        if gpu.memoryTotal > 12000:
            return ""
    return "Insufficient GPU graphics memory for use."


def read_requirements(file_path):
    requirements = []
    with open(file_path, 'r') as file:
        for line in file:
            requirements.append(line.strip())

    return requirements

def check_lib(requirements):
    missing_libs = []
    for libs in requirements:
        try:
            importlib.import_module(libs)
        except ImportError:
            missing_libs.append(libs)
    return missing_libs

def install_detection():
    requir = read_requirements("./install_script/check.txt")
    miss = check_lib(requir)
    if miss == []:
        output = "All listed libraries are installed."
    else:
        output = f"Not installed libraries: {', '.join(miss)}"
    return output

subprocess.run(['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', './install_script/check_install.ps1'],shell=True)