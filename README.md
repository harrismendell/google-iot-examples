# Library of various examples of using IOT Core with related GCP functionality

## Device Simulator
* Code located in 'device'
* Includes python script device_simulator.py which will publish a message every 10 seconds (currently publishing arbitrary data)
* Steps to run device_simualtor.py:
..1. change directory into 'device'
..2. pip install pipenv (Virtual environment management system to run your script in)
..3. pipenv start
..4. pip install
..5. export the following environmental variables before running: PROJECT_ID, REGION, REGISTRY_ID, DEVICE_ID, PATH_TO_KEY
Example: 
```
	export PROJECT_ID='fakeProjectId
	export REGION='us-central1'
	export REGISTRY_ID='fakeRegistryId'
	export DEVICE_ID='fakeDeviceId'
	export PATH_TO_KEY='relative/path/to/public/key
	
	python device_simulator.py
```
