import http.client

conn = http.client.HTTPConnection("businesscorp.com.br", port=80)
conn.request("GET", "/kjkas")
response = conn.getresponse()
headers = response.headers
conn2 = http.client.HTTPConnection('businesscorp.com.br', port=80)
conn2.request("GET", "/ajasj", headers=headers)
response2 = conn2.getresponse()
print(response.status)
conn.close()
conn2.close()

