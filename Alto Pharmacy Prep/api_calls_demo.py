import requests
"""
Remember to
pip3 install requests
"""

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

def post_data(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 201:
        return "Data successfully posted"
    else:
        return f"Error: {response.status_code}"

# Example usage
api_url = "https://api.example.com/data"
get_result = get_data(api_url)
print("GET result:", get_result)

post_data = {"name": "John Doe", "email": "john@example.com"}
post_result = post_data(api_url, post_data)
print("POST result:", post_result)

"""
Setting up local environment:

Install Python (if not already installed)
Open a terminal or command prompt
Navigate to your project directory
Create a virtual environment:

python3 -m venv venv

On macOS/Linux: source myenv/bin/activate

pip3 install requests

Create a new Python file (e.g., api_calls.py) and paste the code from the artifact above
Run your script from the command line:

python3 api_calls_demo.py
"""