from PIL import Image
XOR_KEY = 123

def xor_encrypt_decrypt(text):
    result = ""
    for char in text:
        result += chr(ord(char) ^ XOR_KEY)
    
    return result

def text_to_binary(text):
    
    binary = ""

    for character in   text:
        binary_char = format(ord(character), '08b')
        binary += binary_char

    return binary
def encode_message(image_path, secret_message):
        image = Image.open(image_path).convert("RGB")
        encrypted_message = xor_encrypt_decrypt(secret_message)
        secret_message = "START###" + encrypted_message + "#####"
        binary_message = text_to_binary(secret_message)

        pixels = image.load()
        width, height = image.size

        binary_index=0

        for y in range(height):
            for x in range(width):
                r,g,b =pixels[x,y]
                if binary_index < len(binary_message):
                    r = (r & ~1) | int(binary_message[binary_index])
                    binary_index += 1

                pixels[x,y] = (r,g,b)

                if binary_index >= len(binary_message):
                    break
            
            if binary_index >= len(binary_message):
                break
    
        output_path = f"encoded/encoded_image.png"
    
        image.save(output_path,format="PNG")

        return output_path 


 

def decode_message(image_path):
    image = Image.open(image_path).convert("RGB")
    pixels = image.load()
    width, height = image.size

    binary_data = ""
    decoded_text = ""
    for y in range(height):
        for x in range(width):
            r,g,b = pixels[x,y]
            binary_data += str(r & 1)

            if len(binary_data) == 8:        
                character = chr(int(binary_data, 2))
                decoded_text += character
                binary_data = ""

                if "START###" in decoded_text:
                    start_index = decoded_text.find("START###") + len("START###")
                    actual_message = decoded_text[start_index:]

                    if "#####" in actual_message:
                        end_index = actual_message.find("#####")
                        encrypted_message = actual_message[:end_index]

                        decrypted_message = xor_encrypt_decrypt(encrypted_message)

                        return decrypted_message
                
    return "No Hidden Message Found"

