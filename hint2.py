
#Hint:"Got some extra time to burn? Feel free to read every line and enjoy a stroll down Procrastination Lane.
#  But if you're sharp and want to save time, crack the hint from the previous file—your brain will thank you!"












# Function 1: Calculate Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    














# Function 2: Print "Hello, State Meets"
def print_hello_state_meets():
    print("Hello, State Meets!")














# Function 3: Story of Zeus
def story_of_zeus():
    story = """
    Zeus, in ancient Greek religion, is the god of the sky and thunder, and the king of the gods of Mount Olympus.
    Zeus is the child of Cronus and Rhea, the youngest of his siblings to be born. However, he was saved from being 
    swallowed by his father by his mother, who tricked Cronus into swallowing a stone wrapped in cloth. 
    Zeus later freed his brothers and sisters, leading the charge in overthrowing Cronus and the other Titans.
    """
    print(story)






















# Function 4: Story of Athena
def story_of_athena():
    story = """
    Athena is one of the major goddesses in Greek mythology. She is the daughter of Zeus and is known as the goddess
    of wisdom, courage, and warfare. According to legend, Athena was born fully armored and out of the forehead of Zeus
    after he swallowed her mother, Metis. Athena was known for her strategic skill in warfare and for being the protector
    of cities, especially Athens.
    """
    print(story)


















# Function 5: Basic addition function
def add_two_numbers(a, b):
    return a + b




































# Function 6: Simple string reversal
def reverse_string(s):
    return s[::-1]





















# Function 7: Prime number checker
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True







































# Function 8: Print Fibonacci sequence up to n terms
def fibonacci(n):
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq





















































# Function 9: Print the first n squares
def print_squares(n):
    for i in range(1, n + 1):
        print(i ** 2)




















































# Function 10: Check for palindrome
def is_palindrome(s):
    return s == s[::-1]











































# Function 11: Return the nth Fibonacci number
def nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a






























# Function 12: Sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))






























# Function 13: Check if number is even
def is_even(n):
    return n % 2 == 0





























# Function 14: Return cube of a number
def cube(n):
    return n ** 3
























# Function 15: Generate a list of n random numbers
import random
def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]











































# Function 16: Print "Python is fun!"
def print_python_is_fun():
    print("Python is fun!")






























# Function 17: Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

































# Function 18: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9





























# Function 19: Multiply two numbers
def multiply(a, b):
    return a * b
















































# Function 20: Print ASCII values of a string
def print_ascii_values(s):
    for char in s:
        print(f"ASCII value of {char} is {ord(char)}")































































# Function 100: Find the largest number in a list
def find_largest_number(lst):
    if not lst:
        return None
    largest = lst[0]
    for number in lst:
        if number > largest:
            largest = number
    return largest




















































# Continuation of adding more simple functions...

























# Function 101: Check if a number is odd
def is_odd(n):
    return n % 2 != 0






















# Function 102: Greet a user with name
def greet_user(name):
    print(f"Hello, {name}!")






























# ... (Add similar functions till line 2000)

# Function 1000: Print the story of Poseidon
def story_of_poseidon():
    story = """
    Poseidon, god of the sea, earthquakes, and horses, is one of the twelve Olympian deities of ancient Greece. He is 
    the brother of Zeus and Hades. Poseidon is known for his trident, a three-pronged spear, which he used to create 
    storms and earthquakes. He was highly venerated by sailors, and his Roman equivalent is Neptune.
    """
    print(story)






















    
# Function 103: Calculate the area of a circle
def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

# Function 104: Convert kilometers to miles
def kilometers_to_miles(km):
    return km * 0.621371

# Function 105: Convert miles to kilometers
def miles_to_kilometers(miles):
    return miles / 0.621371

# Function 106: Print all even numbers up to n
def print_even_numbers(n):
    for i in range(0, n + 1, 2):
        print(i)

# Function 107: Generate a list of squares up to n
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

# Function 108: Calculate the perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# Function 109: Calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Function 110: Print the first n odd numbers
def print_odd_numbers(n):
    for i in range(1, n * 2, 2):
        print(i)

