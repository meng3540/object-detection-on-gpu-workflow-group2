# Object Detection Workflow on NVIDIA Jetson (GPU Edge Device)

## Overview
This project demonstrates a complete workflow for real-time object detection inference on an embedded GPU platform using an NVIDIA Jetson device. The system captures live video from a camera, processes frames using a pre-trained YOLOv8 model, and displays bounding boxes and labels.

Object detection inference is a parallel computation problem because multiple convolution operations and feature extractions are performed simultaneously across image data. This type of workload benefits significantly from GPU acceleration.

## Hardware
- NVIDIA Jetson Orin Nano (JetPack 6.2)
- USB Camera

## Software & Frameworks
- Python 3.10
- PyTorch (NVIDIA Jetson build)
- TorchVision (compiled from source)
- Ultralytics YOLOv8
- OpenCV
- CUDA 12.6

## Pre-trained Model
- YOLOv8n (lightweight model for real-time embedded inference)

## Key Features
- GPU-accelerated inference using CUDA
- Real-time camera detection
- CPU vs GPU performance comparison
- Complete reproducible setup workflow

## Repository Structure
.
├── code/
├── Workflow/
├── Reflection-Learning-Plan/
└── README.md

---

## Results Summary

| Device | Latency | FPS | Observation |
|--------|--------|-----|------------|
| CPU | High | Low | Not suitable for real-time |
| GPU | Low | High | Real-time capable |
