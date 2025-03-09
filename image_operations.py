def process_image(image_path, key, operation):
    """Encrypts or decrypts an image using XOR operation with the provided key."""
    with open(image_path, 'rb') as input_image:
        image = bytearray(input_image.read())

    # Perform the XOR operation with the key
    for index in range(len(image)):
        image[index] ^= key

    # Write the processed image to a new file
    with open(image_path, 'wb') as output_image:
        output_image.write(image)

    if operation == 'encrypt':
        print("Image encrypted successfully")
    elif operation == 'decrypt':
        print("Image decrypted successfully")


image_path = input("Please enter the image path: ")
key = int(input("Please enter the encryption key: "))
task_ordered = int(input("Please choose the task: 1 for encryption, 2 for decryption: "))

if task_ordered == 1:
    process_image(image_path, key, 'encrypt')
elif task_ordered == 2:
    process_image(image_path, key, 'decrypt')