# Function 111: Check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Function 112: Count the number of vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Function 113: Reverse the digits of a number
def reverse_digits(n):
    return int(str(n)[::-1])

# Function 114: Print the multiplication table of a number
def print_multiplication_table(n, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{n} x {i} = {n * i}")

# Function 115: Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Function 116: Convert a list of strings to uppercase
def convert_to_uppercase(lst):
    return [s.upper() for s in lst]

# Function 117: Find the second largest number in a list
def second_largest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

# Function 118: Print the first n prime numbers
def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

# Function 119: Return the sum of the first n natural numbers
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

# Function 120: Return the nth triangular number
def triangular_number(n):
    return (n * (n + 1)) // 2

# Function 121: Convert a decimal number to binary
def decimal_to_binary(n):
    return bin(n)[2:]

# Function 122: Convert a binary number to decimal
def binary_to_decimal(b):
    return int(b, 2)

# Function 123: Generate a list of random floats
def generate_random_floats(n):
    return [random.uniform(0, 100) for _ in range(n)]

# Function 124: Find the median of a list
def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Function 125: Find the mode of a list
from collections import Counter
def find_mode(lst):
    count = Counter(lst)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

# Function 126: Calculate the distance between two points
def distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Function 127: Check if a string contains only alphabets
def is_alpha(s):
    return s.isalpha()

# Function 128: Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function 129: Find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function 130: Generate a random password of length n
import string
def generate_random_password(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))

# Function 131: Find all divisors of a number
def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Function 132: Capitalize the first letter of each word in a string
def capitalize_words(s):
    return s.title()

# Function 133: Return the first n terms of the arithmetic sequence
def arithmetic_sequence(a, d, n):
    return [a + i * d for i in range(n)]

# Function 134: Calculate the compound interest
def compound_interest(principal, rate, time, times_compounded_per_year):
    return principal * (1 + rate / times_compounded_per_year) ** (times_compounded_per_year * time)

# Function 135: Merge two dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Function 136: Check if two numbers are co-prime
def are_coprime(a, b):
    return gcd(a, b) == 1

# Function 137: Return the factorial of a number using iteration
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function 138: Find the sum of the squares of the first n numbers
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

# Function 139: Print the story of Hades
def story_of_hades():
    story = """
    Hades is the god of the underworld in Greek mythology. He is the brother of Zeus and Poseidon and the ruler of the dead.
    Though often depicted as a dark and morose figure, Hades is not evil but rather a just and stern ruler of the dead.
    His Roman equivalent is Pluto, and he is often associated with wealth, as the underworld was thought to hold great riches.
    """
    print(story)

# Function 140: Return a list of the first n triangular numbers
def generate_triangular_numbers(n):
    return [triangular_number(i) for i in range(1, n + 1)]

# Continue adding functions to reach the total line count needed...
# Function 1: Story of Zeus
def story_of_zeus():
    story = """
    Zeus is the king of the gods in Greek mythology. He is the god of the sky, lightning, and thunder.
    Zeus overthrew his father, Cronus, and freed his siblings from his father’s stomach. He then led the
    Olympian gods in a war against the Titans, resulting in their victory.
    """
    print(story)

# Function 2: Story of Hera
def story_of_hera():
    story = """
    Hera is the queen of the gods and the goddess of marriage and family. She is the wife of Zeus
    and is often portrayed as jealous due to Zeus's many affairs. Hera was also worshipped as a
    protector of women during childbirth.
    """
    print(story)

# Function 3: Story of Poseidon
def story_of_poseidon():
    story = """
    Poseidon, god of the sea, earthquakes, and horses, is one of the twelve Olympian deities. He is 
    the brother of Zeus and Hades. Poseidon is known for wielding a powerful trident and controlling
    the oceans and seas.
    """
    print(story)

# Function 4: Story of Athena
def story_of_athena():
    story = """
    Athena is the goddess of wisdom, war, and craftsmanship. She was born fully armored from the
    forehead of Zeus after he swallowed her mother, Metis. Athena is known for her strategic warfare
    skills and is the patron deity of Athens.
    """
    print(story)

