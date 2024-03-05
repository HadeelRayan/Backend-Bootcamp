import requests
import numpy
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def main():

    # Fetching the game data
    url = "https://store.steampowered.com/explore/new/"
    response = requests.get(url)

    html_content = response.text
    file_name = "html_content.html"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_content)

    with open('html_content.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    games = soup.find_all("div", class_="tab_item_content")  # returns a list, each element represent a game
    all_tags = []

    for game in games:
        name = game.find('div', class_='tab_item_name').text
        genre = game.find_all('span', class_='top_tag')[0].text
        all_tags.append(genre)
        theme = game.find_all('span', class_='top_tag')[1].text
        print("game name:", name, ",game genre:", genre, ",game theme:", theme)

    # Calculate frequency of tags
    tags_frequency = {}
    for tag in all_tags:
        if tag in tags_frequency:
            tags_frequency[tag] += 1
        else:
            tags_frequency[tag] = 1

    top_tags = sorted(tags_frequency.items(), key=lambda item: item[1], reverse=True)
    top_tags = top_tags[:10]
    keys, values = zip(*top_tags)

    plt.figure(figsize=(15, 5))
    plt.bar(keys, values)
    plt.xlabel('tags')
    plt.ylabel('frequency')
    plt.title('most common tags')
    plt.show()

    user_tag = input("Enter a tag to check its percentage: ").strip()
    total_tags = sum(tags_frequency.values())
    tag_count = tags_frequency.get(user_tag, 0)

    if total_tags > 0:
        tag_percentage = (tag_count / total_tags) * 100
        print(f"The genre '{user_tag}' appears in {tag_percentage:.2f}% of the games.")
    else:
        print("No genres found in the games list.")


if __name__ == "__main__":
    main()
