clothing = []

for survey in range(1, 31):
    info = {
    'shirt': 'lavender',
    'pants': 'blue',
    'hat': 'blue'
    }
    clothing.append(info)

print len(clothing)
for x in (clothing[:4]):
    print(x['hat'])
    x['hat'] = 'orange'


print

for x in (clothing):
    print(x['hat']
