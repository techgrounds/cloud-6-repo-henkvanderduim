# Project (Cloud6. Sentia1)
In deze folder is alle informatie te vinden over het Project wat de komende weken uitgevoerd wordt.  
Het project kent twee fasen:  
1. [MVP 1.0](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpscript#mvp-10)  
2. [Belangrijke Mijlpalen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpscript#belangrijke-mijlpalen)
3. [Het Project](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpscript#het-project)
4. [Stackscript Gebruiken](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpscript#stack-script-gebruiken)

## MVP 1.0
## Project Document v1.0
In het document [PRO-01 Project](https://docs.google.com/document/d/1yiJkqn4bXbaM5r-KYqE907bFJSXZoPKeWgFpOIHl19E/edit) is het project beschreven.

## Project Requirements Document v1.0
Alle zaken met betrekking tot de eisen, epics, aannames, doelen, uitwerkingen, etc. zijn beschreven in het [Project Requirements Document](../07_Project/Product_Requirements_Document.md).
## JIRA v1.0
In Jira is een Roadmap aangemaakt voor het project. Op basis van de Epics is deze samengesteld.
Plek waar het te vinden is: [Jira](https://techgroundscloud6q.atlassian.net/jira/software/projects/PCS/boards/5).

## MVP Script v1.0

In dit document is de (technische)informatie te vinden over de 'mvpscript_stack.py' en de parameters in de 'cdk.json', de uitleg van de parameters wordt gegeven in het [Parameters](../mvpscript/parameters.md) document.  

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpscript#project-cloud6-sentia1)  


## Belangrijke mijlpalen
| **Onderwerp**              | **Datum (pw)**  | **Progressie**                                                                                     | **Datum klaar** |
| -------------------------- | --------------- | -------------------------------------------------------------------------------------------------- | --------------- |
| Start Python               | 07-02-2022 (w1) | ![Python Project](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)           | 8 februari 2022 |
| Start project (v1.0)       | 07-02-2022 (w1) | ![Start Project v1.0](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)       | 7 februari 2022 |
| Introductie Project v1.1   | 14-03-2022 (w5) | ![Introductie Project v1.1](https://us-central1-progress-markdown.cloudfunctions.net/progress/100) | 8 maart 2022    |
| Oplevering/Eindpresentatie | 08-04-2022 (w9) | ![Oplevering/Eindpresentatie](https://us-central1-progress-markdown.cloudfunctions.net/progress/0) | d.d.            |

## Projectactiviteiten
| **Project Activiteit**                                 | **Datum (pw)**  | **Progressie**                                                                                         |
| ------------------------------------------------------ | --------------- | ------------------------------------------------------------------------------------------------------ |
| Sprint 1: Review progressie app v1                     | 25-02-2022 (w3) | ![Sprint1rp](https://us-central1-progress-markdown.cloudfunctions.net/progress/100) - 25 februari 2022 |
| Sprint 2: Review oplevering app v1                     | 11-03-2022 (w5) | ![Sprint2ro](https://us-central1-progress-markdown.cloudfunctions.net/progress/100) - 7 maart 2022     |
| Sprint 3: Review progressie app v1.1                   | 25-03-2022 (w7) | ![Sprint3rp](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)                    |
| Sprint 4: Review oplevering app v1.1 / Eindpresentatie | 08-04-2022 (w9) | ![Sprint4ro](https://us-central1-progress-markdown.cloudfunctions.net/progress/30)                     |

# Cloud6.Sentia1 - MVP v1.0

In deze folder is alle project documentatie te vinden over dit project.

## Het Project
Aan de hand van het [Project Plan](https://docs.google.com/document/d/1yiJkqn4bXbaM5r-KYqE907bFJSXZoPKeWgFpOIHl19E/edit) en het [Product Requirements Document](../mvpscript/Product_Requirements_Document.md), ben ik gekomen tot de volgende opbouw van de Minimum Viable Product (MVP):  
1. M.b.v. AWS CDK/Python een stack bouwen, die gebruikt kan worden door AWS Cloudformation.
2. In de stack is de configuratie opgenomen zoals te zien is in het diagram in het [Product Requirements Document](../mvpscript/Product_Requirements_Document.md).
3. Alle gebruikte parameters zijn opgenomen in het bestand `cdk.json`. Uitleg over alle parameters is terug te vinden in het document: [Parameters](../mvpscript/parameters.md).
4. Ik ga er vanuit dat een cloud engineer hiermee aan de slag gaat. 

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

3. Direct na de *class* definitie worden de parameters neergezet. Deze zijn terug te vinden in het document: [Parameters](../mvpscript/parameters.md)

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

8. Vervolgens is de  s3 Bucket aangemaakt met de juiste instellingen. Om vervolgens de Security Groups aan te maken die nodig zijn voor eisen van het project.  
Ook de key pairs worden klaargemaakt voor het vervolg in het script.

9.  Daarna zijn de twee EC2 instances aangemaakt. Hieronder een voorbeeld:  
```python
management_server = ec2.Instance(
            self,
            ec1_name,
            instance_type=ec2.InstanceType(ec1_instance_type),
            machine_image=amzn_windows,
            vpc=self.vpc1,
            security_group=mngtsg,
            key_name=key.key_pair_name,
            block_devices=[
                ec2.BlockDevice(
                    device_name=ec1_device_name,
                    volume=ec2.BlockDeviceVolume.ebs(30, encrypted=ec1_encrypted),
                )
            ],
        )
```

10. De *User Data* die ik nodig heb om de webserver daadwerkelijk als webserver te laten functioneren, wordt dan in de S3 Bucket geplaatst om vevolgens vanuit de S3 Bucket gelanceert te worden.

11. Bij het Backup deel maak ik gebruik van *Tags*. Deze zijn als volgt samengesteld:  
```python
### Tags
        Tags.of(web_server).add("PRD", "WSBackup")
        Tags.of(management_server).add("MNGT", "MSBackup")
```

12. Als laatste zijn de Backup Vaults, Plans en Rules aangemaakt.

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpscript#project-cloud6-sentia1)  

## Stackscript gebruiken
Om het script te gebruiken doe je het volgende:  

In de terminal (VSCode/Powershell/CMD)
```
python -m venv .venv
```

Na de creatie van de virtualenv, kun je de virtualenv activeren op de volgende manier.

```
source .venv/bin/activate
```

Op een Windows platform gaat het zo:

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

Als dat foutloos gaat, dan deploy je de code:

```
cdk deploy
```

## Handige commando's

 * `cdk ls`          Lijst van alle stacks in de app
 * `cdk synth`       Synthesizes de Cloudformation template
 * `cdk deploy`      deploy deze stack in je standaard AWS account/region
 * `cdk diff`        vegelijk de deployed stack met de huidige status
 * `cdk docs`        open CDK documentatie

Have fun!

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpscript#project-cloud6-sentia1)  