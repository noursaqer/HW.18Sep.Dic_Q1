keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res = {}
for key in keys:
    for value in values:
        res[key] = value
        values.remove(value)
        break
print(res)