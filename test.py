import nbformat

# 1) Read the notebook
nb = nbformat.read("MegaDescriptor_copy.ipynb", as_version=4)

# 2) Remove any metadata.widgets entries
for cell in nb.cells:
    if cell.get("metadata", {}).pop("widgets", None) is not None:
        print(f"  ▶ Removed widgets metadata from cell {nb.cells.index(cell)}")

# 3) Write back over the original
nbformat.write(nb, "MegaDescriptor_copy.ipynb")
print("✅ Notebook cleaned.")
