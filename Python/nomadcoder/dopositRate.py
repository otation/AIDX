deposit=int(input("5년간 예치할 금액:"))
rate=0.05

deposit+=deposit*rate
deposit+=deposit*rate
deposit+=deposit*rate
deposit+=deposit*rate
deposit+=deposit*rate

print("5년 후 총 수령액",int(deposit),"원")

