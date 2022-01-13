# Lambda
AWS Lambda is een 'event-driven', serverlESS computerplatform dat door Amazon wordt aangeboden als onderdeel van Amazon Web Services. Daarom hoeft jij je geen zorgen te maken over welke AWS-bronnen je moet starten of hoe jij ze gaat beheren. In plaats daarvan moet je de code op Lambda zetten en dan werkt het.

In AWS Lambda wordt de code uitgevoerd op basis van de respons op gebeurtenissen in AWS-services (meer dan 200) en Software as a service (Saas) applicaties, zoals bestanden toevoegen/verwijderen in S3-bucket, HTTP-verzoek van Amazon API-gateway, enz. Amazon Lambda kan echter alleen worden gebruikt om achtergrondtaken uit te voeren.

De AWS Lambda-functie helpt je te concentreren op jouw kernproduct en bedrijfslogica in plaats van het beheer van toegangscontrole van het besturingssysteem (OS), OS-patching, juiste grootte, provisioning, schaling, enz.

In de AWS Free Tier versie krijg je de beschikking over 1 miljoen requests.

Ik heb een mindmap gemaakt van de features van AWS Lambda:  
![lambda](../00_includes/mindmap-aws-lambda.png)

## Key-terms
- Alle key-terms die betrekking hebben op AWS Cloud Practitioner, zijn te vinden in het document: [AWS-Cloud-Practitioner](../beschrijvingen/aws-cloud-practitioner.md)  

## Opdracht
Hoe een RDS MySQL uitvragen via AWs Lambda in Python van AWS Lambda in Python.  
https://www.youtube.com/watch?v=vyLvmPkQZkI
### Gebruikte bronnen
- https://aws.amazon.com/lambda/
- 

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
**Database aanmaken**  
![rds](../00_includes/AWS-24a.png)

Via SQL Workbench contact maken met de database:  
![sql](../00_includes/AWS-24b.png)

Database aanmaken en de tabel:  
![sql](../00_includes/AWS-24c.png)

En we vullen de tabel met 2 rijen data:  
![sql](../00_includes/AWS-24d.png)

