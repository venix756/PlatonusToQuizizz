from pandas import DataFrame
import config

v = [[], [], [], [], []]
t = []
c = []
q = []

file = open(config.path_to_sessia, "r", encoding="utf8")
text = file.read()

variants = text.split("<question>")

for variant in variants:
    vars = variant.split("<variant>")
    for i, var in enumerate(vars):
        if i == 0:
            q.append(var)
            t.append("Multiple Choice")
            c.append("1")
        else:
            v[i-1].append(var)

t.pop(0)
q.pop(0)
c.pop(0)

a = {'Question Text': q, "Question Type": t, 'Option 1': v[0], 'Option 2': v[1], 'Option 3': v[2], 'Option 4': v[3],
     'Option 5': v[4], 'Correct Answer': c}
df = DataFrame.from_dict(a, orient='index')
df = df.transpose()

df.to_excel(config.path_to_quizizz, sheet_name='sheet', index=False)
