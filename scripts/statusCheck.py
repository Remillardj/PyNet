import requests

def status_code(url):
	try:
		result = requests.get(url)
		return result.status_code
	except requests.exceptions.ConnectionError as e:
		return e