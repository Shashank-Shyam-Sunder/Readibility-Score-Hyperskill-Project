import os
file_name = "test_file.txt"
# print("Current working directory:", os.getcwd())
# print("Looking for:", os.path.abspath(file_name))
# print("Files in this directory:", os.listdir())
os.chdir(r"C:\Shashank_work\Python_Works\Readability_score\Readability Score (Python)\task\readability")
with open(file_name, "r") as file:
    text = file.read()

# Remove spaces, tabs, and newlines
clean_text = text.replace(" ", "").replace("\n", "").replace("\t", "")

# Count characters
char_count = len(clean_text)
print("Character count (no spaces, tabs, newlines):", char_count)

# %%
# for _ in text:
#     print(_)