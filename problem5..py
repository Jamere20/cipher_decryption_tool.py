def create_mapping(plaintext, ciphertext):
    mapping = {}
    for p, c in zip(plaintext, ciphertext):
        mapping[c] = p
    return mapping

def decrypt_message(mapping, ciphertext):
    decrypted_message = ''
    for c in ciphertext:
        decrypted_message += mapping.get(c, '.')
    return decrypted_message

# Input
plaintext = input().strip()
ciphertext1 = input().strip()
ciphertext2 = input().strip()

# Create mapping
mapping = create_mapping(plaintext, ciphertext1)

# Decrypt second ciphertext
decrypted_message = decrypt_message(mapping, ciphertext2)

# Output
print(decrypted_message)
