b=input("Enter text to write in the file : ")
with open('output.txt','w')  as file:
    file.write(b + '\n')
    print("Data succesfully written to output.txt.")

c=input("Enter additional text to append :")
with open('output.txt','a') as file:
    file.write(c + '\n')
print("Data successfully appended")

with open('output.txt','r') as file:
    D=file.read()
print("Final content of output.txt : ")
print(D)



