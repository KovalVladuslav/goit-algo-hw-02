from collections import deque

def is_palindrome(input_string):
    # Очищаємо рядок від пробілів та приводимо до нижнього регістру
    clean_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Створюємо двосторонню чергу
    char_deque = deque(clean_string)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо не збігаються, це не паліндром
    
    return True  # Якщо всі символи збігаються, це паліндром

# Приклад використання:
test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')