# Function 5: Story of Hades
def story_of_hades():
    story = """
    Hades is the god of the underworld and the dead. He is the brother of Zeus and Poseidon. Unlike his
    brothers, Hades preferred to stay in the underworld, ruling over the souls of the departed. His domain 
    was also a place of great wealth, and he was associated with the riches beneath the earth.
    """
    print(story)

# Function 6: Story of Apollo
def story_of_apollo():
    story = """
    Apollo is the god of the sun, music, poetry, prophecy, and healing. He is the son of Zeus and Leto, and
    the twin brother of Artemis. Apollo is associated with the oracle at Delphi and is often depicted with a lyre.
    """
    print(story)

# Function 7: Story of Artemis
def story_of_artemis():
    story = """
    Artemis is the goddess of the hunt, wilderness, and childbirth. She is the twin sister of Apollo and
    is known for her independence and protection of animals and young women. Artemis was also associated
    with the moon.
    """
    print(story)

# Function 8: Story of Hephaestus
def story_of_hephaestus():
    story = """
    Hephaestus is the god of blacksmiths, metalworking, and craftsmanship. He is the son of Zeus and Hera,
    though he was cast out of Olympus due to his deformity. He is known for creating the weapons and armor of the gods.
    """
    print(story)

# Function 9: Story of Ares
def story_of_ares():
    story = """
    Ares is the god of war and represents the brutal and violent aspect of warfare. He is the son of Zeus
    and Hera and is often depicted in battle. Unlike Athena, who represented strategic warfare, Ares was
    more associated with the chaos and bloodshed of battle.
    """
    print(story)

# Function 10: Story of Aphrodite
def story_of_aphrodite():
    story = """
    Aphrodite is the goddess of love, beauty, and desire. According to myth, she was born from the sea foam.
    She is often depicted as the most beautiful of the gods and is associated with both romantic and physical love.
    """
    print(story)

# Function 11: The Labors of Heracles
def labors_of_heracles():
    story = """
    Heracles, the son of Zeus and the mortal Alcmene, was forced to complete twelve labors as a punishment.
    These labors included slaying the Nemean Lion, capturing the Golden Hind of Artemis, and fetching the
    Apples of the Hesperides.
    """
    print(story)

# Function 12: The Trojan War
def story_of_trojan_war():
    story = """
    The Trojan War was a conflict between the Greeks and the city of Troy, sparked by the abduction of Helen by
    the Trojan prince Paris. The war lasted ten years and is famous for events like the Trojan Horse and the involvement
    of heroes like Achilles, Hector, and Odysseus.
    """
    print(story)

# Function 13: The Odyssey
def story_of_odyssey():
    story = """
    The Odyssey tells the story of Odysseus, a Greek hero, as he tries to return home after the Trojan War.
    During his journey, Odysseus encounters numerous challenges, including the Cyclops, the Sirens, and the witch
    Circe, before finally reaching his home in Ithaca.
    """
    print(story)

# Function 14: The Birth of Dionysus
def story_of_dionysus():
    story = """
    Dionysus is the god of wine, fertility, and theatre. He is the son of Zeus and the mortal Semele. After his mother
    died, Zeus sewed Dionysus into his thigh until he was ready to be born. Dionysus is associated with wild revelry and
    the growth of vines.
    """
    print(story)

# Function 15: Story of Persephone
def story_of_persephone():
    story = """
    Persephone is the daughter of Demeter and Zeus, and she became the queen of the underworld after being abducted
    by Hades. Her mother, Demeter, caused the earth to wither in her grief, leading to the creation of the seasons.
    Persephone spends part of the year in the underworld and part on earth, symbolizing the cycle of life and death.
    """
    print(story)

# Function 16: The Judgment of Paris
def story_of_judgment_of_paris():
    story = """
    The Judgment of Paris is a mythological story in which Paris, prince of Troy, was asked to judge who was the most
    beautiful among the goddesses Hera, Athena, and Aphrodite. Paris chose Aphrodite, who promised him the love of
    Helen, leading to the Trojan War.
    """
    print(story)

