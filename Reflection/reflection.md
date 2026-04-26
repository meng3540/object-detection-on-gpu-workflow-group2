# Reflection & Learning Plan

## Reflection

This project was significantly more challenging than expected. Initially, we assumed that installing PyTorch and running a pre-trained model would be straightforward. However, we quickly realized that working on an embedded GPU system like the Jetson requires careful alignment between software versions.

One of the biggest struggles we encountered was related to compatibility issues between PyTorch, TorchVision, CUDA, and JetPack. We initially installed incorrect versions of PyTorch that were built for CUDA 13, which caused GPU detection to fail. Even when PyTorch appeared to install correctly, TorchVision caused runtime errors such as "operator torchvision::nms does not exist", which prevented Ultralytics from running.

We also faced issues such as:
- Incorrect package installations
- Broken downloads resulting in invalid wheels
- Command-line errors (typos, incorrect flags)
- Import conflicts from local folders
- TorchVision requiring compilation from source
- Long build times during CUDA compilation

These challenges forced us to debug step by step and verify each component individually. We learned that on embedded systems, it is critical to:
- Verify CUDA compatibility
- Use NVIDIA-specific PyTorch builds
- Avoid generic pip installs for GPU frameworks
- Build dependencies like TorchVision manually when needed

Despite the difficulties, We successfully:
- Installed CUDA-compatible PyTorch
- Built TorchVision from source
- Verified GPU acceleration
- Ran real-time object detection using YOLO
- Compared CPU vs GPU performance

This project helped us understand that deploying AI models on hardware is often more complex than developing them. It also improved our troubleshooting skills and taught us how to work with system-level dependencies.

---

## Learning Plan

Through this project, we identified several areas for improvement:

- Better understanding of GPU computing frameworks
- Experience with containerization (Docker for Jetson)
- Knowledge of TensorRT optimization
- Performance profiling techniques
- Managing software dependencies in embedded systems

If this project were scaled for industry use, we would need additional skills in:
- Deployment pipelines
- Real-time optimization
- Hardware-aware AI design
- Model compression and acceleration

To improve, we would explore:
- NVIDIA Jetson documentation
- TensorRT tutorials
- Docker-based AI workflows
- Advanced PyTorch deployment strategies

