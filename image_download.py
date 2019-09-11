import urllib.request

main_url = "https://cdn4.geckoandfly.com/wp-content/uploads/2015/03/positive-quotes-of-the-day-life"

for i in range(1, 21):
	file_url = main_url + str(i) + ".jpg"
	# if i == 1:
	# 	file_url = main_url + ".jpg"
	file_name = str(i) + "positive-quotes-of-the-day-life" + ".jpg"
	print("Downloading - " + file_url)
	try:
		urllib.request.urlretrieve(file_url, file_name)
	except:
		print("something went wrong...")
