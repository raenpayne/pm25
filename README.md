Pulls pm 2.5 value, 10 minute average, from your nearest PurpleAir sensor. Uses Twilio to send a text message when values change so you know when to open or close the windows.

### Google Cloud Platorm
I have this running on Google Cloud Platform and am using pub/sub to trigger the function. Old pm 2.5 values are stored in a file and am using Cloud Scheduler to run run the function and thus check the pm 2.5 value once per hour. 

If you do not have a Google Cloud Platform account, it's free to create and currently they offer $300.00 of credit for the first 90 days. 

### Text Feature
This uses Twilio to send the texts. You'll need to create an account. Trial accounts are free and give you $15.00 of credit, at this time.

### Future Updates
Currently the application will text if the sensor value changes from green to yellow or above or vice versa. I plan to update it so it will also text if say the air quality goes from red to yellow or yellow to red or orange or red, etc. 
