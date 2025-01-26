# FinetuneAI_Learning

How to fine-tune AI models for undergraduates and beginners (with free GPU resources).

## Introduction

This repository serves as a record of my learning process and the insights I've gained while studying the fine-tuning of AI models. The aim is to create a comprehensive resource that is easy to revisit and can help others understand and implement fine-tuning techniques.
Especially, this aims to help no-local-GPU users to fine-tune AI models effectively with free GPU resources.

---

## Free GPU Resources

In order to train AI models effectively, GPU is essential. However, not everyone has access to a local GPU or the resources to rent one. 

This section provides an overview of free GPU resources available on platforms like Kaggle and Google Colab, along with tips on how to manage these resources efficiently.

### Platforms
The two most popular platforms that offer free GPU resources are [Kaggle](https://www.kaggle.com/) and [Google Colab](https://colab.research.google.com/).

### Getting Started
- You can check my file: [Kaggle](kaggle/getting_started.md) or learn from the original guide.
- You can check my file: [Google Colab](colab/getting_started.md) or learn from the original guide.

### Effective Resource Management
- Although these platforms offer free GPU resources, they come with limitations (time, VRAM, etc.)
- It's important to manage these resources efficiently to avoid interruptions during training.
- Please check these below files for detailed information:
  - [Use Kaggle for small models](kaggle/small_model.md)
  - [Use Kaggle for large models](kaggle/large_model.md)
  - [Use Colab for small models](colab/small_model.md)
  - [Use Colab for large models](colab/large_model.md)

- **TL;DR**:
  - [Kaggle](kaggle): 
    - 30 hours weekly.
    - Fast data/weight uploads and workflows.
    - 1x 16 GB VRAM GPU or 2x 15 GB VRAM GPUs. (Tesla P100 or 2x T4).
  - [Colab](colab):
    - About 3 hours daily.
    - Many example scripts available.
  - Effective mix:
    - Load data on both platforms.
    - Find avaible online scripts (usually written for Colab).
    - Stablize/Debug/Estimate time on Colab.
    - Convert the scripts to Kaggle.
    - Fine-tune models on Kaggle.
      - For large models: Run per epoch and use Kaggle advantage for output workflows. (check [Use Kaggle for large models](kaggle/large_model.md))
      - For small models: Use Colab to experiment (hyperparameter tuning, etc.) and fine-tune in one go on Kaggle.
    - Download weight from Kaggle, upload to Colab and inference (Optional).
---

## Script samples for fine-tuning

Another problems besides the resource management is that there are not many scripts available for fine-tuning AI models. (You can find many scripts for inference, but not for fine-tuning from my experience.)

This section provides some fine-tune scripts for some AI tasks. 
### Computer vision tasks

Please check the [Computer vision script](scripts/cv/README.md) folder for detailed information.

**TL;DR**: I provide scripts for fine-tuning with Torch and TF, and YOLO with Ultralytics.

### NLP tasks

Please check the [NLP script](scripts/llm/README.md) folder for detailed information.

**TL;DR**: I provide scripts for fine-tuning with Hugging Face.

---
## Others

Beside the above sections, I also provide some other useful information for fine-tuning AI models that I have learned from reading cool papers, books, and blogs.

Please check the [Others](others/README.md) folder for detailed information.
---

This repository will continue to grow as I learn more about fine-tuning AI models. Feel free to explore, learn, and contribute! 🚀
