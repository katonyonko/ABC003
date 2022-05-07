import io
import sys

_INPUT = """\
6
ch@ku@ai
choku@@i
aoki
@ok@
aoki
@ok@
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  T=input()
  ans='You can win'
  tmp=set(['a','t','c','o','d','e','r','@'])
  for i in range(len(S)):
    if S[i]=='@' and T[i] not in tmp or S[i] not in tmp and T[i]=='@' or S[i]!='@' and T[i]!='@' and S[i]!=T[i]: ans='You will lose'
  print(ans)