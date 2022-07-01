from _csv import writer

import requests
from bs4 import BeautifulSoup


class scrapin:
    URL = "https://pib.gov.in/PressReleaseIframePage.aspx?PRID=1781673"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    table_elements = soup.find_all("table", class_="Table")

    with open('malnutrition.csv', 'w', encoding='utf8') as f:
        thewriter = writer(f)
        header = ['S. No', 'State', 'Stunted 16', 'Stunted 21',  'Wasting 16', 'Wasting 21', 'Underweight 16', 'Underweight 21', 'Women Under Normal BMI 16', 'Women Under Normal BMI 21'];
        thewriter.writerow(header)

        row_elements = table_elements[1].find_all("tr")
        for row_element in row_elements[2:]:
            cell_elements = row_element.find_all('td')
            cells = []
            for cell_element in cell_elements:
                cells.append(cell_element.text.strip())
            thewriter.writerow(cells)