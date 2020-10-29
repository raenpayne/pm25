## PM25

Pulls PM2.5 value, 10 minute average, from your nearest PurpleAir sensor. Uses Twilio to send a text message when values change so you know when to open or close the windows.</br></br>
(Basically, I got tired of checking Purple Air's website every hour, or more often, during the fires to know whether I could finally open the windows or should in fact close them, before the Blade Runner atmosphere tried to infiltrate my sinuses.)

### Google Cloud Platorm
I have this running on Google Cloud Platform and am using pub/sub to trigger the function. Values for the PM2.5 value are stored and read from a file. Cloud Scheduler to runs the function once an hour. When it pulls the new value the function compares it to the old value stored in a file and if the value has moved from green to yellow (or above) or vice versa you'll receive a text message from your Twilio account letting you know whether to open or close the windows. 

If you do not have a Google Cloud Platform account, it's free to create and currently they offer $300.00 of credit for the first 90 days. So far, after running the function for nearly a month I've incurred $.01 in charges. 

### Text Feature
This uses Twilio to send the texts. You'll need to create an account. Trial accounts are free and give you $15.00 of credit, at this time. You'll have to verify any number you want to sent texts to with a trial account, so the phone and its owner will need to be present if you have a friend/housemate/partner who would also like automated texts about the air quality. 

### Future Updates
Currently the application will text if the PM2.5 value changes from green to any value at yellow or above, or vice versa. I plan to update it so it will also text if the air quality fluctuates between any range. 

### PM2.5 Values
It's possible to convert PM2.5 values witha number of other data points that can be pulled from Purple Air. However, for simplicity this just uses the unconverted pm 2.5 reading averaged over 10 minutes. 

