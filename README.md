# NLP and Automation with BERT and Selenium

This repository contains a Python script that demonstrates the use of the BERT language model for Natural Language Processing (NLP) and Selenium for web automation. The script interprets user commands, extracts instructions, and automates interactions with a specified website.

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/yourusername/bert-selenium-nlp.git
   cd bert-selenium-nlp
   ```
Install the required packages using pip:
   ```sh 
   pip install transformers selenium torch
   ```

   Download the appropriate version of chromedriver.exe from the official website and place it in the repository directory.
   
   Kindly change the path here:
   ```
   driver = webdriver.Chrome(executable_path='path-to chrome-driver')
   ```
   Run the Python script:

   ```sh
   python interpret_and_automate.py

   ```

  Enter the test case when prompted. For example:

- Enter the test case: 
  Launch 'www.google.com' input Iron Man click Google search

The script will interpret the command using BERT, extract instructions, and automate interactions with the specified website using Selenium.

## Features
 - Interprets user commands using the BERT language model.
 - Extracts commands and website information from the interpreted output.
 - Automates interactions with the specified website using Selenium.
 - Implements error handling and graceful browser closure.

 ## Requirements
 - Python 3.7+
 - transformers library from Hugging Face (for BERT model)
 - selenium library (for web automation)

 ## License
 This project is licensed under the MIT License.
