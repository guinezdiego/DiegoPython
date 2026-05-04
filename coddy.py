# prices = input()
# phone = input()

# prices = list(map(int, prices.split()))

# producto = prices[0] * prices[1]

# if (
#     len(phone) == 12 and
#     phone[3] == "-" and
#     phone[7] == "-" and
#     phone[:3].isdigit() and
#     phone[4:7].isdigit() and
#     phone[8:].isdigit() 
# ):
#     estado = "Valid"
# else:
#     estado = "Invalid"
    
# print(producto)
# print(estado)


numbers = [1, 2, 3, 4, 5]
base = numbers + numbers[::-1]
base = [numbers[0]] + base + [numbers[-1]]
print(base * 2)