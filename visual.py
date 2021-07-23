from matplotlib import pyplot
import pandas

df = pandas.read_csv('/Users/19luc/OneDrive/Desktop/Test_02/Book1.csv')

pyplot.scatter(df['Age'], df['Salary'])
pyplot.show()
