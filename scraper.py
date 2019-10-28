from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://finance.yahoo.com/screener/predefined/growth_technology_stocks?count=50&offset=0'

# opens up connection and grabs page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")


#grabs all stocks
containers_A = page_soup.findAll("tr", {"class":"simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white)"})
containers_B = page_soup.findAll("tr", {"class":"simpTblRow Bgc($extraLightBlue):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc($altRowColor)"})

filename = "techgrowth.csv"
f = open(filename, "w")

headers = "Company, ticker, price, price-change, % Change, Volume, Avg Vol (3 Months), Market Cap, PE Ratio (TTM)\n"

f.write(headers)

for container in containers_A:

	company = container.td.a["title"]

	ticker = container.td.a.text

	price_container =  container.findAll("td",{"aria-label":"Price (Intraday)"})
	price = price_container[0].text

	change_container = container.findAll("td",{"aria-label":"Change"})
	change = change_container[0].text

	percent_change_container = container.findAll("td",{"aria-label":"% Change"})
	percent_change = percent_change_container[0].text

	volume_container = container.findAll("td",{"aria-label":"Volume"})
	volume = volume_container[0].text

	vol_three_months_container = container.findAll("td",{"aria-label":"Avg Vol (3 month)"})
	vol_three_months = vol_three_months_container[0].text

	cap_container = container.findAll("td",{"aria-label":"Market Cap"})
	cap = cap_container[0].text

	PE_container = container.findAll("td",{"aria-label":"PE Ratio (TTM)"})
	PE = PE_container[0].text

	f.write(company.replace(",", "").replace(".","") + "," + ticker + "," + price.replace(",", "")+ "," + change + ","
		+ percent_change + "," + volume.replace(",", "") + "," + vol_three_months.replace(",", "") + "," + cap
		+ "," + PE + "\n")

	print("company:",company)
	print("ticker:",ticker)
	print("price:", price)
	print("price change:",change)
	print("% change:", percent_change)
	print("volume:"volume)
	print("Avg 3 Month Volume:",vol_three_months)
	print("Market Cap:",cap)
	print("PE Ratio:",PE)
	print("\n")


for container in containers_B:

	company = container.td.a["title"]

	ticker = container.td.a.text

	price_container =  container.findAll("td",{"aria-label":"Price (Intraday)"})
	price = price_container[0].text

	change_container = container.findAll("td",{"aria-label":"Change"})
	change = change_container[0].text

	percent_change_container = container.findAll("td",{"aria-label":"% Change"})
	percent_change = percent_change_container[0].text

	volume_container = container.findAll("td",{"aria-label":"Volume"})
	volume = volume_container[0].text

	vol_three_months_container = container.findAll("td",{"aria-label":"Avg Vol (3 month)"})
	vol_three_months = vol_three_months_container[0].text

	cap_container = container.findAll("td",{"aria-label":"Market Cap"})
	cap = cap_container[0].text

	PE_container = container.findAll("td",{"aria-label":"PE Ratio (TTM)"})
	PE = PE_container[0].text

	f.write(company.replace(",", "").replace(".","") + "," + ticker + "," + price.replace(",", "")+ "," + change + ","
		+ percent_change + "," + volume.replace(",", "") + "," + vol_three_months.replace(",", "") + "," + cap
		+ "," + PE + "\n")

	print("company:",company)
	print("ticker:",ticker)
	print("price:", price)
	print("price change:",change)
	print("% change:", percent_change)
	print("volume:"volume)
	print("Avg 3 Month Volume:",vol_three_months)
	print("Market Cap:",cap)
	print("PE Ratio:",PE)
	print("\n")

f.close()
