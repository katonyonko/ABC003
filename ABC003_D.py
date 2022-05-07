import io
import sys

_INPUT = """\
6
3 2
2 2
2 2
4 5
3 1
3 0
23 18
15 13
100 95
30 30
24 22
145 132
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=900
  mod=10**9+7
  F=[1]
  for i in range(N):
      F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(N):
      I.append(I[-1]*(N-i)%mod)
  I=I[::-1]
  def c(i,j):
    if i<j: return 0
    else: return F[i]*I[j]*I[i-j]%mod
  R,C=map(int,input().split())
  X,Y=map(int,input().split())
  D,L=map(int,input().split())
  tmp=c(X*Y,D+L)-2*c((X-1)*Y,D+L)-2*c(X*(Y-1),D+L)+4*c((X-1)*(Y-1),D+L)+c((X-2)*Y,D+L)+c(X*(Y-2),D+L)-2*c((X-2)*(Y-1),D+L)-2*c((X-1)*(Y-2),D+L)
  if X>2 and Y>2: tmp+=c((X-2)*(Y-2),D+L)
  tmp%=mod
  print(c(D+L,D)*(R-X+1)*(C-Y+1)*tmp%mod)