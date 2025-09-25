def encrypt_xor(text: str, key: str) -> str:
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

def decrypt_xor(encrypted_text: str, key: str) -> str:
    return encrypt_xor(encrypted_text, key)  # XOR is symmetric

def encrypt_caesar(text: str, shift: int) -> str:
    return ''.join(chr((ord(c) + shift) % 256) for c in text)

def decrypt_caesar(encrypted_text: str, shift: int) -> str:
    return ''.join(chr((ord(c) - shift) % 256) for c in encrypted_text)
