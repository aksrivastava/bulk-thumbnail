# Thumbnail Generator

The Thumbnail Generator script is a Python tool that generates thumbnails with text overlay using a provided template image and data from an Excel file.

## Features

- Generates thumbnails with text overlay on a template image.
- Supports customization of text content, font, and position.
- Processes data from an Excel file to generate thumbnails in bulk.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your_username/thumbnail_generator.git
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare the environment:**

    - Place your template image (`template.jpg`) in the project directory.
    - Ensure you have an Excel file (`your_excel_file.xlsx`) containing the data for generating thumbnails.

2. **Update script parameters:**

    - Update the `template_path` variable with the path to your template image.
    - Update the `font_filename` variable with the filename of your desired font (e.g., "Roboto-Black.ttf").
    - Update the `text_position` variable with the desired coordinates for text placement on the thumbnail image.

3. **Run the script:**

    ```sh
    python generate_thumbnail.py
    ```

4. **Generated Thumbnails:**

    Thumbnails will be saved in the `thumbnails` directory within the project folder.

## Configuration

- **Excel Data**: Ensure your Excel file (`your_excel_file.xlsx`) contains the necessary data in column B for generating thumbnails.

- **Font**: Place your desired font file (e.g., "Roboto-Black.ttf") in the project directory or specify the path to the font file in the script.

## Example

Assuming you have an Excel file (`data.xlsx`) with the following data in column B:

| Column B      |
|---------------|
| Example Text 1|
| Example Text 2|
| Example Text 3|
| ...           |

Running the script will generate thumbnails with the specified text overlay for each row of data.

## How to Run

To generate thumbnails with text overlay, simply run the following command in your terminal:

```sh
python bulkthumbnail.py