# Function 17: The Story of Pandora
def story_of_pandora():
    story = """
    Pandora was the first woman created by the gods, according to Greek mythology. She was given a box (or jar)
    by Zeus, which contained all the evils of the world. Pandora's curiosity led her to open the box, releasing
    the evils, but she managed to close it before hope could escape.
    """
    print(story)

# Function 18: The Story of Prometheus
def story_of_prometheus():
    story = """
    Prometheus was a Titan who defied Zeus by stealing fire from the gods and giving it to humanity. As a punishment,
    Zeus had Prometheus bound to a rock, where an eagle would eat his liver each day, only for it to regenerate and
    the process to begin anew. Prometheus symbolizes the quest for knowledge and defiance against tyranny.
    """
    print(story)

# Function 19: The Myth of Theseus and the Minotaur
def story_of_theseus_minotaur():
    story = """
    Theseus was a hero of Athens who entered the Labyrinth to slay the Minotaur, a creature that was half-man, half-bull.
    With the help of Ariadne, who gave him a ball of thread to retrace his steps, Theseus killed the Minotaur and
    freed Athens from the burden of human sacrifices to the creature.
    """
    print(story)

# Function 20: The Story of Orpheus and Eurydice
def story_of_orpheus_eurydice():
    story = """
    Orpheus was a legendary musician who fell in love with Eurydice. After her death, Orpheus descended into the underworld
    to bring her back. Hades allowed Eurydice to return with Orpheus, but on the condition that he must not look back at her
    until they reached the surface. Tragically, Orpheus looked back, and Eurydice was lost forever.
    """
    print(story)

# More functions can be added for other Greek myths like the tale of Medusa, the story of Icarus, the adventures of Jason and the Argonauts, etc.
# Function 1: Story of Zeus
def story_of_zeus():
    story = """
    Zeus is the king of the gods in Greek mythology. He is the god of the sky, lightning, and thunder.
    Zeus overthrew his father, Cronus, and freed his siblings from his father’s stomach. He then led the
    Olympian gods in a war against the Titans, resulting in their victory.
    """
    print(story)

# Function 2: Story of Hera
def story_of_hera():
    story = """
    Hera is the queen of the gods and the goddess of marriage and family. She is the wife of Zeus
    and is often portrayed as jealous due to Zeus's many affairs. Hera was also worshipped as a
    protector of women during childbirth.
    """
    print(story)

# Function 3: Story of Poseidon
def story_of_poseidon():
    story = """
    Poseidon, god of the sea, earthquakes, and horses, is one of the twelve Olympian deities. He is 
    the brother of Zeus and Hades. Poseidon is known for wielding a powerful trident and controlling
    the oceans and seas.
    """
    print(story)

# Function 4: Story of Athena
def story_of_athena():
    story = """
    Athena is the goddess of wisdom, war, and craftsmanship. She was born fully armored from the
    forehead of Zeus after he swallowed her mother, Metis. Athena is known for her strategic warfare
    skills and is the patron deity of Athens.
    """
    print(story)

# Function 5: Story of Hades
def story_of_hades():
    story = """
    Hades is the god of the underworld and the dead. He is the brother of Zeus and Poseidon. Unlike his
    brothers, Hades preferred to stay in the underworld, ruling over the souls of the departed. His domain 
    was also a place of great wealth, and he was associated with the riches beneath the earth.
    """
    print(story)

# Function 6: Story of Apollo
def story_of_apollo():
    story = """
    Apollo is the god of the sun, music, poetry, prophecy, and healing. He is the son of Zeus and Leto, and
    the twin brother of Artemis. Apollo is associated with the oracle at Delphi and is often depicted with a lyre.
    """
    print(story)

# Function 7: Story of Artemis
def story_of_artemis():
    story = """
    Artemis is the goddess of the hunt, wilderness, and childbirth. She is the twin sister of Apollo and
    is known for her independence and protection of animals and young women. Artemis was also associated
    with the moon.
    """
    print(story)

