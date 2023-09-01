import torch
from transformers import BertForQuestionAnswering, BertTokenizer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def extract_commands(answer):
    # Extract relevant information from the answer
    command_parts = answer.split("input")
    if len(command_parts) < 2:
        raise ValueError("Invalid command format")
    
    website = command_parts[0].strip().strip("'")
    actions = "input" + command_parts[1].strip()
    return website, actions

def perform_actions(driver, actions):
    for action in actions.split():
        if action.lower() == "input":
            input_text = actions.split("input", 1)[1].strip()
            search_box = driver.find_element_by_name("q")
            search_box.clear()
            search_box.send_keys(input_text)
            search_box.send_keys(Keys.RETURN)
        elif action.lower() == "click":
            driver.find_element_by_name("btnK").click()

# Load BERT model and tokenizer
model_name = 'bert-base-uncased'
model = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# User's input sentence
user_input = input("Enter the test case: ")

try:
    # Preprocess input for BERT
    question = "What is the command?"
    context = user_input
    inputs = tokenizer.encode_plus(question, context, return_tensors="pt")

    # Get BERT's predictions
    start_scores, end_scores = model(**inputs)
    start_index = torch.argmax(start_scores)
    end_index = torch.argmax(end_scores)

    # Extract predicted answer span
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_index:end_index+1]))

    # Extract commands from the answer
    website, actions = extract_commands(answer)

    # Initialize Selenium WebDriver
    driver = webdriver.Chrome(executable_path='path_to_chromedriver.exe')

    # Open the website
    driver.get(website)

    # Perform actions using Selenium
    perform_actions(driver, actions)

    # Wait for a while before closing the browser
    time.sleep(5)

except Exception as e:
    print("An error occurred:", str(e))
finally:
    # Close the browser
    driver.quit()
