import matplotlib.pyplot as plt 
fruits = ["apple", "banana","orange","grapes","mango"]
quantity = [10,20,15,25,30]

plt.title("Fruits vs Quantities", fontsize = 15, fontstyle = 'oblique')

c = ['y','b','m','g']
ec = ['gold','mediumblue','magenta','darkgreen']
plt.bar(fruits,quantity, width = 0.5, color = c, edgecolor = ec, linewidth = 5, linestyle = '--', alpha = 0.2)
plt.xlabel("fruits")
plt.ylabel("quantity")

'''plt.barh(fruits,quantity, color = "Aquamarine", height = 0.5)
plt.ylabel("fruits")
plt.xlabel("quantity")'''
plt.show()