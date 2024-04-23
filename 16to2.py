import random
print("計算ドリルSTART!")
score=0
for i in range(5):
  print(f"第{i+1}問")
  num1=format(random.randrange(254)+1,"x")
  print(f"{num1}を2進法に変換せよ")
  answer=input()  
  ans=int(answer,2)
  num2=str(num1)
  num3=int(num2,16)
  if num3==ans:
    print("お見事！正解")
    score+=1
  else:
     print("残念！不正解")
  print("正解は",format(num3,"b"))
  print()
print(f"終了。正解数は{score}問です。")