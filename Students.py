import statistics as st
import pandas as pd
import csv

df = pd.read_csv("StudentsPerformance.csv")
data = df["math score"].tolist()
# Finding the mean, median, mode and standard deviation of the given data
mean = st.mean(data)
median = st.median(data)
mode = st.mode(data)
standardDeviation = st.stdev(data)

#  Find the standard deviation starting and ending points by subtracting the mean from
#  standard deviation and adding mean to the standard deviation respectively
std_dev_1_math_score_start,std_dev_1_math_score_end = (mean-standardDeviation),(mean+standardDeviation)
std_dev_2_math_score_start,std_dev_2_math_score_end = (mean-(2*standardDeviation)),(mean+(2*standardDeviation))
std_dev_3_math_score_start,std_dev_3_math_score_end = (mean-(3*standardDeviation)),(mean+(3*standardDeviation))

# Get the list of the data points between the standard deviation by looping on the results.
list_of_mathscore_within_1_std_dev = [result for result in data if result > std_dev_1_math_score_start and result < std_dev_1_math_score_end]
list_of_mathscore_within_2_std_dev = [result for result in data if result>std_dev_2_math_score_start and result< std_dev_2_math_score_end]
list_of_mathscore_within_3_std_dev = [result for result in data if result>std_dev_3_math_score_start and result< std_dev_3_math_score_end]

# Find the percentage of the data in the lists
print(" The % of math score which lie between 1 standard deviation is {}".format((len(list_of_mathscore_within_1_std_dev)*100)/len(data)))
print(" The % of math score which lie between 2 standard deviation is {}".format((len(list_of_mathscore_within_2_std_dev)*100)/len(data)))
print(" The % of math score which lie between 3 standard deviation is {}".format((len(list_of_mathscore_within_3_std_dev)*100)/len(data)))
