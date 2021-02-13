#!/bin/sh

# Attempting to dowload the chargemasters from the Martin Health hospital of the cleveland clinic
# with the python requests library or pythons wget package fails with an ssl error.
# Passing very=False to requests.get() doens't work and the python vesion of wget doens't allow
# for the --no-check-certificate option. Long term plan will be to consolidate all downlaods into
# python, but this will work for now.

# Page url where these document links are found:

# martin_url="https://www.martinhealth.org/comprehensive-hospital-charges")

url1=https://www.martinhealth.org/stuff/contentmgr/files/1/254f4f6551747746f33ceaf7bafba80e/misc/price_transparency___payor__a.xlsx
url2=https://www.martinhealth.org/stuff/contentmgr/files/1/254f4f6551747746f33ceaf7bafba80e/misc/price_transparency___payor__b.xlsx
url3=https://www.martinhealth.org/stuff/contentmgr/files/1/254f4f6551747746f33ceaf7bafba80e/misc/price_transparency___payor__c_thru_e.xlsx
url4=https://www.martinhealth.org/stuff/contentmgr/files/1/254f4f6551747746f33ceaf7bafba80e/misc/price_transparency___payor__f_thru_l.xlsx
url5=https://www.martinhealth.org/stuff/contentmgr/files/1/254f4f6551747746f33ceaf7bafba80e/misc/price_transparency___payor__m_thru_o.xlsx
url6=https://www.martinhealth.org/stuff/contentmgr/files/1/254f4f6551747746f33ceaf7bafba80e/misc/price_transparency___payor__p_thru_s.xlsx
url7=https://www.martinhealth.org/stuff/contentmgr/files/1/254f4f6551747746f33ceaf7bafba80e/misc/price_transparency___payor__t_thru_z.xlsx

for url in $url1 $url2 $url3 $url4 $url5 $url6 $url7
do
    wget $url --no-check-certificate --directory-prefix=data
done
