# Library of various examples of using IOT Core with related GCP functionality

## Device Simulator
* Code located in 'device'
* Includes python script device_simulator.py which will publish a message every 10 seconds (currently publishing arbitrary data)
* In order to use script user must export the following environmental variables before running: PROJECT_ID, REGION, REGISTRY_ID, DEVICE_ID, PATH_TO_KEY
Example: 
```
	export PROJECT_ID='fakeProjectId
	export REGION='us-central1'
	export REGISTRY_ID='fakeRegistryId'
	export DEVICE_ID='fakeDeviceId'
	export PATH_TO_KEY='relative/path/to/public/key
	
	python device_simulator.py
```