# Function 8: Story of Hephaestus
def story_of_hephaestus():
    story = """
    Hephaestus is the god of blacksmiths, metalworking, and craftsmanship. He is the son of Zeus and Hera,
    though he was cast out of Olympus due to his deformity. He is known for creating the weapons and armor of the gods.
    """
    print(story)

# Function 9: Story of Ares
def story_of_ares():
    story = """
    Ares is the god of war and represents the brutal and violent aspect of warfare. He is the son of Zeus
    and Hera and is often depicted in battle. Unlike Athena, who represented strategic warfare, Ares was
    more associated with the chaos and bloodshed of battle.
    """
    print(story)

# Function 10: Story of Aphrodite
def story_of_aphrodite():
    story = """
    Aphrodite is the goddess of love, beauty, and desire. According to myth, she was born from the sea foam.
    She is often depicted as the most beautiful of the gods and is associated with both romantic and physical love.
    """
    print(story)

# Function 11: The Labors of Heracles
def labors_of_heracles():
    story = """
    Heracles, the son of Zeus and the mortal Alcmene, was forced to complete twelve labors as a punishment.
    These labors included slaying the Nemean Lion, capturing the Golden Hind of Artemis, and fetching the
    Apples of the Hesperides.
    """
    print(story)

# Function 12: The Trojan War
def story_of_trojan_war():
    story = """
    The Trojan War was a conflict between the Greeks and the city of Troy, sparked by the abduction of Helen by
    the Trojan prince Paris. The war lasted ten years and is famous for events like the Trojan Horse and the involvement
    of heroes like Achilles, Hector, and Odysseus.
    """
    print(story)

# Function 13: The Odyssey
def story_of_odyssey():
    story = """
    The Odyssey tells the story of Odysseus, a Greek hero, as he tries to return home after the Trojan War.
    During his journey, Odysseus encounters numerous challenges, including the Cyclops, the Sirens, and the witch
    Circe, before finally reaching his home in Ithaca.
    """
    print(story)

# Function 14: The Birth of Dionysus
def story_of_dionysus():
    story = """
    Dionysus is the god of wine, fertility, and theatre. He is the son of Zeus and the mortal Semele. After his mother
    died, Zeus sewed Dionysus into his thigh until he was ready to be born. Dionysus is associated with wild revelry and
    the growth of vines.
    """
    print(story)

# Function 15: Story of Persephone
def story_of_persephone():
    story = """
    Persephone is the daughter of Demeter and Zeus, and she became the queen of the underworld after being abducted
    by Hades. Her mother, Demeter, caused the earth to wither in her grief, leading to the creation of the seasons.
    Persephone spends part of the year in the underworld and part on earth, symbolizing the cycle of life and death.
    """
    print(story)

# Function 16: The Judgment of Paris
def story_of_judgment_of_paris():
    story = """
    The Judgment of Paris is a mythological story in which Paris, prince of Troy, was asked to judge who was the most
    beautiful among the goddesses Hera, Athena, and Aphrodite. Paris chose Aphrodite, who promised him the love of
    Helen, leading to the Trojan War.
    """
    print(story)

# Function 17: The Story of Pandora
def story_of_pandora():
    story = """
    Pandora was the first woman created by the gods, according to Greek mythology. She was given a box (or jar)
    by Zeus, which contained all the evils of the world. Pandora's curiosity led her to open the box, releasing
    the evils, but she managed to close it before hope could escape.
    """
    print(story)

# Function 18: The Story of Prometheus
def story_of_prometheus():
    story = """
    Prometheus was a Titan who defied Zeus by stealing fire from the gods and giving it to humanity. As a punishment,
    Zeus had Prometheus bound to a rock, where an eagle would eat his liver each day, only for it to regenerate and
    the process to begin anew. Prometheus symbolizes the quest for knowledge and defiance against tyranny.
    """
    print(story)

