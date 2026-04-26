Camera
  ↓
  Frame Capture (OpenCV)
    ↓
    Image preporcessing
     ↓
     Object detection model
      ↓
      Inference Output(the boxes detected) 
       ↓
       Drawing boundign boxes 
        ↓ 
        Displaying annotated video
         ↓
         Measure FPS
         
# 📄 `Workflow/workflow.md`

```markdown
# Workflow - Object Detection on GPU Edge Device

## System Overview
Camera → OpenCV → YOLOv8 Model → GPU (CUDA) → Bounding Boxes → Display

---

## Step 1: Verify System

```bash
python3 --version
dpkg -l | grep nvidia-jetpack
cat /etc/nv_tegra_release
nvcc --version

## Step 2: Install Dependencies
sudo apt-get update
sudo apt-get install -y python3-pip libopenblas-dev python3-opencv git build-essential libjpeg-dev zlib1g-dev libpython3-dev

## Step 3: Install Python Packages
python3 -m pip install --upgrade pip
python3 -m pip install numpy==1.26.1

## Step 4: Install cuSPARSELt
cd ~
rm -rf cusparselt-install
mkdir cusparselt-install
cd cusparselt-install

wget https://developer.download.nvidia.com/compute/cusparselt/redist/libcusparse_lt/linux-aarch64/libcusparse_lt-linux-aarch64-0.8.0.4_cuda12-archive.tar.xz
tar -xvf libcusparse_lt-linux-aarch64-0.8.0.4_cuda12-archive.tar.xz
cd libcusparse_lt-linux-aarch64-0.8.0.4_cuda12-archive

sudo cp -av lib/* /usr/local/cuda/lib64/
sudo cp -av include/* /usr/local/cuda/include/
sudo ldconfig

## Step 5: Install PyTorch
export TORCH_INSTALL=https://developer.download.nvidia.com/compute/redist/jp/v61/pytorch/torch-2.5.0a0+872d972e41.nv24.08.17622132-cp310-cp310-linux_aarch64.whl
python3 -m pip install --no-cache-dir "$TORCH_INSTALL"

## Step 6: Verify PyTorch GPU
python3 -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.device_count())"

## Step 7: Install TorchVision
cd ~
rm -rf vision
git clone --branch v0.20.0 --depth 1 https://github.com/pytorch/vision.git
cd vision

export BUILD_VERSION=0.20.0
export FORCE_CUDA=1
python3 -m pip install --user --no-build-isolation -v .

## Step 8: Install Ultralytics
python3 -m pip install --user -U ultralytics

## Step 9: Verify Installation
python3 -c "import torchvision; print(torchvision.__version__)"
python3 -c "from ultralytics import YOLO; print('ultralytics ok')"

## Step 10: Run Detection
python3 code/detect_gpu.py

## Step 11: Monitor GPU
jtop

CPU vs GPU Comparison
GPU
●	Low latency
●	High FPS
●	Real-time detection
●	GPU utilization visible in jtop
CPU
●	High latency
●	Low FPS
●	Not real-time
●	High CPU usage
Screenshots to Include
●	JetPack version
●	Torch CUDA True
●	GPU detection output
●	CPU detection output
●	jtop GPU usage

---
