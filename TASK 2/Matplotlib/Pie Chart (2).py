from matplotlib import pyplot as plt

plt.style.use("seaborn")

#slices=[120, 80, 30,20]
#labels=['Sixty','Forty','E1','E2']
#colors=['blue','red','yellow','green']

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0] #explode argument is to emphasize a particular slice 
                            #0.1 indicates the piece is eploded from radius by 0.1

plt.pie(slices, labels=labels, explode=explode, shadow=True,
startangle=90, autopct='%1.1f%%',wedgeprops={'edgecolor': 'black'})

#shadow=True is for shadow along the edges
#startangle is to give an angle to the start piece
#autopct is to show percentage of every piece

#plt.pie(slices)
#plt.pie(slices, labels=labels,colors=colors, wedgeprops={'edgecolor':'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
