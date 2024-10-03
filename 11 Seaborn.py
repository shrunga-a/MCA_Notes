# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# draw lineplot
sns.lineplot(x="sepal_length", y="sepal_width", data=data).set(title="Flower petals analysis")

# setting the x limit of the plot
plt.xlim(5)

# changing the figure size
plt.figure(figsize = (2, 4))

# Setting the scale of the plot
sns.set_context("paper")


# changing the theme to dark
sns.set_style("dark")

# Removing the spines
sns.despine()
plt.show()



#Scatter Plot:
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
sns.scatterplot(x='sepal_length', y='sepal_width', data=data)
plt.show()


#Line Plot
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
sns.lineplot(x='sepal_length', y='species', data=data)
plt.show()


#Bar Plot
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")
sns.barplot(x='species', y='sepal_length', data=data)
plt.show()

#Count Plot
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
sns.countplot(x='species', data=data)
plt.show()


#Box Plot
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")
sns.boxplot(x='species', y='sepal_width', data=data)
plt.show()


#Histogram
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.histplot(x='species', y='sepal_width', data=data)
plt.show()


#Pairplot
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt
# loading dataset
data = sns.load_dataset("iris")
sns.pairplot(data=data, hue='species')
plt.show()
