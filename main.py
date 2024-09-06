import re

print("NED-BATCH-7")


# Regex

text = """
42203-7320776-1
42201-6783496-4
45671-2789776-3

"""

data = re.findall("[0-9]{5}-[0-9]{7}-[0-9]{1}",text, re.IGNORECASE) 
print(data)

data1 = re.findall("\d{5}-\d{7}-\d{1}",text, re.IGNORECASE) 
print(data1)