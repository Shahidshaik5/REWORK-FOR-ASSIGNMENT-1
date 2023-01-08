# Importing the Python Libraries
import pandas as pd # Importing pandas library as pd
import matplotlib.pyplot as plt # Importing matplotlib.pyplot as plt

# Reading the CSV file and Printing it
china_data = pd.read_csv("china population.csv") # Reading the CSV file into pandas dataframe
print(china_data) # Printing the Data

# Plotting the Lineplot for the Fertility rate and Yearly % change in population 
def lineplot(xlabel, Ylabel, Title, savefig): # Creating a defination function for lineplot
    plt.figure(figsize=(8,6)) # To crete the figure
    plt.plot(china_data["Year"], china_data["Fertility Rate"], 
        label="Fertility Rate", linestyle='--', lw=3, color='green') # Plotting the Fertility Rate lineplot
    plt.plot(china_data["Year"], china_data["Yearly % Change"], 
        label="Yearly change", linestyle=':', lw=3, color='red') # Plotting the Yearly % change lineplot
    plt.xlabel(xlabel, fontsize=15) # To label the X-Axis
    plt.ylabel(Ylabel, fontsize=15) # To Label the Y-Axis
    plt.legend(loc='upper right') # To show the Legend on the plot
    plt.title(Title, fontweight ="bold", fontsize=20) # To show the title on the plot
    plt.grid() # To add the grid on the plot
    plt.savefig(savefig, dpi=600) # To Save the fig with desired resolution
    plt.show() # To show the plot

# Plotting the Piechart for the Countrys share of world pop
def piechart(Title, savefig): # Creating a defination function for piechart
    plt.figure(figsize=(8,6)) # To crete the figure
    plt.pie(china_data["Country's Share of World Pop"], labels = china_data["Year"], 
        autopct='%1.0f%%', startangle = 90, rotatelabels = True, counterclock = False, 
        pctdistance = 0.75, labeldistance  = 1, radius = 0.9) # To plot pie chart of Country's Share of World Pop
    plt.title(Title, size = 20, fontweight ="bold") # To show the title on the plot
    plt.savefig(savefig, dpi=600) # To Save the fig with desired resolution
    plt.show() # To show the plot

# Plotting the Barplot for the Total population and Urban population
def barplot(Xlabel, Ylabel, Title, savefig): # Creating a defination function for barplot
    china_data.plot.bar(x ='Year', y = ['Population', 'Urban Population'], 
        rot = '35', width = 0.7) # Ploting the Bar Chart
    plt.xlabel(Xlabel, fontsize=12) # To label the X-Axis
    plt.ylabel(Ylabel, fontsize=12) # To Label the Y-Axis
    plt.title(Title, loc="center", fontsize=15, fontweight ="bold") # To show the title on the plot
    plt.savefig(savefig, dpi=600) # To Save the fig with desired resolution
    plt.legend(loc='best') # To show the Legend on the plot
    plt.show() # To show the plot

lineplot("Year", "Population", "fertility rate and yearly change in population", 
    "fertility rate and Yearly change.jpeg") # Calling the Lineplot function
piechart("China's Share of World Population", "China share of world population.jpeg") # Calling the piechart function
barplot("Year", "Population", "Total population & Urban population", "total vs urban populaton.jpeg") # Callin the barplot function












































'''def lineplot():
    plt.figure() # To create figure with required resolution
    plt.plot(srilanka['Year'], srilanka['GDP growth percentage'], label = 'Population') # To plot line graph of Year vs China's total population
    plt.plot(srilanka['Year'], srilanka['Annual Growth Rate in GDP Per Capita'], label = 'Urban Population') # To plot line graph of Year vs Urban Population      
    plt.xlabel('Year', fontsize = 12) # To label the x-axis
    plt.ylabel('Population', fontsize = 12) # To label the y-axis
    plt.title('China Population', size = 16, color = 'black') # To give title of graph
    plt.legend() # To show the elements of the graph
    plt.grid()   # To show grid on graph
    plt.show()   # To show the graph 
lineplot()'''
'''df = pd.read_csv("Sri Lanka Economy.csv") # To load csv file
print(df)'''

'''plt.figure(dpi = 300) # To create figure with required resolution
plt.plot(df['Year'], df['GDP growth percentage'], label = 'Total Population') # To plot line graph of Year vs China's total population
plt.plot(df['Year'], df['Inflation Rate'], label = 'Urban Population') # To plot line graph of Year vs Urban Population
plt.xlim(2000, 2020)  # To set the limit on x-axis        
plt.xlabel('Year', fontsize = 12) # To label the x-axis
plt.ylabel('Population', fontsize = 12) # To label the y-axis
plt.title('China Population', size = 16, color = 'black') # To give title of graph
plt.legend() # To show the elements of the graph
plt.grid()   # To show grid on graph
#plt.savefig('line_graph-1.jpeg', dpi = 300) # To save the graph
plt.show()   # To show the graph '''

'''def linegraph():
    plt.figure()
    plt.plot(Srilanka_economy['Year'],Srilanka_economy['GDP growth percentage'],kind='Line')
    #plt.plot(Srilanka_economy["Year"],Srilanka_economy["GDP growth percentage"],label="Annual change in GDP growth",color='green')
    #plt.plot(Srilanka_economy["Year"],Srilanka_economy["Inflation Rate"],label="Inflation Rate",color='red')
    plt.savefig('linegraph.png')
    plt.title('Indian Imports and Exports of goods and services (f GDP)')
    plt.xlabel('Year')
    plt.ylabel('Data')
    plt.legend()
    plt.show()'''


'''def Read_Data(file_name): # Definig a function to read the file
    Read_Data=pd.read_csv(file_name) # To read the file
    Read_Data=data1.iloc[[12,21,41,71,180],[0,53,54,55,56,57,58,59,60,61,62]] # To select desired rows and columns using iloc function
    Read_Data=data1.set_axis(['Country','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018'],axis=1,inplace=False) # To assign desired index to given axis
    Read_Data.reset_index(drop=True, inplace=True) # Resetting the index values
    print(data1) # Printing the data
    data2=data1.set_index('Country').T # Transposing the data
    print(data2)'''

