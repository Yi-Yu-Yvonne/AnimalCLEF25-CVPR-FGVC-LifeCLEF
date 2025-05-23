# AnimalCLEF25-CVPR-FGVC-LifeCLEF

This repository contains our code, models, and example data for the AnimalCLEF25 challenge.  

---

## 1. Installation

All installation steps (environment setup, required libraries, etc.) are provided in the first code cell of each notebook when opened in Google Colab:

- **ResNet_Dino.ipynb** (ResNet & DINO workflows)  
- **MegaDescriptor.ipynb** (our contrastive-learning–based descriptor)

Just run the first cell, and you’ll have everything you need.

---

## 2. Advanced Algorithms & Models

- **ResNet-50** fine-tuned checkpoints in `resnet_model_history/`  
- **DINOv2** pre-trained embeddings in `dino_model_history/`  
- **MegaDescriptor** model in `MegaDescriptor.ipynb`

---

## 3. Test / Validation Examples

A few sample images for quick testing. For example:

<p float="left">
  <img src="sample_image/0a2b29c15d9c4d2b_80.jpg" alt="Salamander sample" height="150" />
  <img src="sample_image/0a8eb6e2dc2e6dc8fd1013f651a880b69cb9e7e6a4c4dfdbe4f23919f509ff80.jpg" alt="Lynx sample" height="150" />
  <img src="sample_image/anuJvqUqBB_12.JPG" alt="Turtle sample" height="150" />
</p>


---

## 4. Running Inference

In `ResNet_Dino.ipynb` it includes clear, in-line comments showing how to:

6. **Ensemble Model Prediction**
7. **Single Model Prediction**

In `MegaDescriptor.ipynb` it includes clear, in-line comments showing how to:

6. **Main Execution** 
7. **Create Submission Files**

---

## File description
- `Data_Process_Analysis.ipynb` — Data preprocessing  

- `ResNet_Dino.ipynb` — Code for ResNet and DINO models  
    - `resnet_model_history/` — Fine-tuned ResNet checkpoints  
    - `dino_model_history/` — DINO model files  

- `MegaModel/` — Code for MegaDescriptor  
  1. Upload your dataset to the repo root  
  2. Update the `DATA_PATH` variable at the top of the notebook  
  3. Run all cells  
  - `mega_embedding_id/` — Embeddings and identities for the dataset

- `result/` — Submission CSV files to the website  
  - `Score.xlsx` — Scores of the experiment  

---

### Leaderboard Scores

![Testing image](result/Mega_Test_Score.jpg)
![Testing image](result/Finetune_Resnet_Test_Score.png)
![Testing image](result/Finetune_Resnet_Test_Score.png)

---

### Presentation Slides

- [View PDF](https://github.com/Yi-Yu-Yvonne/AnimalCLEF25-CVPR-FGVC-LifeCLEF/blob/main/Presentation.pdf)
