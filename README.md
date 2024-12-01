# Linkedin-Connection-Automation

Here’s a comprehensive README.md file template and description for your LinkedIn Connection Automation repository:

LinkedIn Connection Automation

A Python-based LinkedIn automation script using Selenium to streamline sending personalized connection requests to recruiters, hiring managers, or professional contacts. The tool dynamically navigates LinkedIn search results, scrolls through profiles, and sends requests with customized notes to expand your network efficiently.

Features

	•	Automated Login: Securely logs into your LinkedIn account using Selenium.
	•	Dynamic Scrolling: Automatically scrolls through LinkedIn search results to load new profiles.
	•	Connection Requests: Clicks the “Connect” button for each profile and sends personalized notes.
	•	Customizable Notes: Allows users to define custom messages to include in connection requests.
	•	Error Handling: Handles pop-ups and errors gracefully to ensure smooth execution.
	•	Easy Configuration: Simply update your LinkedIn credentials and note to start.

Prerequisites

	•	Python 3.7 or above
	•	Chrome browser
	•	ChromeDriver compatible with your Chrome version

Installation

	1.	Clone the repository:

git clone https://github.com/YourUsername/LinkedIn-Connection-Automation.git
cd LinkedIn-Connection-Automation


	2.	Install required dependencies:

pip install selenium


	3.	Ensure ChromeDriver is installed and added to your system PATH:

brew install chromedriver  # For macOS users

Configuration

	1.	Open main.py and update the following fields with your LinkedIn credentials and target note:

email = "your_email@example.com"
password = "your_password"
note = """Hi, I came across your profile and found your experience really inspiring.
I’m currently seeking opportunities and would love to connect. Thank you!"""


	2.	Update the LinkedIn search URL to target specific profiles:

driver.get("https://www.linkedin.com/search/results/people/?keywords=intuit")

Usage

	1.	Run the script:

python3 main.py


	2.	The script will:
	•	Log into your LinkedIn account.
	•	Navigate to the specified search results.
	•	Scroll through profiles and send connection requests with the specified note.
	3.	Monitor the terminal for status updates and potential errors.

Notes

	•	Use this tool responsibly to avoid breaching LinkedIn’s terms of service.
	•	Ensure your connection requests remain professional and relevant to your networking goals.

Known Issues

	•	LinkedIn frequently updates its DOM structure, so some XPaths may need updating if the script fails to locate elements.
	•	Automation scripts may trigger CAPTCHA checks; be ready to solve them if prompted.

Future Improvements

	•	Add support for rotating notes for better personalization.
	•	Implement multi-threading to enhance efficiency.
	•	Enable CSV-based input for bulk connection requests.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing

Feel free to fork the repository, make improvements, and submit a pull request. Contributions are always welcome!
