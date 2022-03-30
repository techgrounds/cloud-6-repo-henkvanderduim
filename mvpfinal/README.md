
# Cloud6.Sentia1 - MVP Final (v1.1)

In de folder 07_Project van deze Github is alle [project documentatie](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/tree/main/07_Project#readme) te vinden over dit project en MVP v1.0.

## Het Project
Aan de hand van het [Project Plan](https://docs.google.com/document/d/1CT8AtpS_o81EeGhCEzPSn8XVu-lkvngzHyz8zWnoGmE/edit) en het [Product Requirements Document](https://github.com/techgrounds/cloud-6-repo-henkvanderduim/blob/main/07_Project/Product_Requirements_Document.md), is de MVP v1.1 gerealiseerd. In dit document bespreek ik alleen de verschillen t.o.v. MVP v1.0.


## Stack script gebruiken
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