# Script to grab all hospital cost info from the Cleveland Clinic Family
# of Hospitals, 15 total.

import requests
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import time



def get_links(url="https://my.clevelandclinic.org/patients/billing-finance/comprehensive-hospital-charges"):
    """ Get links to all Cleveland Clinic chargmaster docs.
    """
    # Grab html
    soup = BeautifulSoup(requests.get(url).text, "html5lib")

    # TODO Martin hospital is throwing an ssl error on request.get. Fix it. For now, grab links from the page directly.

    # martin_url="https://www.martinhealth.org/comprehensive-hospital-charges")

    # Grab the list of docs by the container id

    # TODO Watch this id for changes!
    link_html = soup.find(id='101307de-b1e1-4693-9139-5fc9fec33baf').children


    # Create dict of Hospital name, file url. The hospital names are present in the URLS, but I'd rather
    # pull them out now than parse the urls later, as there are some inconsistencies.

    link_dict ={x.text.lower().replace(' ', '_'): x.attrs['href']
            for x in link_html if type(x) != NavigableString}


    # Grab the url prefix from the clinic url to concat to each relative url

    prefix = url.split('/patients')[0]

    # Add url prefix to the relative urls only

    for k, v in link_dict.items():
        if not v.startswith('https'):
            link_dict[k] = ''.join([prefix, v])

    return link_dict




def download_data(link_dict):
    """ Downloads and writes files to the data directory.
    """

    for k, v in link_dict.items():
        # Martin Health requires different download logic.
        if 'martin' in k:
            continue
        tme = time.strftime('%Y-%m-%d-%H%M')
        filename = Path.cwd() / 'data' / (''.join([k,  '_', tme, '.xlsx']))
        r = requests.get(v)

        with open(filename, 'wb') as csv_file:
            csv_file.write(r.content)

    return None


def main():
    link_dict = get_links()
    download_data(link_dict)

    return get_links()


if __name__ == '__main__':
    link_dict = main()
