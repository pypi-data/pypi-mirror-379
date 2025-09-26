from takucyrpt import Tencrypt, Tdecrypt

a=Tencrypt("hello world")
print(a)
b=Tdecrypt(a)
print(b)