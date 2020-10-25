from transformers import T5Tokenizer, TFT5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-base")
model = TFT5ForConditionalGeneration.from_pretrained("t5-base")

tokenizer.save_pretrained("/saved-models/t5-base")
model.save_pretrained("/saved-models/t5-base")
