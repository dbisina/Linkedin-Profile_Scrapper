# LinkedIn Profile Scraper

## Overview

The LinkedIn Profile Scraper is a Python script designed to extract contact information from LinkedIn profiles. This tool is useful for gathering data on professionals from specified companies, including their names, job titles, email addresses, and phone numbers.

## Features

- Automated login to LinkedIn using Selenium
- Profile data extraction using BeautifulSoup
- Handles multiple profiles from specified companies
- Reads profile URLs from a text file
- Stores extracted data in a CSV file

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6+
- LinkedIn account with login credentials
- Web driver for Selenium (e.g., ChromeDriver)
- A text file (`profile_urls.txt`) containing the LinkedIn profile URLs

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/linkedin-profile-scraper.git
   cd linkedin-profile-scraper
   ```

2. **Install the required Python packages**:

   ```bash
   pip install selenium beautifulsoup4 pandas
   ```

3. **Download the appropriate web driver**:
   - For Chrome: [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
   - Ensure the web driver is placed in your PATH or specify its location in the script.

## Usage

1. **Set your LinkedIn credentials**:
   Open the script and replace `'your_email'` and `'your_password'` with your actual LinkedIn login credentials.

2. **Create the profile URLs text file**:
   Create a file named `profile_urls.txt` and add the LinkedIn profile URLs, one per line.

3. **Run the script**:

   ```bash
   python linkedin_scraper.py
   ```

4. **View the results**:
   The scraped data will be saved to a CSV file named `linkedin_contacts.csv`.

## Script Breakdown

### Authentication

The script uses Selenium to navigate to LinkedIn's login page, input the credentials, and log in.

### Scraping Function

The `scrape_profile` function:
- Navigates to each LinkedIn profile URL.
- Extracts the name, job title, email address, and phone number.
- Handles scenarios where contact info may not be publicly visible.

### Data Handling

The script stores all extracted data in a pandas DataFrame and saves it to a CSV file.

### Reading Profile URLs

The script reads the LinkedIn profile URLs from a text file (`profile_urls.txt`), ensuring flexibility and ease of use.

## Important Notes

- **Compliance**: Scraping LinkedIn data might violate LinkedIn’s terms of service. Use this script responsibly and ensure you have permission to scrape the data.
- **Rate Limiting**: To avoid being blocked by LinkedIn, include delays between requests and consider using proxies.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License.

---

This README provides a comprehensive guide to using the LinkedIn Profile Scraper, ensuring that users can easily understand and utilize the script for their purposes.