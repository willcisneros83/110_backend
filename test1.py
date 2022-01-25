
# create and call a functin that prints your name
# execute the script 


def print_name():
    print("Will Cisneros")





def list1():
    print("Working with lists (arrays)")

    names = ['John', 'Juan']

    # add values to the list
    names.append("Carlos")
    names.append("Charles")

    #  get the values
    print(names[0])
    print(names[3])

    print(names)


#  for loops
    for name in names:
        print(name)


def list2():
    print("-" * 30)

    nums = [123,456,123,3456,6,689,23,6,8,7887,123,46,3,89,12,9,9,565,8,33,1,-200,23]

    #  1 - print the sum of all numbers
    total = 0 
    for n in nums:
        total += n 
    
    print(total)


    # 2 - print numbers lower than 50
    #  2b - count how many numbers are lower than 50

    count = 0 
    for num in nums:
        if(num < 50):
            print(num)
            count += 1

    print(f"There are: {count} nums lower than 50")

    # 3 - find he smallest number in the list
    # variable that starts with any number from the list (first)
    # for loop
    # compare if the number is lower than your smallest number,
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    print(f"The smallest in the list is: {smallest}") 










def dict1():
    print("Dictionary tests 1 ---------------------")


    me = {
        "name": "Will",
        "last": "Cisneros",
        "age": 38,
        "hobbies": [],
        "address": {
            "street": "Evergreen",
            "number": 42,
            "city": "Springfield"
        }
    }

    print(me["name"])

    print(me["name"] + " " + me["last"])

    me["age"] = 99

    me["email"] = "will.cisneros@yahoo.com"

    print( me )



    # print the full address in a single string
    address = me["address"]
    print(f"{address['number']} {address['street']} {address['city']}")




print_name()
list1()

list2()
dict1()