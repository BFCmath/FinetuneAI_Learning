# Getting Started with Kaggle
## Setting Up Kaggle

1. **Create an Account**: Register for an account on Kaggle.
2. **Identity Verification**:
   - Go to **Profile > Settings**.
   - Complete **Phone Verification** by adding and verifying your phone number.
   - Complete **Identity Verification** by scanning your face.

## Creating a New Notebook

- Create your first notebook by selecting **Create > New Notebook**.
- Kaggle notebooks support Jupyter-style shortcuts and magic commands.
- Notebooks save automatically, and you can upload your own `.ipynb` files.

![Upload notebook](image/upload_notebook.png)

## Enabling GPU in Kaggle
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

## Available Resources

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

## Run All + Recurrent Workflow

If you want to use the output of your notebook as the input for the same notebook, follow these steps: 

1. **Save and Run All**: Ensure your notebook runs successfully by using the **Save and Run All (Commit)** option. This will execute the notebook and save the outputs in one step. Remember to turn on the GPU before running the notebook.

![](image/getting_started_2025-01-27-00-25-11.png)

2. **Add Input**: After the notebook has run successfully, click **Add Input** and select **Your Work > Notebooks**. Choose the notebook you just ran.
Here is an example of how the notebook will look after running and adding the input:
![](image/getting_started_2025-01-27-00-28-01.png)

3. **Access Output Files**: You can access the output files directly without creating a new dataset each time. However, this method defaults to the latest version of the output files.

4. **Save as Dataset** (Alternative): 
You can also save the output files as a dataset by clicking **New Dataset** in the **Output** tab. This will create a reusable dataset with the saved outputs.
![](image/getting_started_2025-01-27-00-29-40.png)