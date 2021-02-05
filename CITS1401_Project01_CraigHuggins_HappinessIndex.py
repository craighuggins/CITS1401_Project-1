# Author: Craig Ian Bond Huggins
# Version: 21
# Date: 20/09/2019
# Student ID: 22204675

import os

def generate_lists(filename):
    if not os.path.isfile(filename):   # checks if the input filename exists in the directory
        print("the file", filename, "does not exist in the folder")   # if the file doesnt exist, print an error message
        return(None)   #return None
    else:   #if the file does exist
        overall_data = []   # initialise a list to hold all of the data
        with open(filename,'r') as life:   # open the file provided as input in read mode
            life_data = life.readlines()   # read all the lines of the opened file
            for line in life_data[1:]:   # for each row in the .csv file apart from the first row (which contains the column headers)
                fields = line.split(',')   # split the string into individual elements separated by comma's
                length = int(len(fields))
                fields[7] = fields[7][:-1]   # trim the newline character from the end of each value in the last column 
                for i in range(1,length):   # for each column apart from the first column, which contains the country name
                    if fields[i] == '':   # if the cell is empty
                        fields[i] = None   # convert the empty cell to the None value
                    if fields[i] != None:
                        fields[i] = float(fields[i])   # if the cell is not None, convert the value to float
                overall_data.append(fields)   # fill the overall_data list with data from the opened .csv file
    return overall_data   # return the data to be used in later functions
             
             
def normalise_data(filename):
    fields = generate_lists(filename)
    length = len(fields)
    GDP = []   # initialise list for the 'GDP per capita' column data
    social_support = []   # initialise list for the 'Social Support' column data
    life_expectancy = []   # initialise list for the 'Life Expectancy' column data
    freedom = []   # initialise list for the 'Freedom to make life choices' column data
    generosity = []   # initialise list for the 'Generosity' column data
    confidence_govt = []   # initialise list for the 'Confidence in Government' column data
    norm_GDP = [0] * length   # initialise list to hold the normalised data for the 'GDP' column
    norm_social_support = [0] * length   # initialise list to hold the normalised data for the 'Social Support' column
    norm_life_expectancy = [0] * length   # initialise list to hold the normalised data for the 'Life Expectancy' column
    norm_freedom = [0] * length   # initialise list to hold the normalised data for the 'Freedom to make life choices' column
    norm_generosity = [0] * length   # initialise list to hold the normalised data for the 'Generosity' column
    norm_confidence_govt = [0] * length   # initialise list to hold the normalised data for the 'Confidence in Government' column
    
    for i in range(0,length):
        GDP.append(fields[i][2])   # populate the GDP list with data from the 'GDP per capita' column
        social_support.append(fields[i][3])   # populate the Social Support list with data from the 'Social Support' column
        life_expectancy.append(fields[i][4])   # populate the Life Expectancy list with data from the 'Life Expectancy' column
        freedom.append(fields[i][5])   # populate the Freedom list with data from the Freedom to make 'life choices' column
        generosity.append(fields[i][6])   # populate the Generosity list with data from the 'Generosity' column
        confidence_govt.append(fields[i][7])   # populate the Confidence list with data from the 'Confidence in Government' column
        
    min_GDP = min(x for x in GDP if x is not None)   # compute the smallest value in the GDP column, ignoring any None values
    max_GDP = max(x for x in GDP if x is not None)   # compute the largest value in the GDP column, ignoring any None values
    min_social_support = min(x for x in social_support if x is not None)   # compute the smallest value in the Social Support column, ignoring any None values
    max_social_support = max(x for x in social_support if x is not None)   # compute the largest value in the Social Support column, ignoring any None values
    min_life_expectancy = min(x for x in life_expectancy if x is not None)   # compute the smallest value in the Life Expectancy column, ignoring any None values
    max_life_expectancy = max(x for x in life_expectancy if x is not None)   # compute the largest value in the Life Expectancy column, ignoring any None values
    min_freedom = min(x for x in freedom if x is not None)   # compute the smallest value in the Freedom column, ignoring any None values
    max_freedom = max(x for x in freedom if x is not None)   # compute the largest value in the Freedom column, ignoring any None values
    min_generosity = min(x for x in generosity if x is not None)   # compute the smallest value in the Generosity column, ignoring any None values
    max_generosity = max(x for x in generosity if x is not None)   # compute the largest value in the Generosity column, ignoring any None values
    min_confidence_govt = min(x for x in confidence_govt if x is not None)   # compute the smallest value in the Confidence in Govt column, ignoring any None values
    max_confidence_govt = max(x for x in confidence_govt if x is not None)   # compute the largest value in the Confidence in Govt column, ignoring any None values

    for e in range(0,length):   # this loop transforms the data in every column (apart from the first 2) to normalised values
        if GDP[e] != None:
            norm_GDP[e] = (GDP[e] - min_GDP) / (max_GDP - min_GDP)   
        if social_support[e] != None:
            norm_social_support[e] = (social_support[e] - min_social_support) / (max_social_support - min_social_support)
        if life_expectancy[e] != None:
            norm_life_expectancy[e] = (life_expectancy[e] - min_life_expectancy) / (max_life_expectancy - min_life_expectancy)
        if freedom[e] != None:
            norm_freedom[e] = (freedom[e] - min_freedom) / (max_freedom - min_freedom)
        if generosity[e] != None:
            norm_generosity[e] = (generosity[e] - min_generosity) / (max_generosity - min_generosity)
        if confidence_govt[e] != None:
            norm_confidence_govt[e] = (confidence_govt[e] - min_confidence_govt) / (max_confidence_govt - min_confidence_govt)

    return fields, norm_GDP, norm_social_support, norm_life_expectancy, norm_freedom, norm_generosity, norm_confidence_govt   # return the normalised data for later use
    

