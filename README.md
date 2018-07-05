# Library of various examples of using IOT Core with related GCP functionality

## Device Simulator
* Code located in 'device'
* Includes python script device_simulator.py which will publish a message every 10 seconds (currently publishing arbitrary data)
* Steps to run device_simualtor.py:
	1. change directory into 'device'
	2. pip install pipenv (Virtual environment management system to run your script in)
	3. pipenv start
	4. pip install
	5. create private and public key pairs with following commands:
		1. openssl genrsa -out rsa_private.pem 2048
		2. openssl rsa -in rsa_private.pem -pubout -out rsa_public.pem
	6. Create registry and device in iot core, give device the newly created public key
	7. Save public key somewhere and use its path in the PATH_TO_KEY field in next step
	8. export the following environmental variables before running: PROJECT_ID, REGION, REGISTRY_ID, DEVICE_ID, PATH_TO_KEY
Example: 
```
	export PROJECT_ID='fakeProjectId
	export REGION='us-central1'
	export REGISTRY_ID='fakeRegistryId'
	export DEVICE_ID='fakeDeviceId'
	export PATH_TO_KEY='relative/path/to/public/key
	
	python device_simulator.py
```
