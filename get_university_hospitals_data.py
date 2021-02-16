# Script to grab all hospital cost info from the Univesity Hospitals Family
# of Hospitals, 15 total.

import requests
from subprocess import call
from pathlib import Path
from bs4 import BeautifulSoup
from bs4.element import NavigableString
import time



def get_links(url="https://www.uhhospitals.org/patients-and-visitors/billing-insurance-and-medical-records/cms-medicare-price-transparency-initiative"):
    """ Get links to all University Hospital  chargmaster docs.
    """
    # Grab html
    soup = BeautifulSoup(requests.get(url, verify=False).text, "html5lib")

    # get table rows and skip the header
    rows = soup.findAll("tr")[1:]

    # Create dict of Hospital name, file url.

    def clean_hospital_name(name):
        """ Helper function to  clean up the hospital names'
        """
        name = name.split(",")[0].replace(".", "")
        return '_'.join(name.lower().split())


    link_dict = {clean_hospital_name(row.td.text): row.a.get("href")
            for row in rows if type(row) != NavigableString}

    # Grab the url prefix from the clinic url to concat to each relative url

    prefix = "".join(["https://", url.split("/")[2]])

    # Add url prefix to the relative urls only

    for k, v in link_dict.items():
        if not v.startswith("https"):
            link_dict[k] = "".join([prefix, v])


    return link_dict




def download_data(link_dict):
    """ Downloads and writes files to the data directory.
    """

    for k, v in link_dict.items():
        tme = time.strftime('%Y-%m-%d-%H%M')
        filename = Path.cwd() / 'data' / (''.join([k,  '_', tme, '.xlsx']))
        r = requests.get(v, verify=False)

        with open(filename, 'wb') as excel_file:
            excel_file.write(r.content)

    return None


def main():
    link_dict = get_links()
    download_data(link_dict)

    return get_links()


if __name__ == '__main__':
    link_dict = main()
