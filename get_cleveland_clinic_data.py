# Script to grab all hospital cost info from the Cleveland Clinic Family
# of Hospitals, 15 total.

import requests
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import NavigableString

CLINIC_URL = "https://my.clevelandclinic.org/patients/billing-finance/comprehensive-hospital-charges"

def main():

    # Grab html
    soup = BeautifulSoup(requests.get(CLINIC_URL).text, "html5lib")

    # Grab the list of docs by the container id

    # TODO Watch this id for changes!
    link_html = soup.find(id='101307de-b1e1-4693-9139-5fc9fec33baf').children

    # Grab the url prefix from the clinic url to concat to each relative url
    prefix = CLINIC_URL.split('/patients')[0]

    # Create tuples of Hospital name, file url. The hospital names are present in the URLS, but I'd rather
    # pull them out now than parse the urls later, as there are some inconsistencies.
    link_tuples =[(x.text, x.attrs['href'])
            for x in link_html if type(x) != NavigableString]

    # TODO prefix needs to be added to the correct urls prior to return
    return link_tuples


if __name__ == '__main__':
    link_tuples = main()
