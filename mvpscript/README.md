
# Hier is de code te vinden van het MVP v1.0

Dit is een Python ontwikkeling met de AWS CDK

Het `cdk.json` bestand vertelt de CDK Toolkit hoe de app wordt gedraaid.

Dit project is opgezet als een standaard python project. Het initialisatie
proces maakt een virtualenv binnen het project, die wordt opgeslagen onder
de `.venv` directory. De virtualenv neemt aan dat er een `python3`
executable in het pad aanwezig is om toegang te krijgen tot de `venv`
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
