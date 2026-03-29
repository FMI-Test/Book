import re
import yaml

input_file = "Nano-Banana-Prompts-CP.md"
output_file = "inputs/nano-prompts-full.yml"

try:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    data = {}
    current_group = "General"

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith("## ") or line.startswith("### "):
            current_group = re.sub(r'^#+\s*', '', line).strip()
            if current_group not in data:
                data[current_group] = []
        elif "::" in line:
            parts = line.split("::", 1)
            if len(parts) == 2:
                title = parts[0].strip()
                title = re.sub(r'^[-*]\s*', '', title).strip() # remove bullet points
                title = title.replace("**", "")
                prompt = parts[1].strip()
                
                if current_group not in data:
                    data[current_group] = []
                    
                data[current_group].append({
                    "Title": title,
                    "Prompt": prompt
                })

    with open(output_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"Generated {output_file} successfully.")
except Exception as e:
    print(f"Error: {e}")
