# Project (Cloud6. Sentia1)
In deze folder is alle informatie te vinden over het Project (versie 1.1) wat uitgevoert is na de voltooiing van versie 1.0.  
## Inhoud  
1. [MVP 1.1](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpfinal#mvp-11)  
2. [Belangrijke Mijlpalen](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpfinal#belangrijke-mijlpalen-v11)
3. [Het Project](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpfinal#het-project)
4. [Stackscript Gebruiken](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpfinal#stackscript-gebruiken)

## MVP 1.1
In het document [Project v1.1](https://docs.google.com/document/d/1CT8AtpS_o81EeGhCEzPSn8XVu-lkvngzHyz8zWnoGmE/edit) zijn de aanpassingen/aanvullingen op versie 1.0 van het project beschreven.

## Project Requirements Document v1.1
Alle zaken met betrekking tot de eisen, epics, aannames, doelen, uitwerkingen, etc. zijn beschreven in het [Project Requirements Document](../mvpfinal/Product_Requirements_Document_v_1_1.md).

## MVP Script v1.1
In dit document is de (technische)informatie te vinden over de 'nested stack' en de parameters in de 'cdk.json', de uitleg van de parameters wordt gegeven in het [Parameters](../mvpfinal/parameters_v_1_1.md) document.  

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpfinal#inhoud)  


## Belangrijke mijlpalen v1.1
| **Onderwerp**              | **Datum (pw)**  | **Progressie**                                                                               | **Datum klaar**            |
| -------------------------- | --------------- | -------------------------------------------------------------------------------------------- | -------------------------- |
| Introductie Project v1.1   | 14-03-2022 (w5) | ![Python Project](https://us-central1-progress-markdown.cloudfunctions.net/progress/100)     | 8 maart 2022               |
| Oplevering/Eindpresentatie | 08-04-2022 (w9) | ![Start Project v1.0](https://us-central1-progress-markdown.cloudfunctions.net/progress/100) | 30 maart 2022 (oplevering) |


## Projectactiviteiten v1.0
| **Project Activiteit**                                | **Datum (pw)**  | **Progressie**                                                                                                                              |
| ----------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Sprint 3 Review progressie app v1.1                   | 25-03-2022 (w7) | ![Sprint1rp](https://us-central1-progress-markdown.cloudfunctions.net/progress/100) - 25 maart 2022                                         |
| Sprint 4 Review oplevering app v1.1 / Eindpresentatie | 08-04-2022 (w9) | ![Sprint2ro](https://us-central1-progress-markdown.cloudfunctions.net/progress/50) - 30 maart 2022 (Oplevering)/08 april 2022 (Presentatie) |

## Het Project
Aan de hand van het [Project Plan](https://docs.google.com/document/d/1CT8AtpS_o81EeGhCEzPSn8XVu-lkvngzHyz8zWnoGmE/edit) en het [Product Requirements Document](../mvpfinal/Product_Requirements_Document_v_1_1.md), ben ik gekomen tot de volgende opbouw van de Minimum Viable Product (MVP) versie 1.1 (ik beschrijf alleen de verschillen t.o.v. versie 1.0):  
1. Er is een nested stack gebouwd, waarin de verschillende elementen in zijn verwerkt.
2. In de stack is de configuratie opgenomen zoals te zien is in het diagram:  
![diagram](../00_includes/MVP%20v1.1%20(AWS).drawio.png)  
3. Alle gebruikte parameters zijn opgenomen in het bestand `cdk.json`. Uitleg over alle parameters is terug te vinden in het document: [Parameters](../mvpfinal/parameters_v_1_1.md).
4. Toegevoegd zijn:
   1. Application Load Balancer
   2. Auto Scaling Group
   3. Private Subnets (in de VPC van de webserver)
   4. NAT Gateway in de public subnets (in de VPC van de webserver)
   5. Self-Signed Certificate 
   6. Health Check

## Nested Stack
De volgende bestanden zijn aangemaakt:
- **asg.py**: t.b.v. de Auto Scaling Group voor de webserver
- **mngt.py**: EC2 t.b.v. de Management Server
- **vpcs.py**: De benodigde VPC's, Subnets en NAT Gateways
- **vpcp.py**: De VPC Peering
- **sg.py**: De security groups t.b.v. de Management EC2, Auto Scaling Group en de Load Balancer
- **s3bucket.py**: t.b.v. de S3 Bucket met het launch script voor de webserver
- **roles.py**: De role die gebruikt wordt
- **elb.py**: De Application Load Balancer
- **backup.py**: T.b.v. het backuppen van de Management server en de webserver

## Self-Signed Certificate
Om dit te realiseren zijn er twee extra bestanden aangemaakt:
1. **certmaker.py**: hierin wordt het self-signed certificate aangemaakt
2. **aws_acm_certified.py**: het certificaat wordt geupload naar de AWS Certificate Manager en er wordt tevens gecontroleerd of het certificaat al aanwezig is.

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpfinal#inhoud)  

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

[naar boven](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/mvpfinal#inhoud)  