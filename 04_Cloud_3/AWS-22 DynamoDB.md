# DynamoDB
DynamoDB is een serverless NoSQL database, die automatische ultraschaalbaar is, op basis van snelle SSD's. Meerdere AZ's (3 per regio). Elastic MapReduce-integratie. Back-up naar S3. Het ondersteunt Key-value en een document data structuur.

De structuur lijkt volgens mij op een Tuple. Die ken ik dan weer vanuit Python.

Ik heb een mindmap gemaakt van de features van DynbamoDB.  
![mindmap](../00_includes/mindmap-dynamodb.png)

## Key-terms
- Alle key-terms die betrekking hebben op AWS Cloud Practitioner, zijn te vinden in het document: [AWS-Cloud-Practitioner](../beschrijvingen/aws-cloud-practitioner.md)  
- [NoSQL](../beschrijvingen/aws-cloud-practitioner.md#NoSQL)  

## Opdracht
Ik heb de stappen in de workshop: Hands-on Labs fo Amazon DynamoDB gevolgd.
- https://amazon-dynamodb-labs.workshop.aws/hands-on-labs.html  

De architectuur die in deze oefening gebouwd wordt ziet er als volgt uit:  
![architectuur](../00_includes/AWS-22a.png)
### Gebruikte bronnen
- https://aws.amazon.com/dynamodb/
- https://amazon-dynamodb-labs.workshop.aws/hands-on-labs.html  
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html

### Ervaren problemen
Geen

### Resultaat
**Environment Setup**  
*Creating the Stack*  
![stack](../00_includes/AWS-22b.png)  

![stack2](../00_includes/AWS-22c.png)  

De Stack is klaar:  
![stack](../00_includes/AWS-22d.png)

**Launch Cloud9**  
![cloud9](../00_includes/AWS-22e.png)

**Create the DynamoDB tables**  
De schermafdruk is een fragment van de code!  
![tables](../00_includes/AWS-22f.png)

**Load sample data**  
Download en unzip de data  
![data](../00_includes/AWS-22g.png)  

Het laden van de sample data  
![data](../00_includes/AWS-22h.png)  

**Explore DynamoDB with the CLI**  
Scan de database (een fragment)  
![scan](../00_includes/AWS-22i.png)

1 item uit de database  
![item](../00_includes/AWS-22j.png)  

Nu met een aantal opties  
![opties](../00_includes/AWS-22k.png)

Scan op tabel met Partition key en Sort key  
![scan](../00_includes/AWS-22l.png)

Uitlezen van Thread 1  
![thread1](../00_includes/AWS-22m.png)

**Oefening: return only the first reply to a thread** 
Het was even zoeken in de developerguide.  
![oef1](../00_includes/AWS-22n.png)

**Oefening: return only the most recent reply for a thread**  
![oef2](../00_includes/AWS-22o.png)

**Oefening: Explore the data in the Forum table and write a scan command to return only the Forums that have more than 1 thread and more than 50 views.**  
De tabel structuur:  
![oef3](../00_includes/AWS-22p.png)

De scan:  
![scan](../00_includes/AWS-22q.png)

**Oefening: Update the ProductCatalog item where Id=201 to add new colors “Blue” and “Yellow” to the list of colors for that bike type. Then use the API to remove those “Blue” and “Yellow” list entries to return it to the original state.**  
Item opvragen:  
![get](../00_includes/AWS-22r.png)

Blauw en Geel toevoegen:  
![kleur](../00_includes/AWS-22s.png)

Verwijder blauw en geel:  
![wegkleur](../00_includes/AWS-22t.png)

**Oefening: Find all the Replies written by User A sorted, using the query command instead of the scan command.**  
GSI query:  
![oef4](../00_includes/AWS-22u.png)

**CleanUp**  
![foetsie](../00_includes/AWS-22v.png)