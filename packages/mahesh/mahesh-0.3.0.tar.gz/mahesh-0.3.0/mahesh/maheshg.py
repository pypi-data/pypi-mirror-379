def love(name):
    print("❤️😍"*20)
    print("\n")
    hearts = "❤️  " * 3
    return f"Dear {name}, I ❤️   you choo much..{hearts}!\n\n {"❤️😍"*20}"
def greet(names):
    print("#"*30)
    greetings=f"hello {names}...from yours mahesh.have a good day"
    return greetings

import subprocess
from ultralytics import YOLO
import webbrowser
import shutil
def install_tensorrt_windows(onnx_model_path,engine_model_path,fp16):
    """
    Open NVIDIA official TensorRT download page in default browser
    """
    url = "https://developer.nvidia.com/nvidia-tensorrt-download"
    print("🌐 Opening NVIDIA TensorRT official download page...")
    webbrowser.open(url)
    print("👉 Please download the ZIP that matches your CUDA version (e.g., CUDA 11.x).")
    PATH=input("Enter the trtexec file path:")
    if PATH:
        try:       
            cmd = [
                PATH,
                f"--onnx={onnx_model_path}",
                f"--saveEngine={engine_model_path}",
                "--workspace=2048"
            ]

            if fp16:
                cmd.append("--fp16")

            subprocess.run(cmd, check=True)
            print(f"✅ Converted {onnx_model_path} → {engine_model_path}")
            return engine_model_path
        except Exception as e:
            print(e)




def convert_pt_to_onnx(pt_model_path: str, onnx_model_path: str = None, opset: int = 12):
    """
    Convert YOLO .pt model to ONNX format using Ultralytics
    """
    model = YOLO(pt_model_path)
    if onnx_model_path is None:
        onnx_model_path = pt_model_path.replace(".pt", ".onnx")

    model.export(format="onnx", opset=opset)
    print(f"✅ Converted {pt_model_path} → {onnx_model_path}")
    return onnx_model_path


def convert_onnx_to_tensorrt(onnx_model_path: str, engine_model_path: str = None, fp16: bool = True):
    """
    Convert ONNX model to TensorRT engine using trtexec
    """
     # full path to trtexec.exe

    if engine_model_path is None:
        engine_model_path = onnx_model_path.replace(".onnx", ".engine")
    
    try:       
        cmd = [
                "trtexec",
                f"--onnx={onnx_model_path}",
                f"--saveEngine={engine_model_path}",
                "--workspace=2048"
            ]

        if fp16:
                cmd.append("--fp16")

        subprocess.run(cmd, check=True)
        print(f"✅ Converted {onnx_model_path} → {engine_model_path}")
        return engine_model_path
    except Exception as e:
            print(e)
            if not shutil.which("trtexec"):
                print("❌ TensorRT not found. Please install TensorRT and add trtexec to PATH.")
                enter=input("do you want to install TensorRT? Yes(y) or No(n): ")
                if enter=="y":
                    try:
                        install_tensorrt_windows(onnx_model_path,engine_model_path,fp16)
                    except:
                        print("""we are unable to install it directly,link may have changed.please install TensorRT from Nvidia official site ,to continue conversion""")        
                elif enter=="n":
                    print("""please install TensorRT from Nvidia official site ,to continue conversion""")
            
            



def pt_to_trt(pt_model_path: str, fp16: bool = True):
    """
    Full pipeline: .pt → .onnx → .engine
    """
    onnx_path = convert_pt_to_onnx(pt_model_path)
    engine_path = convert_onnx_to_tensorrt(onnx_path, fp16=fp16)
    return engine_path





