from django.test import TestCase
from UtilTool.Util.ShortUuid import short_uuid
import os

# Create your tests here.
i= 1
print("{0:03d}P".format(i) + short_uuid())
#文件夹
print(os.path.isdir('F:\\通职者\\大感谢祭！福利番外赏！\\P-1.jpg'))

fileList = os.listdir('F:\\通职者')
if os.path.isdir('F:\\通职者\\大感谢祭！福利番外赏！'):
    for file in fileList:
        print(file)