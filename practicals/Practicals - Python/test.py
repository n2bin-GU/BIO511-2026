sequence = "GATTACAGAACTGATAC"

max_a = 7

position = -1
a_count = 0

while a_count < max_a:
    position += 1
    if sequence[position] == "A":
        a_count += 1

print(f"The third A is at position {position}")

# Solution using a for loop
a_count = 0

for position in range(len(sequence)):
    if sequence[position] == "A":
        a_count += 1

        if a_count == max_a:
            break

print(f"The third A is at position {position}")

