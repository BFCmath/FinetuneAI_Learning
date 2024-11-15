# Using HuggingFace
Hugging Face is a leading AI platform and open-source community that simplifies working with state-of-the-art machine learning models. Known for its user-friendly libraries, it empowers developers and researchers to access pre-trained models, fine-tune them, and integrate them into applications with ease.

## Transformers Library
+ [Transformers](https://huggingface.co/transformers/)
+ Installation:
```bash
pip install transformers
```
+ Core components:
    + Models
    + Tokenizers
    + Trainer API 
    + Datasets Integration
## Hugging Face Models
+ [Hugging Face Model Hub](https://huggingface.co/models)
+ Hugging Face have a vast collection of pre-trained models available for various NLP tasks.
+ You can filter task and access to up-to-date models.
+ You can download weight and configuration files for the model you need.
+ They can be easily loaded and utilized using the `transformers` library.
Example usage:
```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "bert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

inputs = tokenizer("I love Hugging Face!", return_tensors="pt")
outputs = model(**inputs)
```
## Tokenizers 
+ Essential for preparing input data for transformer models.
+ Features:
    + Subword tokenization.
    + Batch encoding with padding and truncation.
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
tokens = tokenizer("Transformers are powerful!", return_tensors="pt")
print(tokens)
```
## Datasets 
The library seamlessly integrates with Hugging Face's Datasets library for loading and processing data.
## Trainer API
Simplifies fine-tuning and evaluation of models.
```python
from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=8,
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)
trainer.train()
```