# Function 19: The Myth of Theseus and the Minotaur
def story_of_theseus_minotaur():
    story = """
    Theseus was a hero of Athens who entered the Labyrinth to slay the Minotaur, a creature that was half-man, half-bull.
    With the help of Ariadne, who gave him a ball of thread to retrace his steps, Theseus killed the Minotaur and
    freed Athens from the burden of human sacrifices to the creature.
    """
    print(story)

# Function 20: The Story of Orpheus and Eurydice
def story_of_orpheus_eurydice():
    story = """
    Orpheus was a legendary musician who fell in love with Eurydice. After her death, Orpheus descended into the underworld
    to bring her back. Hades allowed Eurydice to return with Orpheus, but on the condition that he must not look back at her
    until they reached the surface. Tragically, Orpheus looked back, and Eurydice was lost forever.
    """
    print(story)

# More functions can be added for other Greek myths like the tale of Medusa, the story of Icarus, the adventures of Jason and the Argonauts, etc.
# Function 103: Calculate the area of a circle
def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

# Function 104: Convert kilometers to miles
def kilometers_to_miles(km):
    return km * 0.621371

# Function 105: Convert miles to kilometers
def miles_to_kilometers(miles):
    return miles / 0.621371

# Function 106: Print all even numbers up to n
def print_even_numbers(n):
    for i in range(0, n + 1, 2):
        print(i)

# Function 107: Generate a list of squares up to n
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

# Function 108: Calculate the perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# Function 109: Calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Function 110: Print the first n odd numbers
def print_odd_numbers(n):
    for i in range(1, n * 2, 2):
        print(i)

# Function 111: Check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Function 112: Count the number of vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Function 113: Reverse the digits of a number
def reverse_digits(n):
    return int(str(n)[::-1])

# Function 114: Print the multiplication table of a number
def print_multiplication_table(n, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{n} x {i} = {n * i}")

# Function 115: Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Function 116: Convert a list of strings to uppercase
def convert_to_uppercase(lst):
    return [s.upper() for s in lst]

# Function 117: Find the second largest number in a list
def second_largest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

# Function 118: Print the first n prime numbers
def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1
def ohh_did_n0t_expect_that():
    print("Mortal, you seek my downfall? Ha! There exists but one word in all realms—whispered by ancient tongues—that holds the power to shatter even my throne. It is a word so mighty, so absolute, that the very gods tremble at its utterance. But dare not speak it lightly, for with it comes the weight of eternity itself.")
    input1=input()
    if (input1=="omnipotent"):
        print("The pass key is: 0738e91f1ceb7c813190ec1f532b2b1b")
    else :
        print("Guess you are not strong enough!")
# Function 119: Return the sum of the first n natural numbers
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

# Function 120: Return the nth triangular number
def triangular_number(n):
    return (n * (n + 1)) // 2
ohh_did_n0t_expect_that()
# Function 121: Convert a decimal number to binary
def decimal_to_binary(n):
    return bin(n)[2:]

# Function 122: Convert a binary number to decimal
def binary_to_decimal(b):
    return int(b, 2)

# Function 123: Generate a list of random floats
def generate_random_floats(n):
    return [random.uniform(0, 100) for _ in range(n)]

# Function 124: Find the median of a list
def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Function 125: Find the mode of a list
from collections import Counter
def find_mode(lst):
    count = Counter(lst)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

# Function 126: Calculate the distance between two points
def distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Function 127: Check if a string contains only alphabets
def is_alpha(s):
    return s.isalpha()

# Function 128: Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function 129: Find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function 130: Generate a random password of length n
import string
def generate_random_password(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))

# Function 131: Find all divisors of a number
def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Function 132: Capitalize the first letter of each word in a string
def capitalize_words(s):
    return s.title()

# Function 133: Return the first n terms of the arithmetic sequence
def arithmetic_sequence(a, d, n):
    return [a + i * d for i in range(n)]

# Function 134: Calculate the compound interest
def compound_interest(principal, rate, time, times_compounded_per_year):
    return principal * (1 + rate / times_compounded_per_year) ** (times_compounded_per_year * time)

