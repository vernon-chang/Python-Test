
import sys
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


# Read the data 
def load_data(file_path):
    # Declare global variables.

    global reaction_rates
    global reaction_list
    global reactant_list, product_list

    df = pd.read_csv(file_path, index_col = [1])
    # Delete unnamed information.
    reaction_rates = df.drop(df.columns[[0]], axis=1)

    # Get all the reactions.
    with open(file_path, 'r') as infile:
        reader = csv.DictReader(infile)
        reaction_names = reader.fieldnames
    del reaction_names[0:2]

    reaction_list = []
    # Remove spaces and rewrite all letters to lower case 
    for i in range(len(reaction_names)):
        reaction = reaction_names[i].replace(" ","").lower()
        reaction_list.append(reaction)

    reactant_list = []
    product_list = []
    reactant_list1 = []
    product_list1=[]
    # Rewrite all letters as lower case letters and separate into reactant list and product list
    for i in range(len(reaction_names)):
        reactant, product = (reaction_names[i]).lower().split(">")
        reactant_list1.append(reactant)
        product_list1.append(product)

    for i in range(len(reactant_list1)):
        reactant_separate = reactant_list1[i].strip().split(" + ")
        product_separate = product_list1[i].strip().split(" + ")
        reactant_list.append(reactant_separate)
        product_list.append(product_separate)
    
    return reaction_rates


# Task 1 Print all reactions at the specified times.
def output_all_reactions(time):
    global reaction_rates

    if(time not in reaction_rates.index):
        print('Please input a valid time.')
        sys.exit()
    else:
        data = reaction_rates.loc[[time]]

    return data
            

# Task 2 Get the n largest reaction rates based on the data and number selected by the user.
def find_the_nlargest(time, number):
    
    if(str(number).isdigit()):
        if(int(number) > 5 ):
            print('Up to five largest reaction rates can be returned. Please enter a number less than or equal to 5.')
            sys.exit()
        else:
            rr_names = []
            data = output_all_reactions(time)
            # The default sorting method is ascending, [::-1] puts the results in descending order.
            sorted_data = (np.sort(data.values.flatten()))[::-1]
            sorted_id = (np.argsort(data.values.flatten()))[::-1][0:int(number)]
            for i in range(len(sorted_id)):
                n = data.columns.values[sorted_id[i]]
                rr_names.append(n)
            
            print('The', int(number), 'largest reaction rates at', time, ':', sorted_data[0:int(number)] )
            print('For reaction', rr_names)
            plt.title('The n Largest Reaction Rates')
            plt.xlabel('Reactions')
            plt.ylabel('Reaction Rates')
            plt.xticks(rotation = 45, fontsize = 10)
            plt.plot(rr_names, sorted_data[0:int(number)], '-o')
            plt.show()
    
    else:
        print('Please input a valid digit, for example, "0" or "3".')
        sys.exit()



# Task 3 Get the specified reaction rates based on the data and reaction entered by the user.
def specific_reaction_rate(time, input):
    global reaction_rates
    global reaction_list

    data = output_all_reactions(time)
    # Remove spaces and rewrite all letters to lower case for input.
    input1 = (input.lower()).replace(" ","")

    # Compare reaction list and input and Use a counter to determine if a matching reaction exists.
    num = 0
    rr_names = []
    rr = []
    for i in range(len(reaction_list)):
        if(input1 == reaction_list[i]):
            num = num + 1
            n = data.columns.values[i]
            rr_names.append(n)
            v = data[data.columns.values[[i]]].values
            rr.append(list(v.flatten()))
            
    print('The Reaction Rates of', input, 'at', time, ':', rr)
    plt.title('The Specified Reaction Rates')
    plt.xlabel('Reactions')
    plt.ylabel('Reaction Rates')
    plt.plot(rr_names, rr, '-o')
    plt.show()

    if(num  == 0):
        print("There is no reaction to match the input.")
        

