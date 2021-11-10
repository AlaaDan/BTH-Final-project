dic = {}
dic_list = []
dic_list2 = []

def into():
    menu = True
    while menu:
        print('''1. Ask for the name of the file to be loaded 
2. Search for a person. Enter the ID and view the person's data
3. Who has the highest salary?
4. Sort the people and their data at different intervals 
5. Update the salary for all (New file created)
6. Which is the average salary for all employees
7. Exit ''')
        user_input = input("What do you want me to do ? ")
        if user_input == "1":
            file_name()
        if user_input == "2":
            view_data()
        if user_input == "3":
            highies_salary()
        if user_input == "4":
            sorting()
        if user_input == "5":
            update_salary()
        if user_input == "6":
            average()
        if user_input == "7":
            menu = False
        second_input = input("""If you wish to continue press any key to get the menu list again, 
Or press exit to exit the program? \n""")
        if second_input == "exit":
            print("Bye bye ")
            menu = False


def file_name():
    txt_name = input('Enter the file name: ')
    filenamn = open(f'C:/Users/Alaa\Desktop/new_project/{txt_name}.txt', "r")
    for line in filenamn:
        line_to_list = line.strip().split(",")
        dic_list.append(line_to_list) # we add every line into a list in group of list so we can access every line by it self
    #print(dic_list)
    for key in dic_list[0]: # dic_list[0] means to access only the first list in that group lists to get the key for the dic
        dic[key] = []  # I added the keys into the dictionary and gave them an empty list in order to add elements into each key
    #print(dic)
    for second_line in range(1, len(dic_list)): # To start from the second line in our file because the first line we took the keys from
        for item in range(len(dic_list[second_line])): # to access each index in every list
            dic[dic_list[0][item]].append(dic_list[second_line][item]) #  append every element into its key
    #print(f"our print{dic}")

    filenamn.close()

def view_data():
    id_view = []
    id_input = int(input("Please enter the user ID: "))
    for items in dic_list[id_input]:
        id_view.append(items)
    print(f"""ID: {id_view[0]}
First name: {id_view[1]}
Last name: {id_view[2]}
Salary: {id_view[3]}
Weight: {id_view[4]}""")

def highies_salary():
    print("The highest salary is", max(dic["montly_salary"]))


def sorting():
    under_20k = 0
    under_40k  = 0
    under_60k = 0
    under_80k = 0
    under_100k = 0
    for elements in dic['montly_salary']:
        elements = int(elements)
        #print(elements)
        if elements <= 200000 :
            under_20k+=1
        elif elements >= 200001 and elements <= 400000 :
            under_40k+=1
        elif elements >= 400001 and elements <= 600000 :
            under_60k+=1
        elif elements >= 600001 and elements <= 800000:
            under_80k+=1
        elif elements >= 800001 and elements <= 1000000:
            under_100k+=1
    print(f"""         < 200000 {under_20k} people
200000 - < 400000 {under_40k} people
400000 - < 600000 {under_60k} people
600000 - < 800000 {under_80k} people
800000 - < 1000000 {under_100k} people""")


def update_salary():
    txt_name = input('Enter the file name: ')
    filenamn = open(f'C:/Users/Alaa\Desktop/new_project/{txt_name}.txt', "r")
    new_content = ""
    for line in filenamn:
        line_to_list = line.strip().split(",")
        dic_list2.append(line_to_list)
    print("dic", dic_list2)
    for second in range (1, len(dic_list2)):
        #print("test elements", dic_list2[secon][3])
        elements = dic_list2[second]
    #for elements in dic_list:
        elements[3] = int(elements[3])
        print("Original", elements)
        if elements[3] < 500000:
            percentage = (elements[3] * 4) / 100
            elements[3] += percentage
        if elements[3] > 500000:
            percentage = (elements[3] * 2) / 100
            elements[3] += percentage
        print("Result", elements)
        new_content += f"{elements[0]},{elements[1]},{elements[2]},{str(elements[3])}\n"
    print(new_content)
    new_file_name = input("Name the file to save it: ")
    file2 = open(f'C:/Users/Alaa/Desktop/new_project/{new_file_name}.txt', "w")
    file2.write(new_content)
    file2.close()
    filenamn.close()


def average():
    count = 0
    sum_list= []
    for i in dic['montly_salary']:
        count+=1
        i = int(i)
        sum_list.append(i)
    #print(sum(sum_list))
    print("The average salary is", sum(sum_list) / count)



into()