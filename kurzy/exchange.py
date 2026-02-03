import httpx

r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt;jsessionid=CE90DB9B266D3B51A3856C0794DE7D42')
print(r.text)
print(r.status)
lines = r.text.split('\n')
print(lines[0])

