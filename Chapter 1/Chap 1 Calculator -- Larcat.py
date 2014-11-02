faren_temp = float(input("What temp in F do you want to convert? "))

celcius_temp = (faren_temp - 32.0) * (5.0/9.0)

print("When the temp in Farenheit is {:.2f}: ".format(faren_temp))
print("The temp in Celcius is: {:.2f}".format(celcius_temp))