from time import perf_counter
import random
import statistics

'''
Assignment 1
Question 3
This program assesses on what conditions is a linear search and binary search faster than each other
Created by: Brie Basma Chabi
CISC 235
'''


def linear_search(array_s, e):
    """
    This function conducts a linear search on array_s in order to find element e
    :param array_s: A list that will be searched on
    :param e: The element to be searched for
    :return: Boolean depending if element e was found
    """
    index = 0
    found = False

    while index < len(array_s) and not found:

        if array_s[index] == e:
            found = True
        else:
            index = index + 1
    return found


def binary_search(array_s, e):
    """
    This function conducts a binary search on array_s in order to find element e.
    This is done so by halving the array into smaller sections.
    :param array_s: A list that will be searched on
    :param e: The element to be searched for
    :return: Boolean depending if element e was found
    """
    first_index = 0
    last_index = len(array_s) - 1
    found = False

    while first_index <= last_index and not found:
        mid_index = (first_index + last_index) // 2
        if array_s[mid_index] == e:
            found = True
        else:
            if e < array_s[mid_index]:
                last_index = mid_index - 1
            else:
                first_index = mid_index + 1
    return found


def merge_sort(array_s):
    """
    This function divides an unsorted list (array_s) into sub lists that will be subsequently
    merged together to create 1 sorted list.
    :param array_s: A list that will be sorted
    :return: None
    """
    if len(array_s) > 1:
        middle_index = len(array_s) // 2
        left_half = array_s[:middle_index]
        right_half = array_s[middle_index:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array_s[k] = left_half[i]
                i += 1
            else:
                array_s[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array_s[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array_s[k] = right_half[j]
            j += 1
            k += 1


if __name__ == '__main__':

    '''
    My results are as followed:
    N = 1000 K = 51
    N = 5000 K = 62
    N = 10,000 K = 68
    '''

    # The desired number of N to be inputted here
    n = 1000
    s = []  # This array will be filled with N amount of even numbers
    for i in range(n):
        even_rand_num = random.randrange(2, 100, 2)
        s.append(even_rand_num)

    # The desired number of K to be inputted here
    k = 51
    target = random.sample(s, k // 2)  # K is initialized with K//2 number of elements derived from S.
    for i in range(k // 2):
        odd_rand_num = random.randrange(1, 100, 2)
        target.append(odd_rand_num)  # It is then filled with K//2 number of odd numbers
    random.shuffle(target)

    A1_results = []  # This array will hold the results of the linear search time
    A2_results = []  # This array will hold the results of the binary search time

    print("When K is", k, "and N is", n, ",the following search times are found:")
    print("Search time for Linear search:")
    # The Loop is conducted 3 times for reliability
    for i in range(3):
        t1_start = perf_counter()  # Timer for linear search time starts here
        for i in target:
            linear_search(s, i)
        t1_stop = perf_counter()  # Timer for linear search time stops here
        A1_results.append(((t1_stop - t1_start) * 1000))
        print((t1_stop - t1_start) * 1000)

    print("Search time for Binary Search:")
    t2_start = perf_counter()  # This timer will count the merge sort time once to not merge 3 times in the loop.
    merge_sort(s)
    t2_stop = perf_counter()
    for i in range(3):
        t3_start = perf_counter()  # Timer for binary search time starts here
        for i in target:
            binary_search(s, i)
        t3_stop = perf_counter()  # Timer for binary search time stops here
        A2_results.append(((t2_stop - t2_start) + (t3_stop - t3_start)) * 1000)
        print(((t2_stop - t2_start) + (t3_stop - t3_start)) * 1000)

    # This if statement assesses the average of A1_results and A2_results and prints into the console which is faster.
    if statistics.mean(A2_results) < statistics.mean(A1_results):
        print("Binary search is faster for K:", k, "for N:", n)
    else:
        print("Linear search is faster for K:", k, "for N =", n)
