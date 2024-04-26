from googlesearch import search

# ASCII art for the tool name
xxxxxxxxxxxxx = """
.__              .__    .___        ____ _____________.____     
|__| ____   _____|__| __| _/____   |    |   \______   \    |    
|  |/    \ /  ___/  |/ __ |/ __ \  |    |   /|       _/    |    
|  |   |  \\___ \|  / /_/ \  ___/  |    |  / |    |   \    |___ 
|__|___|  /____  >__\____ |\___  > |______/  |____|_  /_______ 
"""

print('A Open Source Project Developed by Sajiya')

def search_urls_with_keyword(keyword, site, num_results):
    query = f"inurl:{site} {keyword}"
    urls = search(query, num=num_results, stop=num_results, pause=2)
    return urls

def main():
    print("\033[1m")  # bold text
    print("\033[93m" + xxxxxxxxxxxxx + "\033[0m")  # yellow color for the ASCII art
    print("\033[0m")  # reset text formatting
    
    site = input("Enter the website (e.g., youtube.com): ")
    keyword = input("Enter the keyword to search for in the URL: ")
    num_results = int(input("Enter the number of results to fetch: "))
    
    print("\nSearching...")
    urls = search_urls_with_keyword(keyword, site, num_results)
    
    print("\nURLs found:")
    for url in urls:
        print(url)
    
    print("\n\033[2mA proud open source security project by Sajiya\033[0m")  # dim text for credits

if __name__ == "__main__":
    main()
