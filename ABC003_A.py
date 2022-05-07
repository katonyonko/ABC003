import io
import sys

_INPUT = """\
6
6
91
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  print(N*5000+5000)