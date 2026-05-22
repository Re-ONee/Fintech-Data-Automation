import requests 

def check_market(): 
	# A public API to get currency rates
	url = "https://api.exchangerate-api.com/v4/latest/USD"
	response = requests.get(url)
	data = response.json()

	egp.rate = data['rates']['EGP']
	print(f"Current USD to EGP: {egp_rate}")


	if egp_rate > 50: # Example threashold
		print("!!! ALERT: Significant currency movement detected !!!")

check_market()

