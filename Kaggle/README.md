# Fine-tuning on Kaggle

## Introduction
This guide is a summary of my learnings and experiences from using Kaggle for AI competitions. Please note that some information may be subject to change and may not always be up-to-date.

This repository is geared toward those looking to minimize costs, so no need to worry about GPU expenses.

## Getting Started with Kaggle
### Setting Up Kaggle

1. **Create an Account**: Register for an account on Kaggle.
2. **Identity Verification**:
   - Go to **Profile > Settings**.
   - Complete **Phone Verification** by adding and verifying your phone number.
   - Complete **Identity Verification** by scanning your face.

### Creating a New Notebook

- Create your first notebook by selecting **Create > New Notebook**.
- Kaggle notebooks support Jupyter-style shortcuts and magic commands.
- Notebooks save automatically, and you can upload your own `.ipynb` files.

![Upload notebook](image/upload_notebook.png)

### Enabling GPU in Kaggle
To enable GPU in your Kaggle notebook, follow these steps:

1. **Verify Identity**: Ensure you have completed identity verification as described [above](#setting-up-kaggle).

2. **Enable GPU**: You have two options to activate the GPU in your notebook:

   - **Option 1**:
     - Open **Settings** in your notebook.
     - Under **Accelerator**, select **GPU**.

![Enable GPU in settings](image/enable_gpu_1.png)

- **Option 2**:
  - Click the button in the lower right corner of your notebook interface.
  - In **Session Options**, go to **Accelerator** and select **GPU**.

<div style="display: flex; justify-content: space-between;background-color:grey;height:500px;">
    <img src="image/button.png" alt="view version" style="width: 30%; ; margin-left: 20px;">
    <img src="image/enable_gpu_2.png" alt="version history" style="width: 40%; height:70%; margin-right:50px">
</div>

### Available Resources

- **Accelerator Options**:
  - 2x GPU T4 (15GB each), GPU P100 (16GB), TPU VM v3-8
  - 30 hours per week, reset every Saturday
- **System Specs**:
  - Disk: HDD 58GB
  - RAM: 29GB
  - CPU: 4 cores
- **Session Limit**: 12 hours per session

Resource usage can be monitored in the top-right corner of the notebook.  
![Resource view](image/resources.png)

## Working with Datasets

- To use a dataset in your notebook, you first need to upload it to Kaggle.
- Go to **Create > New Dataset** and upload your dataset. For large files, consider zipping them before uploading.
- In your notebook, select **Add Input** to access your uploaded dataset.

   ![Add input](image/input.png)

- Check **Your Work** and then **Datasets** to view your uploaded datasets.

   ![Select dataset](image/ticks.png)

- Click the plus sign to add your dataset (ensure it has been successfully uploaded).

- Once added, your dataset will be available in the `/kaggle/input` directory by default.

## Saving and Accessing Outputs

- By default, any files or folders you download or create in the notebook are stored in `/kaggle/working` under **Output**.  
  ![Output tab](image/output_tab.png)  

- To save your output, click **Save Version**.  
  ![Save version](image/save.png)  

- Enter a version name, set the version type to **Quick Save**, and configure the save output setting to **Always save output when creating Quick Save**.  
  <div style="background-color:white; padding:10px; display:flex; justify-content:center;height:300px">
      <img src="image/quicksave.png" alt="Quick Save" />
  </div>

- Wait for the save process to complete.  
  ![Saving queue](image/queue.png)

- Once completed, you can go to the **Output** tab, locate your files, and download them.  
  ![Download output files](image/outputfile.png)

- *Note*: You can directly download smaller output files from the output tab in your notebook.

## Fine-tuning on Kaggle

- Locate a fine-tuning script for your model (either create one or find it on sources like Hugging Face).
- Ensure the model and script fit within Kaggle’s available resources.
- For Hugging Face models, you can check resource requirements in the model hub. For scripts from other sources, run them initially to estimate resource needs.

### When GPU Resources Are Insufficient

- Use resource-saving techniques like gradient accumulation, smaller batch sizes, and efficient memory management.
- Available options include:
  - flash_attn 1.x
  - Mixed Precision (FP16)
  - qlora
  - int8 quantization (`bitsandbytes`)
- Clear unused variables and use `torch.cuda.empty_cache()` to manage memory.
- If resources are still insufficient, try a smaller or alternate model.

### Fine-tuning Strategy on Kaggle

- For large models, consider fine-tuning one epoch at a time. This approach helps conserve resources, allows you to monitor the training process, and reduces the risk of overfitting.
- Here’s the process step-by-step:
  1. Fine-tune the model for one epoch.
  2. Save the model weights and optimizer state.
  3. (Optional) Run inference on the validation set.
  4. Restart the notebook and reload the saved weights and optimizer state to continue training.
  5. Repeat until the desired number of epochs is reached or overfitting occurs.

- **Avoid Downloading and Re-uploading Weights**:
  - Save weights and optimizer state in the output folder using **Quick Save**.
  - In the notebook’s **Output** tab, click **New Dataset** to create a reusable dataset with the saved weights.
    <div style="background-color:grey; padding:10px; display:flex; justify-content:center;height:300px">
        <img src="image/avoid_download.png" alt="Avoid Downloading"/>
    </div>
  - Add this dataset back into your fine-tuning notebook as an input to save time and avoid re-uploading.
  - If needed, you can access previous versions by checking the version history and selecting the desired output version.
    <div style="display: flex; justify-content: space-between;background-color:grey;height:350px;">
        <img src="image/view_versions.png" alt="View Version" style="width: 50%; margin-right: 10px;">
        <img src="image/version_history.png" alt="Version History" style="width: 50%;">
    </div>

- **Alternative Method for Managing Weights**:
  - Use **Save and Run All (Commit)** to execute and save outputs.
    ![Run with GPU](image/run_with_gpu.png)
  - In the notebook, click **Add Input**, select **Your Work > Notebooks**, and choose the previously committed notebook.
  - This allows you to access output files directly without creating a new dataset each time, although this method defaults to the latest version of the output files.

## Helpful Tips

- **Preserving Progress**: If you need to stop a running notebook but want to save progress, change **Persistence** to **Variables and Files** before stopping the notebook. This will save your variables and files for the next session.  
  ![Persistence](image/persistence.png)

- **Monitoring Progress Efficiently**: When you **Save and Run All (Commit)**, a progress bar will appear at the bottom of the notebook window, showing the output of the current cell. You can resize the window to keep the progress bar visible while working on other tasks, allowing you to monitor the fine-tuning progress of multiple scripts simultaneously.

- **Sharing Datasets and Notebooks**: You can share datasets and notebooks privately with others without publishing them. This saves time when collaborating, especially if multiple datasets need to be uploaded.