def mean_calculation(filename):
    fields, GDP, SS, LE, FR, GE, CO = normalise_data(filename)   # capture the normalised data from the normalise_data() function
    length = len(fields)   # the number of countries being tested
    list_values = []   # list to hold the values for each column, row by row
    country = []   # list to hold the Country names
    score = []   # list to hold the computed scores for each country
    for i in range(0,length):
        list_values.append([GDP[i],SS[i],LE[i],FR[i],GE[i],CO[i]])   # fill the list with data from every column for each country
        country.append(fields[i][0])   # fill the list with the names of the countries
        score.append((sum(list_values[i]))/(len(list_values[i])))   # append the calculated mean for each country to the list
    
    score, country = zip(*sorted(zip(score, country)))   # sort the values in both lists, keeping the country-score pairs matched
    
    country = list(country)   # convert back to list
    score = list(score)   # convert back to list
    country.reverse()   # order the list in descending order
    score.reverse()   # order the list in descending order
    
    return fields, length, country, score   # return this data for use in the mean_list and mean_correlation functions
    
    
def mean_list(filename):
    
    fields, length, country, score = mean_calculation(filename)   # receive the data from the mean_calculation function
    
    for i in range(0,length):
        print(country[i], score[i])   # print the country, score pairs
        
        
def mean_correlation(filename):
    
    fields, length, country, score = mean_calculation(filename)   # receive the data from the mean_calculation function
    
    country_life_ladder = []   # initialise list to hold the country names for the life ladder scores
    life_ladder = []   # initialise list to hold the life ladder scores
    
    for i in range(0,length):
        country_life_ladder.append(fields[i][0])   # append the Country Name list with corresponding data from the .csv file
        life_ladder.append(fields[i][1])   # append the Life Ladder list with corresponding data from the .csv file
        
    life_ladder, country_life_ladder = zip(*sorted(zip(life_ladder, country_life_ladder)))   # sort the values in both lists, keeping the country-score pairs matched
    
    life_ladder = list(life_ladder)   # convert back to list once sorted
    country_life_ladder = list(country_life_ladder)   # convert back to list once sorted
    
    life_ladder.reverse()   # order in descending order
    country_life_ladder.reverse()   # order in descending order

    difference = []   # initialise list to hold the 'Difference Between Ranks' values
    
    for i in range(0,length):   # for each rank in the 'mean' list
        for k in range(0,length):   # for each rank in the 'Life Ladder' list
            if (country[i] == country_life_ladder[k]):   # find matching Country names between the lists
                difference.append(abs(i-k))   # calculate the differences between country ranks and add it to the list of differences
                
    for e in range(0,length):
        difference[e] = (difference[e]**2)   # square each difference value

    total = 0
    total = sum(difference)   # sum the squared difference values
    
    coefficient = 1-(6*total)/(len(difference)*((len(difference)**2)-1))   # formula to calculate the Spearman Coefficient
    print(coefficient)
    
        
