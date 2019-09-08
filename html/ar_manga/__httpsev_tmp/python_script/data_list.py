import os
import re

found = []
for root, dirs, files in os.walk("."):
    for filename in files:
        found.append(os.path.join(root, filename))

filter_target = ('.jpeg', '.jpg')
filter_target += ('.gif', '.bmp', '.png')
filter_target += ('.gltf', '.glb')
files = list(filter(lambda x: x.endswith(filter_target), found))
replacereg = ''
for s in filter_target:
    replacereg = replacereg + '|' + s + '$'
replacereg = replacereg[1:]

with open("js/data.js", mode="w") as f:
    f.write('let data = [\n')
    for s in files:
        s = s.replace('\\', '/')

        patt = re.sub(replacereg, '.patt', s)
        if not os.path.exists(patt):
            continue

        print(s)
        f.write('{')
        f.write('img: "' + s + '",')
        f.write('patt:"' + patt + '",')
        f.write('}, \n')
    f.write('];\n')
