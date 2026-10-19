import json

# Read the notebook json file
with open("takemeter.ipynb", "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Extract all code cells
code_lines = []
for cell in notebook["cells"]:
    if cell["cell_type"] == "code":
        # Some cells might be lists of strings or a single string
        source = cell["source"]
        if isinstance(source, list):
            code_lines.extend(source)
        else:
            code_lines.append(source)
        code_lines.append("\n\n")

# Write out to takemeter.py
with open("takemeter.py", "w", encoding="utf-8") as f:
    f.writelines(code_lines)

print("Successfully extracted takemeter.ipynb into takemeter.py!")