# Task 4 Get all reaction rates with specific products or reactants.
def specified_product_or_reactant(time, type, input): 

    global reactant_list, product_list
    result_list = []
    num = 0

    data = output_all_reactions(time)

    # Check if the input type matches the requirements and process the input to add input inclusivity.
    if(type == 'r' or type == 'R'):
        for i in range(len(reactant_list)):
            if(input.lower().replace(" ","") in reactant_list[i]):
                # Use the counter to check if there is a reaction matching the input. 
                num = num + 1
                result_list.append(data[data.columns.values[i]])
        if(num ==0):
            print('Nothing found,please try again.')
    elif(type == 'p' or type == 'P'):
        for i in range(len(product_list)):
            if(input.lower().replace(" ","") in product_list[i]):
                num = num + 1
                result_list.append(data[data.columns.values[i]])
        if(num ==0):
            print('Nothing found, please try again.')
    else:
        print("Please enter input data type. For eample, 'r' for reactants, 'p' for products. " )
    
    return result_list


# Task 5 Get five largest reaction rates with a specific product or reactant.
def specified_nlargest_reaction_rates(time, type, input, number):
    
    # Check that the number are as required.
    number_list = [1, 2, 3, 4, 5]
    if(number not in number_list):
        print('Up to five largest reaction rates can be returned. Please enter a number from 0 to 5. For example, 3.')
        sys.exit()
    else:
        result_list = specified_product_or_reactant(time, type, input)
        # List for reaction rates and specific data.
        rr_names = []
        s_data = []
        # Sort the data and index.
        for i in range(len(result_list)):
            s_data.append(result_list[i].values)
            sorted_data = (np.sort(np.array(s_data).flatten()))[::-1][0: number]
            sorted_id = (np.argsort(np.array(s_data).flatten()))[::-1][0: number]
        
        print(sorted_id)
        # Get the reaction with largest reaction rates.
        for j in range(len(sorted_id)):
            n = result_list[sorted_id[j]].name
            rr_names.append(n)
        print('At', time, 'the largest', number,'reaction rates are:', sorted_data[0:number])
        print('For reaction', rr_names)
   
    return sorted_data, rr_names


# # Task 6 Get all rates for reactions producing/consuming a specified species.
def rates_for_producing_or_consuming(time, type, input):
    
    global reactant_list, product_list
    result_list = []
    num = 0
    data = output_all_reactions(time)
    
    # Check if the input type matches the requirements and process the input to add input inclusivity.
    if(type == 'p' or type == 'P'):
        for i in range(len(product_list)):
            if(input.lower().replace(" ","") in product_list[i]):
                if(input.lower().replace(" ","") not in reactant_list[i]):
                    num= num + 1
                    result_list.append(data[data.columns.values[i]])
        if(num == 0): 
            print(input, "is not producing.")
        
    elif(type == 'c' or type == 'C'):
        for i in range(len(reactant_list)):
            if(input.lower().replace(" ","") in reactant_list[i]):
                if(input.lower().replace(" ","") not in product_list[i]):
                    result_list.append(data[data.columns.values[i]])
                    num= num + 1

        if(num == 0): 
            print(input, "is not consuming.")

    else:
        print("Please enter input data type. For eample, 'r' for reactants, 'p' for products. " )
        sys.exit()
    
    return result_list


