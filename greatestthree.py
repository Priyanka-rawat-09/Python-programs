a=int(input("enter the no."))
b=int(input("enter the second no."))
c=int(input("enter the third no."))
if a>=b and a>=c:
	print(a,"is greatest no.")
elif b>=a and b>=c:
	print(b,"is a greatest no.")
else:
	print(c,"is a greatest no.")