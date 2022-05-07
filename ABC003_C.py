import io
import sys

_INPUT = """\
6
2 2
1000 1500
2 1
1000 1500
10 5
2604 2281 3204 2264 2200 2650 2229 2461 2439 2211
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  R=list(map(int,input().split()))
  R=sorted(R)[-K:]
  C=0
  for i in range(K):
    C=(C+R[i])/2
  print(C)