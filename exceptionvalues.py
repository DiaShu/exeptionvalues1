try:
    n = int(input("please enter a integer"))

except:
    print("Please enter a valid number")

else:
    print(n)
finally:
    print("this will always be executed")

