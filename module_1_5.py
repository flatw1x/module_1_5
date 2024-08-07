immutable_var = 1, 'string', 1.5, [1, 2], True
print(immutable_var)
immutable_var[3][0]=2
print(immutable_var)
mutable_list = [1, 'string', 1.5, [1,2], True]
mutable_list[1]= 'str'
print(mutable_list)