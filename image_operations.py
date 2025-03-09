def encrypt_image(image_path, key):
    # Open the image
    input_image = open(image_path, 'rb')
    image = input_image.read()
    input_image.close()

    # Convert image to bytearray
    image = bytearray(image)
   
    # Perform the XOR operation with the key
    for index, values in enumerate(image):
        image[index] = values ^ key

    # Write the encrypted image to a new file
    input_image = open(image_path, 'wb')
    input_image.write(image)
    input_image.close()

    print("Image encrypted successfully")


def decrypt_image(image_path, key):
    # Open the image
    input_image = open(image_path, 'rb')
    image = input_image.read()
    input_image.close()

    # Convert image to bytearray
    image = bytearray(image)
   
    # Perform the XOR operation with the key
    for index, values in enumerate(image):
        image[index] = values ^ key

    # Write the encrypted image to a new file
    input_image = open(image_path, 'wb')
    input_image.write(image)
    input_image.close()

    print("Image decrypted successfully")
    

image_path  = input("Please enter the image path: ")
key = int(input("Please enter the encryption key: "))
task_ordered = int(input("Please chose the task: 1 for encryption, 2 for decryption: "))

if task_ordered == 1:
    encrypt_image(image_path, key)
elif task_ordered == 2:
    decrypt_image(image_path, key)



