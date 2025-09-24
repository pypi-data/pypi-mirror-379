from setuptools import setup, find_packages

setup(
    name="mahesh",
    version="0.3.0",
    description="Convert YOLO .pt models to ONNX and TensorRT engines easily 🚀",
    author="Mahi",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/yolo2trt",
    packages=find_packages(),
    install_requires=[
        "ultralytics>=8.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "yolo2trt=yolo2trt.exporter:pt_to_trt",
        ],
    },
    python_requires=">=3.8",
)

