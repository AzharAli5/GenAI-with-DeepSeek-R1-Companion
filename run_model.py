from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Path to your local model
model_path = r"DeepSeek-R1-Distill-Qwen-1.5B"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16, device_map="auto")

# Input prompt
input_text = "What is artificial intelligence?"
inputs = tokenizer(input_text, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

# Generate response
output = model.generate(**inputs, max_length=100)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Text:", generated_text)
