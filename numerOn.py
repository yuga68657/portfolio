import random
def rand_ints_nodup(a, b, k):
  ns = []
  while len(ns) < k:
    n = random.randint(a, b)
    if not n in ns:
      ns.append(n)
  return ns
num=(rand_ints_nodup(0, 9, 3))
ans=input("3桁の数字を入力せよ")
ans2=list(ans)
ans3=[int(n) for n in ans2]
while ans3!=num:
  eat=0
  bite=0
  for n in range(3):
    if num[n]==ans3[n]:
      eat+=1
  if num[0]==ans3[1] or num[0]==ans3[2]:
    bite+=1
  if num[1]==ans3[0] or num[1]==ans3[2]:
    bite+=1
  if num[2]==ans3[1] or num[2]==ans3[0]:
    bite+=1
  print(f"{eat}eat、{bite}biteです！！")
  print()
  ans=input("3桁の数字を入力せよ")
  ans2=list(ans)
  ans3=[int(n) for n in ans2]
else:
  print(f"3eat!! 正解は{num}です。")