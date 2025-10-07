try:
  a2=input("Please enter file name : ")
  file=open(a2,'r')
  r1=file.readline()
  r2=file.readline()
  print("reading file content :")
  print("line 1 :",r1)
  print("line 2 :" ,r2)
  file.close()
except FileNotFoundError:
    print("Error: The file ",a2 , "was not found")
finally:
    print("program finished!")
