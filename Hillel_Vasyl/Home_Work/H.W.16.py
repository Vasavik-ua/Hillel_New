input_val = b'r\xc3\xa9sum\xc3\xa9'
decod = input_val.decode()
print(decod)
new_input = decod.encode('Latin1')
print(new_input)
new_input_dec = new_input.decode('Latin1')
print(new_input_dec)
