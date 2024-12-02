import requests
import json

# Define the API endpoint and headers
url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

# Input and output file names
input_file = "french_revolution.txt"
output_file = "summary_french.txt"

# Read the input text from input.txt
try:
    with open(input_file, "r", encoding="utf-8") as file:
        input_text = file.read()
except FileNotFoundError:
    print(f"Error: File {input_file} not found.")
    exit()

# Create a prompt to instruct the model
prompt = (
    "Please summarize the following text in **French** using simple words and short sentences. "
    "The summary should be clear and easy for a 5th grader to understand:\n\n"
    f"{input_text}\n\n"
    "The summary should be very basic, avoiding complicated words or ideas. Keep it easy to read."
)

# Define the data payload
data = {
    "model": "llama3.2",
    "prompt": prompt,
    "stream": False
}

# Send the request to the API
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        # Parse the response
        response_data = json.loads(response.text)
        summary = response_data.get("response", "No summary generated.")
        
        # Save the summary to output_file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(summary)
        
        print(f"The summary has been saved to {output_file}.")
    else:
        print(f"Error: {response.status_code}, {response.text}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while connecting to the API: {e}")
