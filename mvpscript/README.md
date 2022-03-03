
# Cloud6.Sentia1 - MVP

In de folder 07_Project van deze Github is alle [project documentatie](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/07_Project#readme) te vinden over dit project.

## Het Project
Aan de hand van het [Project Plan](https://docs.google.com/document/d/1yiJkqn4bXbaM5r-KYqE907bFJSXZoPKeWgFpOIHl19E/edit) en het [Product Requirements Document](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Product_Requirements_Document.md), ben ik gekomen tot de volgende opbouw van de Minimum Viable Product (MVP):  
1. M.b.v. AWS CDK/Python een stack bouwen, die gebruikt kan worden door AWS Cloudformation.
2. In de stack is de configuratie opgenomen zoals te zien is in het diagram in het [Product Requirements Document](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Product_Requirements_Document.md).
3. Alle gebruikte parameters zijn opgenomen in het bestand `cdk.json`. Uitleg over alle parameters is terug te vinden in het document: [uitleg parameters]().

## Het bestand: mvpscript_stack.py
Dit bestand is als volgt opgebouwd:  
1. Eerst worden de benodigde *libraries* geladen.  
```python
### Importing the necessary libraries

import os.path
from urllib import response
import aws_cdk as cdk
from aws_cdk import (
    Duration,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_backup as backup,
    aws_events as event,
    aws_kms as kms,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_ssm as ssm,
    RemovalPolicy,
    CfnOutput,
    App,
    Stack,
    Tags,
)

from constructs import Construct
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_events import Schedule
from aws_cdk.aws_s3_assets import Asset
```

2. Dan wordt de *class* gedefinieerd:  
```python
class MvpscriptStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
```

3. Direct na de *class* definitie worden de parameters neergezet. Deze zijn terug te vinden in het document: [uitleg parameters]()

4. Vervolgens worden er twee VPC's en de VPC Peering aangemaakt:  
Voorbeeld van 1 VPC  
```python
### VPC 1 - Management VPC

        self.vpc1 = ec2.Vpc(
            self,
            vpc1_name,
            max_azs=vpc1_max_azs,
            cidr=vpc1_cidr_block,
            # Configure 1 subnet in each AZ, 2 AZ's.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name=vpc1_subnet_name,
                    cidr_mask=vpc1_cidr_mask,
                )
            ],
        )
```

5. Voor de VPC Peering moeten er twee *route tables* aangepast worden (één voorbeeld):  
```python
self.cfn_Route = ec2.CfnRoute(
            self,
            vpcp_route_table1,
            route_table_id=self.vpc1.public_subnets[1].route_table.route_table_id,
            destination_cidr_block=self.vpc2.vpc_cidr_block,
            vpc_peering_connection_id=self.cfn_vPCPeering_connection.ref,
        )
```

6. Er worden twee AMI's aangemaakt. Voor de webserver die gedeployed gaat worden een Linux machine en voor de management server een windows machine.

7. Ik heb een rol aangemaakt voor de *Secrets Manager*:  
```python
 role = iam.Role(
            self, 
            iam_ssm_role,
            assumed_by=iam.ServicePrincipal(iam_ssm_principal)
        )
        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonSSMManagedInstanceCore"
            )
        )
```

8. Vervolgens is de Bucket aangemaakt








Dit is een Python ontwikkeling met de AWS CDK

Het `cdk.json` bestand vertelt de CDK Toolkit hoe de app wordt gedraaid. En bevat alle parameters.

Dit project is opgezet als een standaard python project. Het initialisatie
proces maakt een virtualenv binnen het project, die wordt opgeslagen onder
de `.venv` directory. De virtualenv neemt aan dat er een `python3`
executable in het pad aanwezig is om toegang te krijgen tot de `.venv`
package. Als het automatisch creëeren van de virtualenv niet lukt, dan kan
er handmatig eentje gemaakt worden.

In de terminal (Powershell/CMD)

```
python -m venv .venv
```

Na de creatie van de virtualenv, kun je de virtualenv activeren op de volgende manier.

```
source .venv/bin/activate
```

OP een Windows platform gaat het zo:

```
.venv\Scripts\activate.bat
```

Als de virtualenv is geactiveerd, kun je de afhankelijkheden installeren.

```
pip install -r requirements.txt
```

Nu kun je de code synthesizen:

```
cdk synth
```

## Handige commando's

 * `cdk ls`          Lijst van alle stacks in de app
 * `cdk synth`       Synthesizes de Cloudformation template
 * `cdk deploy`      deploy deze stack in je standaard AWS account/region
 * `cdk diff`        vegelijk de deployed stack met de huidige status
 * `cdk docs`        open CDK documentatie

Have fun!
