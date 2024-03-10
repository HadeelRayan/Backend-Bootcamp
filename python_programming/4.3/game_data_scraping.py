import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


class SteamScraper:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        response = requests.get(self.url)
        return response.text

    @staticmethod
    def save_html(self, html_content, file_name="html_content.html"):
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html_content)

    @staticmethod
    def read_html(self, file_name="html_content.html"):
        with open(file_name, "r", encoding="utf-8") as file:
            return file.read()


class HTMLParser:
    def __init__(self, html_content):
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def extract_game_details(self):
        games = self.soup.find_all("div", class_="tab_item_content")
        game_details = []
        for game in games:
            name = game.find('div', class_='tab_item_name').text
            genre = game.find_all('span', class_='top_tag')[0].text.strip(', ')
            theme = game.find_all('span', class_='top_tag')[1].text.strip(', ')
            game_details.append((name, genre, theme))
        return game_details


class TagFrequencyAnalyzer:
    def __init__(self, game_details):
        self.game_details = game_details

    def calculate_tag_frequency(self):
        tags_frequency = {}
        for _, genre, _ in self.game_details:
            tags_frequency[genre] = tags_frequency.get(genre, 0) + 1
        return tags_frequency


class DataVisualizer:
    @staticmethod
    def plot_tag_frequency(tags_frequency):
        top_tags = sorted(tags_frequency.items(), key=lambda item: item[1], reverse=True)[:10]
        keys, values = zip(*top_tags)

        plt.figure(figsize=(15, 5))
        plt.bar(keys, values)
        plt.xlabel('Tags')
        plt.ylabel('Frequency')
        plt.title('Most Common Tags')
        plt.show()


class UserInteraction:
    @staticmethod
    def query_tag_percentage(tags_frequency):
        user_tag = input("Enter a tag to check its percentage: ").strip()
        total_tags = sum(tags_frequency.values())
        tag_count = tags_frequency.get(user_tag, 0)
        if total_tags > 0:
            tag_percentage = (tag_count / total_tags) * 100
            print(f"The genre '{user_tag}' appears in {tag_percentage:.2f}% of the games.")
        else:
            print("No genres found in the games list.")


def main():

    url = "https://store.steampowered.com/explore/new/"
    stream = SteamScraper(url)
    html_content = stream.fetch_html()
    stream.save_html(html_content, file_name="html_content.html")
    html_content = stream.read_html(file_name="html_content.html")

    soup = HTMLParser(html_content)
    game_details = soup.extract_game_details()
    for game_detail in game_details:
        print("game name:", game_detail[0], ",game genre:", game_detail[1], ",game theme:", game_detail[2])

    tags_analyzer = TagFrequencyAnalyzer(game_details)
    tags_frequency = tags_analyzer.calculate_tag_frequency()

    DataVisualizer.plot_tag_frequency(tags_frequency)
    UserInteraction.query_tag_percentage(tags_frequency)


if __name__ == "__main__":
    main()
