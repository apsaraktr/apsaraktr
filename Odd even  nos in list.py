def custom_sort(input_list):
    # Separate elements in odd and even positions
    odd_elements = [input_list[i] for i in range(len(input_list)) if i % 2 == 0]  # 1-based odd
    even_elements = [input_list[i] for i in range(len(input_list)) if i % 2 == 1]  # 1-based even

    # Sort odd positions in descending order and even positions in ascending order
    odd_elements.sort(reverse=True)
    even_elements.sort()

    # Merge sorted odd and even elements back into the list
    sorted_list = []
    odd_index, even_index = 0, 0
    for i in range(len(input_list)):
        if i % 2 == 0:
            sorted_list.append(odd_elements[odd_index])
            odd_index += 1
        else:
            sorted_list.append(even_elements[even_index])
            even_index += 1

    return sorted_list

# Test the function
input_list = [1, 3, 2, 8, 5, 7, 4, 6]
print("Original list:", input_list)
print("Sorted list:", custom_sort(input_list))


output


Original list: [1, 3, 2, 8, 5, 7, 4, 6]
Sorted list: [5, 3, 4, 6, 2, 7, 1, 8]
