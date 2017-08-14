import matplotlib.pyplot as plt


population_ages = [22, 55, 62, 75, 26, 74, 65, 90, 8, 30,
				   2, 25, 56, 27, 52, 67, 46, 59, 80, 32,
				   100, 111, 120, 130, 121, 123, 124, 125] 


#ids = [x for x in  range(len(population_ages))]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', 
		 rwidth=0.8, label='Populations')


plt.xlabel('x')
plt.ylabel('y')

plt.title('Intersting Graph\nCheck it out')
plt.legend()

plt.show() 