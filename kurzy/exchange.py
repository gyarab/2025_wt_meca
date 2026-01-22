import httpx

r = httpx.get('URL z ukolu 2')
print(r.text)
print(r.status)
lines = r.text.split('\n')
print(lines[0])

