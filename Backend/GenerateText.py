import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1")

model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-R1",
    device_map="auto",
    torch_dtype=torch.float16  
   )

prompt = "<|im_start|>user\ntell me about you<|im_end|>\n<|im_start|>assistant\n"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
output = model.generate(
    **inputs,
    max_new_tokens=200,  # Adjust based on desired response length
    temperature=0.7,     # Controls randomness; lower values yield more deterministic outputs
    do_sample=True       # Enables sampling for more varied responses
)
response = tokenizer.decode(output[0][inputs['input_ids'].shape[-1]:], skip_special_tokens=True)


print(response)
