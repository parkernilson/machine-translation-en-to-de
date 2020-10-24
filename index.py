# from transformers import pipeline
import transformers
from transformers import T5Tokenizer, TFT5ForConditionalGeneration
import sys

# set logging level to error to prevent unnecessary logging
transformers.logging.set_verbosity(transformers.logging.ERROR)

# try to load the model from /saved_models volume
try:
    tokenizer = T5Tokenizer.from_pretrained("/saved_models/t5-base")
    model = TFT5ForConditionalGeneration.from_pretrained("/saved_models/t5-base")
except:
    # if the model cannot be loaded from filesystem, download it from the huggingface api instead.
    print("INFO: The saved_models could not be loaded from /saved_models volume. Downloading from huggingface api instead")

    # load from hugging face
    tokenizer = T5Tokenizer.from_pretrained("t5-base")
    model = TFT5ForConditionalGeneration.from_pretrained("t5-base")

    # save to volume
    tokenizer.save_pretrained("/saved-models/t5-base")
    model.save_pretrained("/saved-models/t5-base")


DEFAULT_PHRASE = "The Wheel of Time is an incredible Book."

if not len(sys.argv) > 1:
    print(f"\nNo phrase was given for translation, so we will use the default phrase: {DEFAULT_PHRASE}\n")
    string_to_translate = DEFAULT_PHRASE
else:
    string_to_translate = sys.argv[1]

inputs = tokenizer(f"translate English to German: {string_to_translate}", return_tensors="tf").input_ids
result = model.generate(inputs)

print("\nTranslation:\n")
print(tokenizer.decode(result[0]))
print()
