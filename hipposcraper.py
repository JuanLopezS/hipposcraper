#!/usr/bin/env python2
"""Main entry point for hipposcrape

To-do:
    - fix low_scraper to scrape without header:
        test link: https://intranet.hbtn.io/projects/213

    - fix set_permissions to catch no files
        current error: chmod: cannot access '*': No such file or directory
        does not seem to be an error
"""
from scrapers import *


def get_args():
    """Method that grabs argv

    Returns:
        link (str): argv[1]
    """
    arg = sys.argv[1:]
    count = len(arg)

    if count > 1:
        print("[ERROR] Too many arguments (must be one)")
        sys.exit()
    elif count == 0:
        print("[ERROR] Too few arguments (must be one)")
        sys.exit()

    link = sys.argv[1]
    return link

def set_permissions():
    """Method that sets permissions on files"""
    sys.stdout.write("  -> Setting permissions... ")
    try:
        os.system("chmod u+x *")
        print("done")
    except OSError:
        print("[ERROR] Failed to set permissions")
    
def hipposcrape():
    """hipposcrape

    Entry point for the scraper.
    """

    link = get_args()
    parse_data = BaseParse(link)

    parse_data.get_json()

    soup = parse_data.get_soup()

    print("Creating project:")

    parse_data.find_directory()
    parse_data.create_directory()

    project_type = parse_data.project_type_check()
    if "high" in project_type:
        # Creating scraping objects
        hi_scraper = HighScraper(soup)
        t_scraper = TestFileScraper(soup)

        # Scraping necessary data
        hi_scraper.find_prototypes()
        hi_scraper.find_files()

        # Writing to files with scraped data
        hi_scraper.write_files()

        # Finding and creating test files
        t_scraper.find_test_files()
        t_scraper.write_test_files()

    elif "low" in project_type:
        # Creating scraping objects
        lo_scraper = LowScraper(soup)
        t_scraper = TestFileScraper(soup)

        # Scraping necessary data
        lo_scraper.find_putchar()
        lo_scraper.find_prototypes()
        lo_scraper.find_header()
        lo_scraper.find_files()

        # Writing to files with scraped data
        lo_scraper.write_putchar()
        lo_scraper.write_header()
        lo_scraper.write_files()

        # Finding and creating test files
        t_scraper.find_test_files()
        t_scraper.write_test_files()

    elif "system" in project_type:
        # Creating scraping objects
        sy_scraper = SysScraper(soup)
        t_scraper = TestFileScraper(soup)

        # Scraping necessary data
        sy_scraper.ruby_checker()
        sy_scraper.find_files()

        # Writing to files with scraped data
        sy_scraper.write_files()

    else:
        print("[ERROR]: Could not determine project type")
        sys.exit()

    set_permissions()
    print("Project all set!")

hipposcrape()
