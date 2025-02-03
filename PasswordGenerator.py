import random 
letters =['a','b','c', 'd', 'e','f','g','h','1','j', 'k', 'l','m','n','o','p', 'q','r', 's','t','u', 'v','w', 'x', 'y', 'z', 'A','B', 'C', 'D','E','F','G','H','I','J','K', 
          'L','M', 'N', '0', 'P', 'Q', 'R', 'S','T','U','V','W','X','Y','Z']
numbers =['0', '1', '2','3','4','5', '6','7','8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*','+']
print("Welcome to Password Generaor...!")
n_let=int(input("How many letters you want in your password?\n"))
n_numb=int(input("How many numbers you want in your password?\n"))
n_symb=int(input("How many symbols you want in your password?\n"))
password=''
for _ in range(1,n_let+1):
  ch=random.choice(letters)
  password=password+ch
for _ in range(1,n_numb+1):
  ch=random.choice(numbers)
  password=password+ch
for _ in range(1,n_symb+1):
  ch=random.choice(symbols)
  password=password+ch
print(password)
