from operator import index
from urllib import response
from wsgiref import headers
import requests, csv, sys, urllib.parse
from requests.api import head

def usage():
    print('Uso: {0} "ORDER"'.format(sys.argv[0]))
    print('Busque um order por vez')
    sys.exit(1)

def localizar(item):
  url = 'https://6f008c57-99e0-4a2e-8d80-782a71cf99db.mock.pstmn.io/orders/{0}'.format(item)

  headers = {
    'Accept': 'applcation/json',
    'Content-Type': 'applcation/json'
  }
  response = requests.request("GET",url,params="caller.id=661750045",data={})
  myjson = response.json()
  ourdata = []
  csvheader = ['HEADER']

  for x in myjson['order_items']:
    listing = [x['item']] #ficou pendente esta parte de buscar somente os campos solicitados no desafio
    ourdata.append(listing)

  with open('meli.csv','w',encoding='iso-8859-1',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csvheader)
    writer.writerows(ourdata)

  print("CSV gerado")

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        usage()

    localizar(urllib.parse.quote_plus(' '.join(sys.argv[1:])))