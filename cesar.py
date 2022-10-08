raw_input_str = "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
alphabet = "abcdefghijklmnopqrstuvwxyz"

input_str = raw_input_str.lower()

for shift in range(0, 26):
    output = ""
    for idx in range(0, len(input_str)):
        input_char = input_str[idx]
        input_char_idx = alphabet.find(input_char)
        if input_char_idx == -1:
            output = output + input_char
            continue
        shifted_char_idx = (input_char_idx + shift) % 26
        shifted_char = alphabet[shifted_char_idx]
        output = output + shifted_char

    print(output)

    for word in ["the", "are", "has", "had"]:
        if output.find(word) >= 0:
            print("^^^^^^^^^^^^^^^^^")
            break

print("")