#!/usr/bin/python

import requests

sites = [
  ('ANZ', 'https://www.anz.com/INETBANK/bankmain.asp'),
  ('Bank of China', 'https://ebs.boc.cn/BocnetClient/LoginFrameAbroad.do?_locale=en_US'),
  ('Bank of Melbourne', 'https://ibanking.bankofmelbourne.com.au/ibank/loginPage.action'),
  ('Bankwest', 'https://ibs.bankwest.com.au/BWLogin/rib.aspx'),
  ('Bendigobank', 'https://www.bendigobank.com.au/banking/BBLIBanking/'),
  ('Bank of Queensland', 'https://www.ib.boq.com.au/boqbl'),
  ('Citibank', 'https://www.citibank.com.au/AUGCB/JSO/signon/DisplayUsernameSignon.do'),
  ('Commonwealth Bank', 'https://www.my.commbank.com.au/netbank/Logon/Logon.aspx'),
  ('Heritage Bank', 'https://online.hbs.net.au/hbsv47/ntv471.asp?wci=entry'),
  ('HSBC' , 'https://www.hsbc.com.au/1/2/HUB_IDV2/IDV_EPP?__IWCountry=US&__IWLang=en&__Destination=HUB_IDV_CUSTOMER_MIGRATION&__menuType=__REGISTRATION&__registrationType=PIB-Registration'),
  ('Mebank', 'https://ib.mebank.com.au/ME'),
  ('NAB', 'https://ib.nab.com.au/nabib/index.jsp'),
  ('Rabobank', 'https://secure.rabodirect.com.au/exp/policyenforcer/pages/loginB2CDGPEN.jsf?login'),
  ('St. George', 'https://ibanking.stgeorge.com.au/ibank/loginPage.action'),
  ('Suncorp Bank', 'https://internetbanking.suncorpbank.com.au/'),
  ('Westpac', 'https://online.westpac.com.au/esis/Login/SrvPage'),
]

for site in sites:
  r = requests.get(site[1], verify=False,  # Disabling cert checking, do not do this at home!
                   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'})
  if 'strict-transport-security' in r.headers:
    print site[0] + ': yes! [' + r.headers['strict-transport-security'] + ']'
  else:
    print site[0] + ': no :('
