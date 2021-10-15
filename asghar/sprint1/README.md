# Website Health Checker 

## This is code for running periodic lambda function on Cloud infrastructure defined by Cloud Develeopment Kit (CDK)

> #### How to use project
>
> - First move to infra forlder where insfrastructure of cloud is defined
> - Then install all requirements using pip
> - The requirements in requirenment.txt are loaded from a setup.py with  install_requires list.
> - After that write cdk synth to generate .yml for cloud infrastructure.
> - Then write cdk deploy to deploy the project.
> - The project can be viewed by visiting lambda in ***aws console***

##### Commands

```
cd infra
```
```
python -m pip install -r requirements.txt
```
```
cdk synth && cdk deploy
```
