import importlib
import subprocess
import GPUtil


def check_memory():
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        if gpu.memoryTotal > 12000:
            return ""
    return "Insufficient GPU graphics memory for use."


def install_detection(requir_path):
    # 读
    file_path = requir_path
    requirements = []
    with open(file_path, 'r') as file:
        for line in file:
            requirements.append(line.strip())

    # 查
    missing_libs = []
    for libs in requirements:
        try:
            importlib.import_module(libs)
        except ImportError:
            missing_libs.append(libs)

    return missing_libs

def print_missing(missing_libs):
    # 返
    if missing_libs == []:
        return ""
    else:
        return f"Not installed libraries: {', '.join(missing_libs)}"