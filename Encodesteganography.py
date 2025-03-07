from PIL import Image

def encode_image(image_path, secret_message, output_path):
    # Load the image
    try:
        image = Image.open(image_path)
        print("Image loaded successfully.")
    except Exception as e:
        print(f"Error loading image: {e}")
        return
    
    encoded_image = image.copy()
    
    # Convert the image to RGB
    encoded_image = encoded_image.convert("RGB")
    width, height = encoded_image.size
    
    # Convert the secret message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
    binary_message += '1111111111111110'  # Delimiter to indicate end of message
    
    data_index = 0
    message_length = len(binary_message)
    
    # Encode the message into the image
    for y in range(height):
        for x in range(width):
            if data_index < message_length:
                pixel = list(encoded_image.getpixel((x, y)))
                # Modify the least significant bit of the blue channel
                pixel[2] = (pixel[2] & ~1) | int(binary_message[data_index])
                encoded_image.putpixel((x, y), tuple(pixel))
                data_index += 1
            else:
                break
        if data_index >= message_length:
            break
    
    # Save the encoded image
    encoded_image.save(output_path)
    print("Message encoded successfully!")

# Example usage
if __name__ == "__main__":
    # Encode a message
    encode_image("input_image.png", "Hello, this is a secret message!", "output_image.png")