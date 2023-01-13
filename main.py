# imports
from pandas import DataFrame
import config

v1 = []  # 1 var of question
v2 = []  # 2 var of question
v3 = []  # 3 var of question
v4 = []  # 4 var of question
v5 = []  # 5 var of question
t = []   # question type
c = []   # answer
q = []   # question
i = 0

file = open(config.path_to_sessia, "r", encoding="utf8")  # reading file
text = file.read()

variants = text.split("<question>")              # split all questions

for variant in variants:                         # split by variants
    vars = variant.split("<variant>")
    for var in vars:                             # sorting
        i = i + 1
        if i == 1:
            q.append(var)
            t.append("Multiple Choice")
            c.append("1")
        if i == 2:
            v1.append(var)
        if i == 3:
            v2.append(var)
        if i == 4:
            v3.append(var)
        if i == 5:
            v4.append(var)
        if i == 6:
            v5.append(var)
    i = 0

# deleteing first variants (idk why, but they empty)
t.pop(0)
q.pop(0)
c.pop(0)

# importing to excel sheets
a = {'Question Text': q, "Question Type": t, 'Option 1': v1, 'Option 2': v2, 'Option 3': v3, 'Option 4': v4,
     'Option 5': v5, 'Correct Answer': c}
df = DataFrame.from_dict(a, orient='index')
df = df.transpose()

df.to_excel(config.path_to_quizizz, sheet_name='sheet', index=False)