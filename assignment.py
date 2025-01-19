# Part 1: Python Syntax
def format_string(name, age):
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"

def loop_sum(n):
    return sum(range(1, n + 1))

# Part 2: Data Structures
def list_operations(numbers):
    return sum(numbers), max(numbers), min(numbers)

def dict_operations(students_dict):
    """
    Take a dictionary of student names and scores.
    Return a list of names of students who scored above 80.
    """
    return [name for name, score in students_dict.items() if score > 80]


def set_operations(list1, list2):
    """Returns a set of common elements between two lists."""
    return set(list1).intersection(list2)



# Part 3: Operators
def arithmetic_ops(a, b):
    """Performs arithmetic operations and returns a dictionary of results."""
    results = {
        'sum': a + b,
        'difference': a - b,
        'product': a * b,
    }
    try:
        results['quotient'] = a / b
    except ZeroDivisionError:
        results['quotient'] = "undefined (division by zero)"
    return results

def logical_ops(x, y):
    """Performs logical operations and returns a dictionary of results."""
    return {
        'and': x and y,
        'or': x or y,
        'not_x': not x
    }

def bitwise_ops(a, b):
    """
    Return a dictionary with:
    - 'and': a & b
    - 'or': a | b
    - 'xor': a ^ b
    """
    return {
        'and': a & b,
        'or': a | b,
        'xor': a ^ b
    }