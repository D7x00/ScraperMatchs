# Match Details Scraper

This Python script (`main.py`) is designed to scrape football match details from the [Yallakora](https://www.yallakora.com) website and save them to a CSV file. It utilizes the `requests` library to fetch the web page, `BeautifulSoup` for web scraping, and `logging` for error handling. Additionally, it uses a custom `Color` library to add color to the console output.

## Usage

1. Clone this repository to your local machine:

```bash
git clone 
```

2. Navigate to the project directory:

```bash
cd match-details-scraper
```

3. Install the required Python libraries if you haven't already:

```bash
pip install -r  requirments.txt
```

4. Run the script:

```bash
python main.py
```

The script will prompt you to enter a date in the format `mm/dd/yyyy`. It will then scrape the match details for that date from the Yallakora website and save them to a CSV file named `matches-details.csv`.

## Script Overview

- `main.py` contains the main script.
- `Color.py` is a custom library for adding color to console output.

## Script Components

- **Logging**: The script configures logging to record any errors in a `match_details.log` file.

- **Functions**:
  - `write_match_details_to_csv(filename, match_content)`: Writes match details to a CSV file.
  - `print_banner()`: Prints a colorful banner in the console.
  - `get_url()`: Prompts the user for a date and retrieves the corresponding Yallakora URL.
  - `scrape_match_details(response)`: Scrapes match details from the Yallakora web page and returns them as a list of dictionaries.

- **Main Execution**:
  - The script starts by printing a banner to the console.
  - It then calls `get_url()` to fetch the web page.
  - If successful, it calls `scrape_match_details(response)` to scrape match details.
  - Finally, it calls `write_match_details_to_csv()` to save the details to a CSV file.

Please note that this script relies on the structure of the Yallakora website. Any changes to the website's structure may break the scraper.

## Dependencies

- [Requests](https://pypi.org/project/requests/): Used to make HTTP requests.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): Used for web scraping.
- [lxml](https://lxml.de/): A library used by Beautiful Soup for parsing HTML.

## Disclaimer

This script is for educational purposes only. Be sure to review and comply with the terms of use of any website you scrape data from. Additionally, consider the website's policies and rate limiting to avoid overloading their servers with requests.