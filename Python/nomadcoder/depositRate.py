deposit=depositOrigin=int(input("5년간 예치할 금액:"))
rate=0.05

deposit+=deposit*rate
deposit+=deposit*rate
deposit+=deposit*rate
deposit+=deposit*rate
deposit+=deposit*rate

interest=deposit-depositOrigin
print("5년 후 총 수령액",int(deposit),"원")
print("원금:",depositOrigin,"원")
print("이자:",int(interest+int(interest%2>0)),"원(1원미만 절상)")
#print(int(interest%2)) 올림 표현하는 방법, 나머지값이 있으면(나머지>0)1로 표현하여 +해주기
#print(int(3%2>0))