# Function 135: Merge two dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Function 136: Check if two numbers are co-prime
def are_coprime(a, b):
    return gcd(a, b) == 1

# Function 137: Return the factorial of a number using iteration
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function 138: Find the sum of the squares of the first n numbers
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

# Function 139: Print the story of Hades
def story_of_hades():
    story = """
    Hades is the god of the underworld in Greek mythology. He is the brother of Zeus and Poseidon and the ruler of the dead.
    Though often depicted as a dark and morose figure, Hades is not evil but rather a just and stern ruler of the dead.
    His Roman equivalent is Pluto, and he is often associated with wealth, as the underworld was thought to hold great riches.
    """
    print(story)

# Function 140: Return a list of the first n triangular numbers
def generate_triangular_numbers(n):
    return [triangular_number(i) for i in range(1, n + 1)]

# Continue adding functions to reach the total line count needed...
# Function 103: Calculate the area of a circle
def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

# Function 104: Convert kilometers to miles
def kilometers_to_miles(km):
    return km * 0.621371

# Function 105: Convert miles to kilometers
def miles_to_kilometers(miles):
    return miles / 0.621371

# Function 106: Print all even numbers up to n
def print_even_numbers(n):
    for i in range(0, n + 1, 2):
        print(i)

# Function 107: Generate a list of squares up to n
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

# Function 108: Calculate the perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# Function 109: Calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Function 110: Print the first n odd numbers
def print_odd_numbers(n):
    for i in range(1, n * 2, 2):
        print(i)

# Function 111: Check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Function 112: Count the number of vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Function 113: Reverse the digits of a number
def reverse_digits(n):
    return int(str(n)[::-1])

# Function 114: Print the multiplication table of a number
def print_multiplication_table(n, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{n} x {i} = {n * i}")

# Function 115: Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Function 116: Convert a list of strings to uppercase
def convert_to_uppercase(lst):
    return [s.upper() for s in lst]

# Function 117: Find the second largest number in a list
def second_largest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

# Function 118: Print the first n prime numbers
def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

# Function 119: Return the sum of the first n natural numbers
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

# Function 120: Return the nth triangular number
def triangular_number(n):
    return (n * (n + 1)) // 2

# Function 121: Convert a decimal number to binary
def decimal_to_binary(n):
    return bin(n)[2:]

# Function 122: Convert a binary number to decimal
def binary_to_decimal(b):
    return int(b, 2)

# Function 123: Generate a list of random floats
def generate_random_floats(n):
    return [random.uniform(0, 100) for _ in range(n)]

# Function 124: Find the median of a list
def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Function 125: Find the mode of a list
from collections import Counter
def find_mode(lst):
    count = Counter(lst)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

# Function 126: Calculate the distance between two points
def distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Function 127: Check if a string contains only alphabets
def is_alpha(s):
    return s.isalpha()

# Function 128: Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function 129: Find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function 130: Generate a random password of length n
import string
def generate_random_password(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))

# Function 131: Find all divisors of a number
def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Function 132: Capitalize the first letter of each word in a string
def capitalize_words(s):
    return s.title()

# Function 133: Return the first n terms of the arithmetic sequence
def arithmetic_sequence(a, d, n):
    return [a + i * d for i in range(n)]

# Function 134: Calculate the compound interest
def compound_interest(principal, rate, time, times_compounded_per_year):
    return principal * (1 + rate / times_compounded_per_year) ** (times_compounded_per_year * time)

# Function 135: Merge two dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Function 136: Check if two numbers are co-prime
def are_coprime(a, b):
    return gcd(a, b) == 1

# Function 137: Return the factorial of a number using iteration
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function 138: Find the sum of the squares of the first n numbers
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

# Function 139: Print the story of Hades
def story_of_hades():
    story = """
    Hades is the god of the underworld in Greek mythology. He is the brother of Zeus and Poseidon and the ruler of the dead.
    Though often depicted as a dark and morose figure, Hades is not evil but rather a just and stern ruler of the dead.
    His Roman equivalent is Pluto, and he is often associated with wealth, as the underworld was thought to hold great riches.
    """
    print(story)

