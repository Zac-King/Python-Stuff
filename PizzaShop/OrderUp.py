def mulThat(A, B):
	m = A * B
	return m

pizzaSlice = input('How much is a slice of pizza?  ')

print('Price of a full pizza would be $', mulThat(eval(pizzaSlice), 8))