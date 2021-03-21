def bubble_sort(list_to_sort: list):
    """ Recursively sort the parameter list_to_sort. """
    sorted_list = list_to_sort[:]
    iteration_num = 0
    for n in range(len(sorted_list) - 1):
        if sorted_list[n] > sorted_list[n + 1]:
            sorted_list[n], sorted_list[n + 1] = sorted_list[n + 1], \
                                                 sorted_list[n]
            iteration_num += 1
    if iteration_num == 0:
        return sorted_list
    else:
        return bubble_sort(sorted_list)


alphabet = ['g', 'w', 'e', 'y', 'l', 'j', 'r', 'v', 'o', 'h', 'p', 'n', 'x',
            'm', 'c', 'i', 'b', 'f', 'd', 't', 'k', 'z', 's', 'u', 'q', 'a']
sorted_alphabet = bubble_sort(alphabet)
print(sorted_alphabet)