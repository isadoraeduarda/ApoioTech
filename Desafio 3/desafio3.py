N = int (input())

for i in range(N):
    num1, num2, num3 = map(float, input().split())
    media_ponderada = (num1*2 + num2*3 + num3*5)/10
    print(media_ponderada)

