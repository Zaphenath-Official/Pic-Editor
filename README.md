# PicEditor

A simple and elegant desktop image editor built with PyQt5 and Python, allowing users to apply various artistic filters and transformations to their photos.

<img width="599" height="628" alt="Screenshot 2025-08-17 193902" src="https://github.com/user-attachments/assets/ac169f09-8449-4a71-8ae8-87cbf2c77af8" />


## Features

  * **Load Images:** Easily load and display images from any local directory.
  * **Image Filters:** Apply a variety of built-in filters with a single click:
      * Grayscale
      * Blur
      * Sharpness, Contrast, and Brightness adjustments.
  * **Image Transformations:** Rotate images 90 degrees left or right.
  * **Custom Fonts:** Utilizes custom Google Fonts (`Genos`, `Zain`, `Pacifico`) for a unique and stylish look.
  * **Custom Save:** Save edited images to a user-specified directory with a custom filename.
  * **Modern UI:** A clean and minimalist user interface with a glassmorphism design.

## Prerequisites

To run this application, you need to have the following installed on your system:

  * **Python 3.x**
  * **PyQt5:** The framework used for the GUI.
  * **Pillow (PIL):** The library used for image manipulation.

## Installation

1.  **Clone the repository:**

    ```sh
    git clone [Your Repository URL]
    cd [Your Project Folder]
    ```

2.  **Install dependencies:**
    Use `pip` to install the required Python libraries.

    ```sh
    pip install PyQt5 pillow
    ```

3.  **Download Font and Image Assets:**
    Ensure your project directory is structured as follows. You need to download the specified `.ttf` font files from [Google Fonts](https://fonts.google.com/) and place them in a `fonts` directory.

    ```
    PicEditor/
    ├── main.py
    ├── fonts/
    │   ├── Genos-VariableFont_wght.ttf
    │   ├── Pacifico-Regular.ttf
    │   └── Zain-Regular.ttf
    └── images/
        ├── default_image.png
        ├── dir.png
        ├── save.png
        ├── folder.png
        ├── left.png
        ├── right.png
        ├── blur.png
        ├── brightness.png
        ├── sharpness.png
        ├── contrast.png
        └── grayscale.png
    ```

## Usage

1.  **Run the application:**
    Open your terminal or command prompt, navigate to the project directory, and run the main script.

    ```sh
    python main.py
    ```

2.  **Select a Directory:**
    Click the "Select Directory" button to choose the folder containing your images. The application will then list all supported image files in that folder.

3.  **Edit an Image:**

      * Click on an image from the list to display it.
      * Use the buttons at the bottom of the window to apply filters and transformations.

4.  **Save the Edited Image:**

      * Click the "Save Image" button.
      * A dialog box will pop up, asking you to enter a filename for your edited image.
      * Enter a name and click OK. The image will be saved to the `Edited_Images` subfolder within your selected directory.

## Project Structure

```
PicEditor/
├── main.py                  # The main application script
├── fonts/                   # Directory for custom font files
│   ├── ...
└── images/                  # Directory for all icon and default image assets
    └── ...
```

## Contributing

Feel free to fork the repository and contribute to the project. You can add more filters, improve the UI, or fix bugs.
