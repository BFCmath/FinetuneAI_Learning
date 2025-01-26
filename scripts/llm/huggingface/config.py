from transformers import TrainingArguments, Trainer
NAME = ...
PRETRAINED_MODEL = ...

args = TrainingArguments( NAME,
                     PRETRAINED_MODEL,
                     evaluation_strategy = 'steps',
                     eval_steps = 500,
                     dataloader_num_workers=8,
                     warmup_ratio=0,
                     lr_scheduler_type = 'linear',
                     learning_rate = 2e-5,
                     log_level = 'warning',
                     fp16 = True,
                     per_device_train_batch_size = 2,
                     per_device_eval_batch_size = 2,
                     gradient_accumulation_steps = 2,
                     gradient_checkpointing = True,
                     num_train_epochs = 5,
                     save_strategy = 'no',
                     save_total_limit = 1)

trainer = Trainer(model,
              args,
              train_dataset=train_dataset,
              eval_dataset=valid_dataset,
              compute_metrics=KaggleMetric(valid_df, valid_dataset),
              callbacks=[SaveBestModelCallback],
              data_collator=data_collator,
              tokenizer=tokenizer)