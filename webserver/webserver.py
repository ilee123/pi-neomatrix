'''
	Raspberry Pi GPIO Status and Control
'''
import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

#define sensors GPIOs
button = 20
senPIR = 16

#define actuators GPIOs
ledRed = 13
ledYlw = 19
ledGrn = 26

#initialize GPIO status variables
buttonSts = 0
senPIRSts = 0
ledRedSts = 0
ledYlwSts = 0
ledGrnSts = 0
	
@app.route("/")
def index():
	# Read GPIO Status
	buttonSts = 0
	senPIRSts = 0
	ledRedSts = 0
	ledYlwSts = 0
	ledGrnSts = 0

	templateData = {
      'button'  : buttonSts,
      'senPIR'  : senPIRSts,
      'ledRed'  : ledRedSts,
      'ledYlw'  : ledYlwSts,
      'ledGrn'  : ledGrnSts,
      }
	return render_template('index.html', **templateData)
	
# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	if deviceName == 'ledRed':
		actuator = ledRed
	if deviceName == 'ledYlw':
		actuator = ledYlw
	if deviceName == 'ledGrn':
		actuator = ledGrn
   
	if action == "on":
		GPIO.output(actuator, GPIO.HIGH)
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
   
	templateData = {
	  'button'  : buttonSts,
      'senPIR'  : senPIRSts,
      'ledRed'  : ledRedSts,
      'ledYlw'  : ledYlwSts,
      'ledGrn'  : ledGrnSts,
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='192.168.21.185', port=80, debug=True)