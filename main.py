import requests
from bs4 import BeautifulSoup
import logging
import csv
from lib.Color import *

# Configure logging
logging.basicConfig(filename='match_details.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Define a function to write match details to a CSV file
def write_match_details_to_csv(filename, match_content):
    try:
        with open(filename, 'w', newline='') as output_file:
            fieldnames = match_content[0].keys()
            dict_writer = csv.DictWriter(output_file, fieldnames=fieldnames)
            dict_writer.writeheader()
            dict_writer.writerows(match_content)

        logging.info(f"Match details saved to '{filename}'")
        print(f"Match details saved to '{filename}'")

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        print(f"Error: {str(e)}")


# Define a function to print a banner
def print_banner():
    banner_text = [
        "     __                                ",
        "    / _\\ ___ _ __ __ _ _ __   ___ _ __ ",
        "    \\ \\ / __| '__/ _` | '_ \\ / _ \\ '__|",
        "    _\\ \\ (__| | | (_| | |_) |  __/ |   ",
        "    \\__/\\___|_|  \\__,_| .__/ \\___|_|   ",
        "                      |_|              ",
    ]

    # Print the banner
    for line in banner_text:
        print(Color.banner+line+Color.Reset)

# Define a function to get the URL
def get_url():
    try:
        Date = input(Color.fore.YELLOW+"[*] Input Date Format mm/dd/yyyy: "+Color.Reset)
        url = f"https://www.yallakora.com/match-center?date={Date}"

        if not url:
            print("URL cannot be empty. Please try again.")
            return None

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Successfully retrieved the page")
            return response
        elif response.status_code == 401:
            logging.error("Error: Unauthorized")
            print("Unauthorized!")
        else:
            logging.error("Error: Failed to retrieve the page")
            print("Failed to retrieve the page")

    except requests.exceptions.RequestException as e:
        logging.error(f"Error: Failed to connect to the server: {e}")
        print(f"Failed to connect to the server: {e}")


# Define a function to scrape match details
def scrape_match_details(response):
    try:
        soup = BeautifulSoup(response.content, 'lxml')
        match_cards = soup.find_all('li', class_='item')
        print(len(match_cards))
        match_details = []

        for match_card in match_cards:
            channel_elem = match_card.find('div', class_='channel icon-channel')
            channel = channel_elem.text.strip() if channel_elem else "N/A"

            date_elem = match_card.find('div', class_='date')
            date = date_elem.text.strip() if date_elem else "N/A"

            status_elem = match_card.find('div', class_='matchStatus')
            status = status_elem.text.strip() if status_elem else "N/A"

            team_a_elem = match_card.find('div', class_='teams teamA')
            team_a = team_a_elem.find('p').text.strip() if team_a_elem else "N/A"

            team_b_elem = match_card.find('div', class_='teams teamB')
            team_b = team_b_elem.find('p').text.strip() if team_b_elem else "N/A"

            result_elem = match_card.find_all('span', class_='score')

            score_a = result_elem[0].text.strip() if result_elem else "N/A"
            score_b = result_elem[1].text.strip() if result_elem else "N/A"

            time_elem = match_card.find('span', class_='time') if result_elem else None
            time = time_elem.text.strip() if time_elem else "N/A"

            if team_a_elem:
                match_details.append({
                    'Team A': team_a,
                    'Team B': team_b,
                    'Time': time,
                    'Result': f"{score_a} - {score_b}",
                    'State': status,
                    'Date': date,
                    'Channel': channel,
                })

        return match_details

    except Exception as e:
        print(f"An error occurred while parsing the page: {e}")


if __name__ == "__main__":
    print("\nStarting Tools...")
    print("\n")
    print_banner()
    response = get_url()

    if response:
        match_details = scrape_match_details(response)
        write_match_details_to_csv('matches-details.csv', match_details)
