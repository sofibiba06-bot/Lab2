
operation = input()
pseudo_random_number = int(input())
rotors = []
for i in range(3):
    rotors.append(input())
message = input()

new_message = ""
if operation == "ENCODE":
    for i, letter in enumerate(message):
        new_message += chr((ord(letter) - ord("A") + i + pseudo_random_number) % 26 + ord("A"))

    new_rotor_message = ""
    for rotor in rotors:
        new_rotor_message = ""
        for i, letter in enumerate(new_message):
            new_message = new_message[:i] + rotor[ord(letter) - ord("A")] + new_message[i + 1:]


elif operation == "DECODE":
    new_message = message

    rotors = rotors[::-1]

    for rotor in rotors:
        for i, letter in enumerate(new_message):
            new_message = new_message[:i] + chr(rotor.find(letter) + ord("A")) + new_message[i + 1:]

    for i, letter in enumerate(new_message):
        index = ord(letter) - ord("A") - i - pseudo_random_number
        while index < 0:
            index += 26

        new_message = new_message[:i] + chr(index + ord("A")) + new_message[i + 1:]

print(new_message)