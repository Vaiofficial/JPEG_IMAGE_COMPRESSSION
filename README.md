# JPEG Image Compression Example

This GitHub repository provides a simple example of JPEG image compression using Python and the Pillow (PIL) library. JPEG (Joint Photographic Experts Group) is a widely used image compression technique that allows for efficient storage and transmission of images while maintaining reasonable image quality.

## Table of Contents

- [Demo](#demo)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Demo

No live demo available for this code example. You can follow the instructions below to run the code on your local machine.

## Getting Started

Follow these steps to set up and run the JPEG compression code on your local machine.

### Prerequisites

- Python 3.x
- Pillow (PIL) library (`pip install pillow`)

### Installation

1. Clone this repository to your local machine:

   ``` shell
   git clone https://github.com/your-username/jpeg-compression.git

   #Note

   1. Change your current directory to the project folder:
   cd jpeg-compression

   #Usage
   1. Replace "input_image.jpg" in the encode_image function with the path to your input image that you want to compress as a JPEG.

   2.Replace "output_image.jpg" in the encode_image function with the desired output path and filename for the compressed JPEG image.

   3. Run the code to encode the image as a JPEG:
   python jpeg_compression.py

   4. The code will calculate and print the size of the original image and the size of the encoded JPEG image to the console.

   5. You can then decode the JPEG image using the provided code:
   python jpeg_compression.py

###CodeExplanation

The code demonstrates the encoding and decoding of an image as a JPEG. It involves the following key processes:

Encoding as JPEG: The code uses the Pillow (PIL) library to open an input image and encode it as a JPEG image. This process involves the application of the Discrete Cosine Transform (DCT), quantization, and Huffman coding, which are fundamental components of JPEG compression.

Decoding JPEG: The code also shows how to decode a JPEG image using Pillow, displaying the decoded image.


