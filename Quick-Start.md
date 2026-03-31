# Quick Start Guide

Welcome to the Book repository quick start guide.

## Working with Nano Banana Prompts

The repository contains extensive lists of "Nano Banana" prompts which can be executed efficiently in parallel using our custom script found in the `src/` directory.

### Local Nano Banana Image Generation Setup

To set up your local environment and begin processing these prompts to generate images, follow the steps below:

1. **Prerequisites**
   - Ensure Python 3.8 or higher is installed.
   - Install required dependencies by running:
     ```bash
     pip install pyyaml
     ```

2. **Quick Single Generation**
   You can easily invoke the API passing a single specific prompt through via inline options:
   ```bash
   cd src/
   python nano_banana_api.py --prompt "Do unto others"
   ```

3. **Generating Lists of Images in Parallel**
   You can point the automation script directly at our markdown files (using the `::` delimiter) or YAML configuration templates located in the `inputs/` folder. This greatly speeds up processing by running things in parallel.

   ```bash
   # From a double-colon delimited markdown file:
   ./src/nano_banana.sh --file "Nano-Banana-Prompts-CP.md" --format "delimited" --workers 10

   # Using a standard YAML format file from the inputs directory:
   ./src/nano_banana.sh --file "inputs/nano-prompts.yml" --format "yaml"

Outputs will, by default, be stored locally in the `images/` directory at the project root. The script dynamically names the generated image outputs based on your initial prompt input string.

> For more detailed script information and inner workings, be sure to check out the deep dive inside [src/README.md](src/README.md).
