import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

mymail = "mailme.anonymous.1@gmail.com"
pasd = "mailme1997"
mymail2 = "aravindvasvav@gmail.com"
cost = 200000

url = "https://www.ajio.com/teamspirit-embroidered-hoodie-with-kangaroo-pockets/p/441112315006"
hdrs = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
    'Accept-Language': "en-US,en;q=0.9"
}

rsp = requests.get(url=url, headers=hdrs)
# print(rsp.content)
soup = BeautifulSoup(rsp.content, "lxml")
print(soup.prettify())

# pr = soup.find(id="priceblock_ourprice").get_text()
# pr_no = pr.split("₹")[1]
# pr_no2 = float(pr_no.replace(',', ''))
# tit = soup.find(id="productTitle").get_text().strip()
# print(tit)
# print(pr, pr_no, pr_no2)
#
# if pr_no2 < cost :
#     msg2 = f"{tit} - is now :{pr}"
#     with smtplib.SMTP("smtp.gmail.com:587") as conct:
#         conct.ehlo()
#         conct.starttls()
#         conct.login(user=mymail, password=pasd)
#         conct.sendmail(from_addr=mymail,
#                        to_addrs=mymail2,
#                        msg=f"Subject:Amazon Price Alert!!\n\n{msg2}\n{url}")