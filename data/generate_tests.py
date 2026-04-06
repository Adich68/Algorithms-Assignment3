import random

alphabet = ['a', 'b', 'c', 'd', 'e']
values = {'a': 2, 'b': 4, 'c': 5, 'd': 3, 'e': 1}

sizes = [25, 50, 100, 200, 300, 400, 500, 600, 700, 800]

for i, size in enumerate(sizes):
    A = ''.join(random.choices(alphabet, k=size))
    B = ''.join(random.choices(alphabet, k=size))
    filename = f"data/test{i+1}.in"
    with open(filename, 'w') as f:
        f.write(f"{len(alphabet)}\n")
        for char, val in values.items():
            f.write(f"{char} {val}\n")
        f.write(A + "\n")
        f.write(B + "\n")
    print(f"Generated {filename} with string length {size}")