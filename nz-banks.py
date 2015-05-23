#!/usr/bin/python

import requests

sites = [
  ('ASB', 'https://online.asb.co.nz/auth/'),
  ('ANZ', 'https://secure.anz.co.nz/IBCS/pgLogin'),
  ('ANZ (Direct Online)', 'https://www.anzdirect.co.nz/online/EnterANZDirect.do'),
  ('BankDirect', 'https://vault.bankdirect.co.nz/default.asp'),
  ('BNZ', 'https://www.bnz.co.nz/ib/app/login'),
  ('HSBC', 'https://www.hsbc.co.nz/1/2/HUB_IDV2/IDV_EPP?__IWCountry=&__IWLang=en&__Destination=HUB_IDV_CUSTOMER_MIGRATION&__menuType=__REGISTRATION&__registrationType=PIB-Registration'),
  ('Kiwibank', 'https://www.ib.kiwibank.co.nz/'),
  ('Rabobank', 'https://secure1.rabodirect.co.nz/exp/authenticationDGPEN.jsp'),
  ('SBS', 'https://secure.sbsbank.co.nz/personal/'),
  ('SBS (Community Banking)', 'https://ibank.sbs.net.nz/ui/inetbankindex.aspx'),
  ('TSB', 'https://homebank.tsbbank.co.nz/online/'),
  ('Westpac', 'https://sec.westpac.co.nz/IOLB/Login.jsp'),
]

for site in sites:
  r = requests.get(site[1], verify=False,  # Disabling cert checking, do not do this at home!
                   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'})
  if 'strict-transport-security' in r.headers:
    print site[0] + ': yes! [' + r.headers['strict-transport-security'] + ']'
  else:
    print site[0] + ': no :('
