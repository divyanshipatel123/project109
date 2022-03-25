import statistics
import plotly.figure_factory as ff 
import csv 
import pandas as pd
df = pd.read_csv("SP.csv")
# the data of the math score will be taken from the dataframe 
data = df["math score"].tolist()
# finding the central tendency and the standard deviation
mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)
stdDeviation = statistics.stdev(data)
print(mean , "  id the mean of the math score from the dataset")
print(mode , "  id the mode of the math score from the dataset")
print(median , "  id the median of the math score from the dataset")
print(stdDeviation , "  id the standard deviation of the math score from the dataset")
# finding propability from standard deviation pointing the standard deviations 
start_1_sd , end_1_sd = mean - stdDeviation,mean + stdDeviation
start_2_sd , end_2_sd = mean - (stdDeviation*2),mean + (stdDeviation*2)
start_3_sd , end_3_sd = mean - (stdDeviation*3),mean + (stdDeviation*3)
# finding values in between standard deviations
# the below code is in one line states result = the result between the standard deviations = lists
listOfDataIn_1_sd = [result for result in data if result > start_1_sd and result < end_1_sd]
listOfDataIn_2_sd = [result for result in data if result > start_2_sd and result < end_2_sd]
listOfDataIn_3_sd = [result for result in data if result > start_3_sd and result < end_3_sd]
# printing the probabilities
print("{}% of the data lies in the first standard deviation of the math score from the dataset".format(len(listOfDataIn_1_sd)*100/len(data)))
print("{}% of the data lies in the second standard deviation of the math score from the dataset".format(len(listOfDataIn_2_sd)*100/len(data)))
print("{}% of the data lies in the third standard deviation of the math score from the dataset".format(len(listOfDataIn_3_sd)*100/len(data)))

# plotting distribution graph
fig  = ff.create_distplot([data],["The math scores"],show_hist=False)
fig.show()