# Task 7 Get five largest rates for reactions producing/consuming a specified species. 
def nlargest_rates_for_producing_or_consuming(time, type, input, number):
    
    # Check that the number are as required.
    number_list = [1, 2, 3, 4, 5]
    if(number not in number_list):
        print('Up to five largest reaction rates can be returned. Please enter a number from 0 to 5. For example, 3.')
        sys.exit()
    else:
        result_list = rates_for_producing_or_consuming(time, type, input)
        # List for reaction rates and specific data.
        rr_names = []
        s_data = []
        # Sort the data and index.
        for i in range(len(result_list)):
            s_data.append(result_list[i].values)
            sorted_data = (np.sort(np.array(s_data).flatten()))[::-1][0:number]
            sorted_id = (np.argsort(np.array(s_data).flatten()))[::-1][0:number]
        
        # Get the reaction with largest reaction rates.
        for j in range(len(sorted_id)):
            n = result_list[sorted_id[j]].name
            rr_names.append(n)
            
        print('At', time, 'the largest', number,'reaction rates are:', sorted_data[0:number])
        print('For reaction', rr_names)
   
    return sorted_data, rr_names
 

# Plot graphs for task 4, 5
def plot_figures_sp(time, type, input, number):
    
    spr = specified_product_or_reactant(time, type, input)

    if (spr != []):
        
        rr_name = []
        rr = []
        for i in range(len(spr)):
            n = spr[i].name
            rr_name.append(n)
            v = list(spr[i].values)
            rr.append(v)
        
        print('The Reaction Rates of', input.upper(), 'at', time, ':', rr)
        nl, nl_names = specified_nlargest_reaction_rates(time,type,input, number)
        plt.figure(figsize=(15,5))
        plt.title('The Specified Reaction Rates',fontsize = 20)
        plt.xlabel('Reactions')
        plt.xticks(rotation = 90, fontsize = 10)
        plt.ylabel('Reaction Rates')
        plt.plot(rr_name, rr, '-')  
        plt.scatter(nl_names, nl, color = 'r')
        plt.show()
    
    
# Plot graphs for task 6, 7
def plot_figures_sp_poc(time, type, input, number):
    result_list = rates_for_producing_or_consuming(time, type, input)
    
    rr_name = []
    rr = []
    for i in range(len(result_list)):
        n = result_list[i].name
        rr_name.append(n)
        v = list(result_list[i].values)
        rr.append(v)
        
    print('The Reaction Rates of', input.upper(), 'at', time, ':', rr)
    nl, nl_names = nlargest_rates_for_producing_or_consuming(time,type,input, number)
    plt.figure(figsize=(15,5))
    plt.title('The Specified Reaction Rates',fontsize = 20)
    plt.xlabel('Reactions')
    plt.xticks(rotation = 90, fontsize = 10)
    plt.ylabel('Reaction Rates')
    plt.plot(rr_name, rr, '-')  
    plt.scatter(nl_names, nl, color = 'r')
    plt.show()

   

if __name__ == "__main__":
    # Enter the data address in brackets to load the data.
    reaction_rates = load_data('/Users/vernon/Desktop/TestReactionRates.csv')

    # 1) All reaction rates.
    #reactions = output_all_reactions(0.4)
    #print(reactions)

    # 2) The 5 largest reaction rates.
    #lrr = find_the_nlargest(0.4, 5)
    #print(lrr)
    

    # 3) The rate for a specific reaction.
    #specific_reaction_rate(0.2, 'e- + H2 > e- + e- + H2+')

    # 4) All rates for reactions having a specified product or reactant
    #spr = specified_product_or_reactant(0.3, 'p', 'Nh3')
    #print(spr)

    # 5) The (up to) 5 largest reaction rates for reactions having a specified product or reactants
    #result = specified_nlargest_reaction_rates(0.3,'p','nh3', 5)
    
    # 6) All rates for reactions producing/consuming a specified species
    #result_list = rates_for_producing_or_consuming(0.0, 'p', 'h')
    #print(result_list)
    
    
    # 7) The (up to) 5 largest rates for reactions producing/consuming a specified species.
    #nlargest_rates_for_producing_or_consuming(0.1, 'c', 'e-', 5)
    
    # 8) Plot the results of the data 
    #plot_figures_sp(0.0, 'r', 'nh3', 5)
    #plot_figures_sp_poc(0.3, 'c', 'nh3', 5)
     
    
    