def number_count(num) -> int:
    return sum(int(number) for number in str(num) if number.isdigit())

def sort_list(integers: list) -> list:
    integers.sort(key=number_count)
    return integers

lst = [5, 31, 123, 80, 11] 
print(sort_list(lst))