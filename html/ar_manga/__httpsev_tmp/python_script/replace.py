import sys
import os
import re

with open(sys.argv[1]) as f:
    data_lines = f.read()

targetstr = "http://" + sys.argv[3] + ":" + sys.argv[4]
if sys.argv[4] == "4443":
    targetstr = "https://" + sys.argv[3] + ":" + sys.argv[4]

data_lines = re.sub("xxx", targetstr, data_lines)

with open(sys.argv[2], mode="w") as f:
    f.write(data_lines)
