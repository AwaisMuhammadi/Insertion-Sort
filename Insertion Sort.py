
list_of_numbers = []


def insertion_sort():
    n = len(list_of_numbers)  # length of the list
    i = 1
    while i < n:
        j = i-1
        current_element = list_of_numbers[i]
        while j >= 0 and current_element < list_of_numbers[j]:
            list_of_numbers[j+1] = list_of_numbers[j]  # move element one position ahead in list if condition satisfies
            j = j - 1
        list_of_numbers[j+1] = current_element
        i = i + 1


def take_input(n):  # take list of numbers from user
    for i in range(n):
        list_of_numbers.append(input("Enter number:"))


take_input(int(input("Enter Length of the list:")))  # length of list user wants to sort
insertion_sort()
print("Sorted List:")
print(list_of_numbers)