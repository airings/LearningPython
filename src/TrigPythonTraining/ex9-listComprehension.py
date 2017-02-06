def toDict(tabString):
    list = tabString.strip().split('\t')
    dict = {}
    keys = 'Brand,Color,Size'
    for index, key in enumerate(keys.split(',')):
        dict[key] = list[index]
    return dict

def line_to_dict(line):
    brand, color, size = line.strip().split('\t')
    return {
        'brand' : brand,
        'color' : color,
        'size'  : size
    }

print [toDict(line) for line in open('exercise/shoe-data.txt')]