from PIL import Image

# Define the ASCII characters used to represent pixel intensities
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Resizes the image while maintaining aspect ratio."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """Converts the image to grayscale."""
    return image.convert("L")

def pixel_to_ascii(image):
    """Maps each pixel to an ASCII character based on its intensity."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def image_to_ascii(image_path, new_width=100):
    """Converts the given image to ASCII art."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {e}")
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)
    ascii_str = pixel_to_ascii(image)

    # Format the ASCII string into multiple lines
    ascii_len = len(ascii_str)
    ascii_str_len = new_width
    ascii_img = "\n".join([ascii_str[index:index + ascii_str_len] for index in range(0, ascii_len, ascii_str_len)])

    return ascii_img

def save_ascii_image(ascii_img, output_file="ascii_image.txt"):
    """Saves the ASCII art to a text file."""
    with open(output_file, "w") as f:
        f.write(ascii_img)

# Input image path and output file
image_path = "wp5145715-naruto-desktop-tumblr-wallpapers.jpg"
output_file = "ascii_image.txt"

# Convert image to ASCII art
ascii_img = image_to_ascii(image_path)

# Save the ASCII art to a text file
if ascii_img:
    save_ascii_image(ascii_img, output_file)
    print(f"ASCII art saved to {output_file}")