def harmonic_mean_calculation(filename):
    fields, GDP, SS, LE, FR, GE, CO = normalise_data(filename)
    length = len(fields)   # the number of countries being tested
    list_values = []
    list_without_zeros = [[] for _ in range(length)]   # create a new list-of-lists big enough to hold all the non-zero values
    country = []   # list to hold the country names
    score = []   # list to hold the computed scores for each country
    
    for i in range(0,length):
        list_values.append([GDP[i], SS[i], LE[i], FR[i], GE[i], CO[i]])

        for d in range(0,len(list_values[i])):
            if list_values[i][d] != 0:   # if the element value does not have a value of 0
                list_without_zeros[i].append(list_values[i][d])   # append all non-zero values to the new list
                
        for d in range(0,len(list_without_zeros[i])):   # for all elements in the new list that contains no zero values
            list_without_zeros[i][d] = 1/list_without_zeros[i][d]   # transform the element to the reciprocal of its value

        country.append(fields[i][0])   # fill the list with the names of the countries
        score.append(1/(sum(list_without_zeros[i])/len(list_without_zeros[i])))   # get the average of all reciprocals in the non-zero list, then calculate the reciprocal of that average
        
    score, country = zip(*sorted(zip(score, country)))   # sort the values in both lists, keeping the country-score pairs matched
    
    country = list(country)   # convert back to list
    score = list(score)   # convert back to list
    country.reverse()   # order the list in descending order
    score.reverse()   # order the list in descending order
    
    return fields, length, country, score   # return this data for use in the harmonic_mean_list and harmonic_mean_correlation functions
    
        
def harmonic_mean_list(filename):
    
    fields, length, country, score = harmonic_mean_calculation(filename)   # receive the data from the harmonic_mean_calculation function
    
    for i in range(0,length):
        print(country[i], score[i])   # print the country, score pairs
        
        
def harmonic_mean_correlation(filename):

    fields, length, country, score = harmonic_mean_calculation(filename)   # receive the data from the harmonic_mean_calculation function
        
    country_life_ladder = []  # initialise list to hold the country names for the life ladder scores
    life_ladder = []   # initialise list to hold the life ladder scores
    
    for i in range(0,length):
        country_life_ladder.append(fields[i][0])   # append the Country Name list with corresponding data from the .csv file
        life_ladder.append(fields[i][1])   # append the Life Ladder list with corresponding data from the .csv file
        
    life_ladder, country_life_ladder = zip(*sorted(zip(life_ladder, country_life_ladder)))  # sort the values in both lists, keeping the country-score pairs matched
    
    life_ladder = list(life_ladder)   # convert back to list once sorted
    country_life_ladder = list(country_life_ladder)   # convert back to list once sorted
    
    life_ladder.reverse()   # order in descending order
    country_life_ladder.reverse()   # order in descending order
        
    difference = []   # initialise list to hold the 'Difference Between Ranks' values
    
    for i in range(0,length):   # for each rank in the 'harmonic_mean' list
        for k in range(0,length):   # for each rank in the 'Life Ladder' list
            if (country[i] == country_life_ladder[k]):   # find matching Country names between the lists
                difference.append(abs(i-k))   # calculate the differences between country ranks and add it to the list of differences
                
    for e in range(0,length):
        difference[e] = (difference[e]**2)   # square each difference value
        
    total = 0
    total = sum(difference)   # sum the squared difference values
    
    coefficient = 1-(6*total)/(len(difference)*((len(difference)**2)-1))   # formula to calculate the Spearman Coefficient
    print(coefficient)
    
        
