# Project_object_detection_JRSB
Object detection workflow using NVIDIA Jetson Nano and GPU acceleration

## Problem Statement
Real-time object detection is one of the key AI tasks in use cases such as autonomous vehicles, surveillance systems, robotics, and industrial automation. It allows to identify and classify objects within images or video streams in real-time. AI inference tasks such as object detection are computationally intensive. Research shows that a higher speed up and lower latency can be achieved by using parallel hardware and optimized software frameworks. Traditionally, such inference tasks have been carried out on powerful cloud-based servers. However, there is a growing demand for low-latency, high-throughput, and real- time performance on embedded edge devices. Embedded devices with AI accelerators provide a powerful compact platform for deploying machine learning inference. They enable AI to run in diverse environments and applications closer to the user and on premise. How would you leverage the capabilities of an accelerator-enabled embedded edge device for a real-time AI inferencing task such as object-detection?

## Reflection
Real-time object detection is an important AI task used in areas like self-driving cars, surveillance systems, robotics, and factory automation. These systems need to identify and classify objects in images or video streams quickly.

Traditional object detection systems depend on cloud computing because deep learning models are complex and require a lot of processing power. However, sending video data to remote servers adds delays and needs a stable internet connection.

Edge computing solves this problem by allowing AI to run directly on embedded devices. Systems with hardware accelerators like GPUs can run machine learning models locally, resulting in less delay and better efficiency.

This project looks at how GPU-accelerated embedded platforms can be used for real-time object detection through optimized deep learning models and parallel computing methods.

### Parallel Computing in AI Inference

Object detection using deep neural networks requires heavy operations such as convolution, matrix multiplication, and tensor transformations. These tasks can be done in parallel.

Graphics Processing Units (GPUs) are ideal for these kinds of workloads because they have hundreds or thousands of cores that can run parallel threads at the same time. By using GPU acceleration, deep learning inference can achieve much higher throughput and reduce latency compared to using only CPUs.

In this project, GPU acceleration is used to process video frames and detect objects in real time.

## Selected Frameworks and Hardware 
### Hardware
- Jetson Nano
- Web camera
### Software
- Pytorch
- OpenCV
- CUDA
- Ultralytics YOLO v5

## Object Detection Model
The *YOLOv5 Nano* was selected since it is optimized for embedded devices, has a fast inference and has real-time performance. 

## Optimization Techniques
- Tiling
- Thread coarsening

## Repository Structure
Workflow/
Reflection/
code/
