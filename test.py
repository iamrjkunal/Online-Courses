import os
import sys
# print(dir(os))
direct = os.getcwd()
print(direct)
print(os.path.dirname(direct))
print(os.path.basename(direct))
print(os.path.split(direct))
print(os.path.splitext(direct))