def median_calculation(filename):
    fields, GDP, SS, LE, FR, GE, CO = normalise_data(filename)
    length = len(fields)   # the number of countries being tested

    list_values = []
    country = []   # list to hold the country names
    score = []   # list to hold the computed scores for each country
    for i in range(0,length):
        list_values.append([GDP[i], SS[i], LE[i], FR[i], GE[i], CO[i]])
        list_values[i].sort()   # sort the values in order to get an accurate calculation of the median
        country.append(fields[i][0])   # fill the list with the names of the countries
        score.append(sum(list_values[i][(len(list_values[i])//2-1):(len(list_values[i])//2+1)])/2)   # append the calculated median for each country to the list
        
    score, country = zip(*sorted(zip(score, country)))   # sort the values in both lists, keeping the country-score pairs matched
        
    country = list(country)   # convert back to list
    score = list(score)   # convert back to list
    country.reverse()   # order the list in descending order
    score.reverse()   # order the list in descending order
    
    return fields, length, country, score   # return this data for use in the median_list and median_correlation functions


def median_list(filename):
    
    fields, length, country, score = median_calculation(filename)   # receive the data from the median_calculation function
    
    for i in range(0,length):
        print(country[i], score[i])   # print the country, score pairs
        
        
def median_correlation(filename):
    
    fields, length, country, score = median_calculation(filename)   # receive the data from the median_calculation function

    country_life_ladder = []  # initialise list to hold the country names for the life ladder scores
    life_ladder = []   # initialise list to hold the life ladder scores
    
    for i in range(0,length):
        country_life_ladder.append(fields[i][0])   # append the Country Name list with corresponding data from the .csv file
        life_ladder.append(fields[i][1])   # append the Life Ladder list with corresponding data from the .csv file
        
    life_ladder, country_life_ladder = zip(*sorted(zip(life_ladder, country_life_ladder)))   # sort the values in both lists, keeping the country-score pairs matched
    
    life_ladder = list(life_ladder)   # convert back to list once sorted
    country_life_ladder = list(country_life_ladder)   # convert back to list once sorted
    
    life_ladder.reverse()   # order in descending order
    country_life_ladder.reverse()   # order in descending order
        
    difference = []   # initialise list to hold the 'Difference Between Ranks' values
    
    for i in range(0,length):   # for each rank in the 'median' list
        for k in range(0,length):   # for each rank in the 'Life Ladder' list
            if (country[i] == country_life_ladder[k]):   # find matching Country names between the lists
                difference.append(abs(i-k))   # calculate the differences between country ranks and add it to the list of differences
                
    for e in range(0,length):
        difference[e] = (difference[e]**2)   # square each difference value

    total = 0
    total = sum(difference)   # sum the squared difference values
    
    coefficient = 1-(6*total)/(len(difference)*((len(difference)**2)-1))   # formula to calculate the Spearman Coefficient
    print(coefficient)
    
    
def min_calculation(filename):
    fields, GDP, SS, LE, FR, GE, CO = normalise_data(filename)
    length = len(fields)   # the number of countries being tested
    list_values = []
    country = []   # list to hold the country names
    score = []   # list to hold the computed scores for each country
    for i in range(0,length):
        list_values.append([GDP[i], SS[i], LE[i], FR[i], GE[i], CO[i]])
        country.append(fields[i][0])   # fill the list with the names of the countries
        score.append(min(list_values[i]))   # append the calculated minimum for each country to the list
        
    score, country = zip(*sorted(zip(score, country)))   # sort the values in both lists, keeping the country-score pairs matched
    
    country = list(country)   # convert back to list
    score = list(score)   # convert back to list
    country.reverse()   # order the list in descending order
    score.reverse()   # order the list in descending order
    
    return fields, length, country, score   # return this data for use in the min_list and min_correlation functions


def min_list(filename):
    
    fields, length, country, score = min_calculation(filename)   # receive the data from the min_calculation function
    
    for i in range(0,length):
        print(country[i], score[i])   # print the country, score pairs
        
        
def min_correlation(filename):
    
    fields, length, country, score = min_calculation(filename)   # receive the data from the min_calculation function

    country_life_ladder = []   # initialise list to hold the country names for the life ladder scores
    life_ladder = []   # initialise list to hold the life ladder scores
    
    for i in range(0,length):
        country_life_ladder.append(fields[i][0])   # append the Country Name list with corresponding data from the .csv file
        life_ladder.append(fields[i][1])   # append the Life Ladder list with corresponding data from the .csv file
        
    life_ladder, country_life_ladder = zip(*sorted(zip(life_ladder, country_life_ladder)))   # sort the values in both lists, keeping the country-score pairs matched
    
    life_ladder = list(life_ladder)   # convert back to list once sorted
    country_life_ladder = list(country_life_ladder)   # convert back to list once sorted
    
    life_ladder.reverse()   # order in descending order
    country_life_ladder.reverse()   # order in descending order
        
    difference = []   # initialise list to hold the 'Difference Between Ranks' values
    
    for i in range(0,length):   # for each rank in the 'min' list
        for k in range(0,length):   # for each rank in the 'Life Ladder' list
            if (country[i] == country_life_ladder[k]):   # find matching Country names between the lists
                difference.append(abs(i-k))   # calculate the differences between country ranks and add it to the list of differences
                
    for e in range(0,length):
        difference[e] = (difference[e]**2)   # square each difference value
        
    total = 0
    total = sum(difference)   # sum the squared difference values
    
    coefficient = 1-(6*total)/(len(difference)*((len(difference)**2)-1))   # formula to calculate the Spearman Coefficient
    print(coefficient)
    
    
def main():
    file_name = str(input("Enter the name of the file containing World Happiness computation data: "))
    if not os.path.isfile(file_name):
        print("The file name that you entered does not exist in the folder")
        return(None)
    metric = str(input("Select a metric to be tested. The option are: min, mean, median, harmonic_mean "))
    action = str(input("Select which action is to be performed on the data using the specified metric. \n Options are: list, correlation "))
    
    if metric == 'mean':
        if action == 'list':
            print("Ranked list of countries' happiness scores based on the", metric, "metric")
            mean_list(file_name)
        elif action == 'correlation':
            print("The correlation coefficient between the study ranking and the ranking using the", metric, "metric is")
            mean_correlation(file_name)
        else:
            print("You did not select one of the available actions. Please check your spelling, then try running the main() function again")
            return
        
    elif metric == 'median':
        if action == 'list':
            print("Ranked list of countries' happiness scores based on the", metric, "metric")
            median_list(file_name)
        elif action == 'correlation':
            print("The correlation coefficient between the study ranking and the ranking using the", metric, "metric is")
            median_correlation(file_name)
        else:
            print("You did not select one of the available actions. Please check your spelling, then try running the main() function again")
            return
        
    elif metric == 'min':
        if action == 'list':
            print("Ranked list of countries' happiness scores based on the", metric, "metric")
            min_list(file_name)
        elif action == 'correlation':
            print("The correlation coefficient between the study ranking and the ranking using the", metric, "metric is")
            min_correlation(file_name)
        else:
            print("You did not select one of the available actions. Please check your spelling, then try running the main() function again")
            return
        
    elif metric == 'harmonic_mean':
        if action == 'list':
            print("Ranked list of countries' happiness scores based on the", metric, "metric")
            harmonic_mean_list(file_name)
        elif action == 'correlation':
            print("The correlation coefficient between the study ranking and the ranking using the", metric, "metric is")
            harmonic_mean_correlation(file_name)
        else:
            print("You did not select one of the available actions. Please check your spelling and run the main() function again")
            return
        
    else:
        print("You did not select one of the available metrics for the data. Please check your spelling, then try running the main() function again")
        return
    