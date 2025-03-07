from PIL import Image

def decode_image(image_path):
    # Load the image
    try:
        image = Image.open(image_path)
        print("Image loaded successfully for decoding.")
    except Exception as e:
        print(f"Error loading image: {e}")
        return
    
    binary_message = ""
    
    # Convert the image to RGB
    image = image.convert("RGB")
    width, height = image.size
    
    # Extract the message from the image
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            # Get the least significant bit of the blue channel
            binary_message += str(pixel[2] & 1)
            # Check for the delimiter
            if binary_message[-16:] == '1111111111111110':
                # Stop if the delimiter is found
                binary_message = binary_message[:-16]  # Remove the delimiter
                break
        else:
            continue
        break
    
    # Convert binary message to string
    secret_message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return secret_message

# Example usage
if __name__ == "__main__":
    # Decode the message from the encoded image
    secret = decode_image("output_image.png")  # Replace with your encoded image path
    if secret:
        print("Decoded message:", secret)
    else:
        print("No message found.")
