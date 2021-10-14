cription
This lambda function is scheduled to called every five minutes to track the latency and 
availability of our website to monitor its health.


# How to run the project
- npm install @aws-cdk/core@1.122.0
- Note: In setup.py, make sure to use "aws-cdk.core==1.122.0",
- cd infra/
- python3 -m venv .venv &&  source .venv/bin/activate     # If not already installed
- pip install -r requirements.txt 
- cdk synth && cdk deploy

