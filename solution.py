def grille(message, code):
    binary_code_reversed = bin(code).replace("0b", "")[::-1]
    message_reversed = message[::-1]

    decrypted_message_reversed = ""
    for sign_index, sing in enumerate(binary_code_reversed):
        if sing == "1" and sign_index < len(message_reversed):
            decrypted_message_reversed += message_reversed[sign_index]

    return decrypted_message_reversed[::-1]
