import random
print("計算ドリルSTART!")
score=0
for i in range(5):
  print(f"第{i+1}問")
  num1=random.randrange(999)+1
  print(f"{num1}を2進法に変換せよ")
  ans=input("答えは？")
  if num1==int(ans,2):
    print("お見事！正解")
    score+=1
  else:
     print("残念！不正解")
  print("正解は",format(num1, 'b'))
  print()
print(f"終了。正解数は{score}問です。")