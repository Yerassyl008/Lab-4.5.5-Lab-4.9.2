import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "FgH1byRszETmOQ12z2viAjB8ELvdHHkO"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)