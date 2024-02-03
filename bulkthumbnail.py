import cv2
import os
from openpyxl import load_workbook
from PIL import Image, ImageDraw, ImageFont

def generate_thumbnail(template_path, text, filename, text_position, font_path):
    # Open the template image using PIL
    template = Image.open(template_path)
    
    # Convert image to RGB mode
    template = template.convert('RGB')

    # Create a drawing context
    draw = ImageDraw.Draw(template)

    # Load the font
    font = ImageFont.truetype(font_path, size=50)  # Adjust the font size as needed
    
    # Draw text on the template image
    draw.text(text_position, text, font=font, fill='black')  # Set text color to black
    
    # Create thumbnails directory if it doesn't exist
    os.makedirs("thumbnails", exist_ok=True)
    
    # Save the thumbnail image
    thumbnail_path = os.path.join("thumbnails", f"{filename}.jpg")
    template.save(thumbnail_path)
    
    print(f"Thumbnail saved as: {thumbnail_path}")

# Load the Excel file
workbook = load_workbook('your_excel_file.xlsx')
sheet = workbook.active

# Specify the font file name (located in the same directory as your script)
font_filename = "Roboto-Black.ttf"
font_path = os.path.join(os.path.dirname(__file__), font_filename)

# Iterate over each cell in column B
for cell in sheet['B']:
    data = str(cell.value)  # Convert data to string
    filename = data.replace(" ", "_")  # Replace spaces with underscores for filename
    template_path = "template.jpg"  # Provide the path to your template image
    text = data  # The text you want to paste onto the thumbnail
    text_position = (143,461)  # Coordinates of the top-left corner where you want to paste the text
    
    generate_thumbnail(template_path, text, filename, text_position, font_path)