# Function 140: Return a list of the first n triangular numbers
def generate_triangular_numbers(n):
    return [triangular_number(i) for i in range(1, n + 1)]

# Continue adding functions to reach the total line count needed...
# Function 103: Calculate the area of a circle
def area_of_circle(radius):
    import math
    return math.pi * radius ** 2

# Function 104: Convert kilometers to miles
def kilometers_to_miles(km):
    return km * 0.621371

# Function 105: Convert miles to kilometers
def miles_to_kilometers(miles):
    return miles / 0.621371

# Function 106: Print all even numbers up to n
def print_even_numbers(n):
    for i in range(0, n + 1, 2):
        print(i)

# Function 107: Generate a list of squares up to n
def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

# Function 108: Calculate the perimeter of a rectangle
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

# Function 109: Calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Function 110: Print the first n odd numbers
def print_odd_numbers(n):
    for i in range(1, n * 2, 2):
        print(i)

# Function 111: Check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Function 112: Count the number of vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Function 113: Reverse the digits of a number
def reverse_digits(n):
    return int(str(n)[::-1])

# Function 114: Print the multiplication table of a number
def print_multiplication_table(n, up_to=10):
    for i in range(1, up_to + 1):
        print(f"{n} x {i} = {n * i}")

# Function 115: Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Function 116: Convert a list of strings to uppercase
def convert_to_uppercase(lst):
    return [s.upper() for s in lst]

# Function 117: Find the second largest number in a list
def second_largest(lst):
    if len(lst) < 2:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) >= 2 else None

# Function 118: Print the first n prime numbers
def print_first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1

# Function 119: Return the sum of the first n natural numbers
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

# Function 120: Return the nth triangular number
def triangular_number(n):
    return (n * (n + 1)) // 2

# Function 121: Convert a decimal number to binary
def decimal_to_binary(n):
    return bin(n)[2:]

# Function 122: Convert a binary number to decimal
def binary_to_decimal(b):
    return int(b, 2)

# Function 123: Generate a list of random floats
def generate_random_floats(n):
    return [random.uniform(0, 100) for _ in range(n)]

# Function 124: Find the median of a list
def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Function 125: Find the mode of a list
from collections import Counter
def find_mode(lst):
    count = Counter(lst)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes if len(modes) > 1 else modes[0]

# Function 126: Calculate the distance between two points
def distance_between_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Function 127: Check if a string contains only alphabets
def is_alpha(s):
    return s.isalpha()

# Function 128: Find the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function 129: Find the least common multiple (LCM) of two numbers
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Function 130: Generate a random password of length n
import string
def generate_random_password(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(n))

# Function 131: Find all divisors of a number
def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

# Function 132: Capitalize the first letter of each word in a string
def capitalize_words(s):
    return s.title()

# Function 133: Return the first n terms of the arithmetic sequence
def arithmetic_sequence(a, d, n):
    return [a + i * d for i in range(n)]

# Function 134: Calculate the compound interest
def compound_interest(principal, rate, time, times_compounded_per_year):
    return principal * (1 + rate / times_compounded_per_year) ** (times_compounded_per_year * time)

# Function 135: Merge two dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Function 136: Check if two numbers are co-prime
def are_coprime(a, b):
    return gcd(a, b) == 1

# Function 137: Return the factorial of a number using iteration
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function 138: Find the sum of the squares of the first n numbers
def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

# Function 139: Print the story of Hades
def story_of_hades():
    story = """
    Hades is the god of the underworld in Greek mythology. He is the brother of Zeus and Poseidon and the ruler of the dead.
    Though often depicted as a dark and morose figure, Hades is not evil but rather a just and stern ruler of the dead.
    His Roman equivalent is Pluto, and he is often associated with wealth, as the underworld was thought to hold great riches.
    """
    print(story)

# Function 140: Return a list of the first n triangular numbers
def generate_triangular_numbers(n):
    return [triangular_number(i) for i in range(1, n + 1)]


