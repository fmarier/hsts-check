#!/usr/bin/python3

import requests

sites = [
  ('Crédit Agricole', 'https://www.cf-g3-enligne.credit-agricole.fr/stb/entreeBam'),
  ('Société Générale', 'https://particuliers.societegenerale.fr/'),
  ('BNP Paribas', 'https://mabanque.bnpparibas/fr/connexion'),
]

for site in sites:
  r = requests.get(site[1], verify=False,  # Disabling cert checking, do not do this at home!
                   headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'})
  if 'strict-transport-security' in r.headers:
    print(site[0] + ': yes! [' + r.headers['strict-transport-security'] + ']')
  else:
    print(site[0] + ': no :(')
