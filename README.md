# base64-image-extractor

A Python utility for extracting base64-encoded JPEG images from HTML files, saving them as JPEG files, and updating the HTML to reference these images by their new file paths.

## Getting Started

These instructions will guide you through setting up and running `base64-image-extractor` on your local machine.

### Prerequisites

- Python 3.x
- pip
- virtualenv

### Installation

1. **Clone the Repository**

   Start by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/miguelsm/base64-image-extractor.git
   cd base64-image-extractor
   ```

2. **Set Up a Virtual Environment**

   Create a virtual environment to manage the project's dependencies separately from your global Python environment:

   ```bash
   python3 -m virtualenv venv
   ```

   Activate the virtual environment:

   - **On Windows:**

     ```cmd
     .\venv\Scripts\activate
     ```

   - **On macOS and Linux:**

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**

   Install the project dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

To run `base64-image-extractor`, ensure your virtual environment is activated, then execute the script with the path to your HTML file as an argument. The script will extract base64-encoded JPEG images, save them as files, and update the HTML file to reference these images by their new paths.

```bash
python base64_image_extractor.py path/to/your/file.html
```

The modified HTML will be printed to standard output. If you want to save the modified HTML to a new file, you can redirect the output like so:

```bash
python base64_image_extractor.py path/to/your/file.html > path/to/your/modified_file.html
```

### Deactivating Virtual Environment

Once you are done, you can deactivate the virtual environment:

```bash
deactivate
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
