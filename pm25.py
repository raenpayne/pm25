def purpleair_sms(event, context):
	from twilio.rest import Client
	import json
	import requests
	from google.cloud import storage
	import base64

	# Twilio account info
	account_sid = 'Your Twilio ID'
	auth_token = 'Your Twilio Auth Token'

	#set Twilio account info = to client
	client = Client(account_sid, auth_token)

	# Purple Air's API is publicly available so you won't need to register a key.
	# However you do need the key and ID Number for the sensor you're interested in.
	# You can get these from Purple Air's map and viewing the JSON file in your browser. 
	# Copy and paste that url below.
	data = requests.get('https://www.purpleair.com/json?key=SENSOR_KEY&show=SENSOR NUMBER').json()

	
	# get 10 minute avg for PM2.5 reading
	stats = (data['results'][0]['Stats'])
	
	statsobj = json.loads(stats)

	# assign to variable and make it a float
	pm25 = float(statsobj['v1'])

	# log retrieved value
	print('retrieved pm 2.5 value of : {}'.format(pm25)) 

	# read old 2.5 value from file
	def download_blob():
	    storage_client = storage.Client()
	    bucket = storage_client.bucket('Your Google Cloud Storage Bucket url')
	    blob = bucket.blob('BLOB NAME')

	    return blob.download_as_string()		

	# set oldPM25 to value read from file/bucket where value was stored during previous upload
	# retrieved value is a string - make it a float to compare with new value inside windows function below
	oldPM25 = float(download_blob())
	
	# log downloaded value
	print('downloaded stored pm 2.5 value of : {}'.format(oldPM25))

	# upload new 2.5 value to file
	def upload_blob():
	    """Uploads a file to the bucket."""
	    # bucket_name = "your-bucket-name"
	    # source_file_name = "local/path/to/file"
	    # destination_blob_name = "storage-object-name"

	    storage_client = storage.Client()
	    bucket = storage_client.bucket('Your Google Cloud Storage Bucket url')
	    blob = bucket.blob('BLOB NAME')

	    blob.upload_from_string(str(pm25))

	# run upload_blob function to upload new pm2.5 value
	upload_blob()

	# return value and message text 
	def windows(pm25):
		if oldPM25 <= 12.0 and pm25 >= 13.0:
			return('Close your windows, the air is chalk! Current pm 2.5 is: '+str(pm25))

		elif oldPM25 >= 13.0 and pm25 <= 12.0:
			return('Open your windows, the air is free of chalk! Current pm 2.5 is: '+str(pm25))

		else:
			return None

	# assign returned value from windows() function to variable
	x = windows(pm25)

	# set text Message content to variable x which contains the returned value from the windows() function above
	Message = x

	numbers_to_message = ['+15556667777', '+15557778888']

	# Twilio Numbers & Message
	if Message is not None:

		for number in numbers_to_message:
		    client.messages.create(
		        body = Message,
		        from_ = '+1Your Twilio Number',
		        to = number
		    )

    # for manually triggering pub/sub
	a = base64.b64decode(event['data']).decode('utf-8')

	# If a == 'Force Text' in the Message Body when manually running pub/sub then function will run - for manually testing function/text
	if a == 'Force Text':
		for number in numbers_to_message:
		    client.messages.create(
		        body = 'The current PM2.5 Value is: {}'.format(pm25),
		        from_ = '+1Your Twilio Number',
		        to = number
		    )

	# log success and pm values
	return('Success: \nPM2.5 value last checked: {old} \nMost recent PM2.5 value is: {new}'.format(old=oldPM25, new=pm25))




