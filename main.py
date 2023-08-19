from PIL import Image
import os


# Encode an Image as JPEG
def encode_image(input_image_path, output_jpeg_path):
    # Open the input image
    img = Image.open(input_image_path)

    # Get the size of the original image
    original_size = os.path.getsize(input_image_path)

    # Step 1: Apply the Discrete Cosine Transform (DCT)
    # (DCT is applied internally by Pillow when saving as JPEG)

    # Step 2: Quantization
    # (Quantization is applied internally by Pillow when saving as JPEG)

    # Save the image as JPEG (Huffman coding is applied internally)
    img.save(output_jpeg_path, format="JPEG")

    # Get the size of the encoded JPEG image
    encoded_size = os.path.getsize(output_jpeg_path)

    # Print image sizes
    print(f"Original Image Size: {original_size} bytes")
    print(f"Encoded JPEG Image Size: {encoded_size} bytes")
    print(f"Image encoded as JPEG and saved to {output_jpeg_path}")


# Decode a JPEG Image
def decode_image(jpeg_path):
    # Open the JPEG image
    img = Image.open(jpeg_path)

    # Display the image (inverse DCT, dequantization, and Huffman decoding are applied internally)
    img.show()


if __name__ == "__main__":
    # Encode an image to JPEG
    input_image_path = "test1.jpg"  # Replace with the path to your input image
    output_jpeg_path = "test1_output.jpg"  # Replace with the desired output path and filename
    encode_image(input_image_path, output_jpeg_path)

    # Decode a JPEG image
    decoded_image_path = "test1_output.jpg"  # Replace with the path to the JPEG image you want to decode
    decode_image(decoded_image_path)
