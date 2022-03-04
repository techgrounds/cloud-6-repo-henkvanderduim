# Parameters
In de tabel hieronder wordt uitleg gegeven over de Parameters die gebruikt worden in het bestand 'mvpscript_stack.py'.  
Als bepaalde termen je als Cloud Engineer onbekend voorkomen dan heb ik hier de oplossing: [Cloud Engineer](https://nl.indeed.com/CEO-vacatures?vjk=4accb240ecb6653b).

## CDK JSON Tabel
| Parameter                         | wat wordt er ingevuld                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **VPC**                           |                                                                                                                                      |
| mngt_name                         | Naam van de VPC voor de MANAGEMENT-PRD-VPC                                                                                           |
| mngt_cidr_block                   | CIDR Block voor de MANAGEMENT-PRD-VPC                                                                                                |
| mngt_cidr_mask                    | CIDR Mask voor de subnets in de MANAGEMENT-PRD-VPC                                                                                   |
| mngt_subnet_name                  | Subnet naam voor de subnets in de MANAGEMENT-PRD-VPC                                                                                 |
| mngt_max_azs                      | Aantal Availability Zones (AZ) in de MANAGEMENT-PRD-VPC                                                                              |
| wsrv_name                         | Naam van de VPC voor de APP-PRD-VPC                                                                                                  |
| wsrv_cidr_block                   | CIDR Block voor de APP-PRD-VPC                                                                                                       |
| wsrv_cidr_mask                    | CIDR Mask voor de subnets in de APP-PRD-VPC                                                                                          |
| wsrv_subnet_name                  | Subnet naam voor de subnets in de APP-PRD-VPC                                                                                        |
| wsrv_max_azs                      | Aantal Availability Zones (AZ) in de APP-PRD-VPC                                                                                     |
| vpcp_name                         | De naam van de VPC Peering Connectie                                                                                                 |
| vpcp_regin                        | De regio waarin de VPC Peering plaatsvindt                                                                                           |
| mngt_vpcp_route                   | VPC Route Table naam voor MANAGEMENT-PRD-VPC                                                                                         |
| wsrv_vpcp_route                   | VPC Route Table naam voor APP-PRD-VPC                                                                                                |
| **Role**                          |                                                                                                                                      |
| iam_ssm_role                      | Naam van de Role                                                                                                                     |
| iam_ssm_principal                 | De Principal van de Role, in dit geval de ec2                                                                                        |
| **Bucket**                        |                                                                                                                                      |
| bucket_name                       | Naam van de Bucket                                                                                                                   |
| versioned                         | Versioned toepassen: true/false                                                                                                      |
| auto_delete_objects               | Bij verwijderen van de bucket, automatisch de inhoud van de bucket verwijderen: true/false                                           |
| deploy_name                       | Naam van de bucket deployment                                                                                                        |
| source                            | Bron van de file(s) die in de bucket geplaatst worden                                                                                |
| **Security Groups**               |                                                                                                                                      |
| mngt_sg_name                      | Naam van de Security Group in het subnet van de  MANAGEMENT-PRD-VPC omgeving                                                         |
| mngt_sg_description               | Omschrijving van de Security Group in het subnet van de MANAGEMENT-PRD-VPC omgeving                                                  |
| mngt_sg_allow_all_outbound        | *Rule* voor al het uitgaande verkeer in het subnet van de MANAGEMENT-PRD-VPC omgeving                                                |
| mngt_sg_ssh_rule_ip               | IP Adres(sen) die toegang krijgt tot het subnet van de MANAGEMENT-PRD-VPC omgeving via SSH. Meerdere adressen scheiden met komma     |
| mngt_sg_ssh_rule_port             | De poort waarmee er via SSH toegang verkregen wordt tot het subnet van de MANAGEMENT-PRD-VPC omgeving                                |
| mngt_sg_rdp_rule_ip               | IP Adres(sen) die toegang krijgt tot het subnet van de MANAGEMENT-PRD-VPC omgeving via RDP. Meerdere adressen scheiden met een komma |
| mngt_sg_rdp_rule_port             | De poort waarmee er via RDP toegang verkregen wordt tot het subnet van de MANAGEMENT-PRD-VPC omgeving                                |
| wsrv_sg_name                      | Naam van de Security Group in het subnet van de APP-PRD-VPC omgeving                                                                 |
| wsrv_sg_description               | Omschrijving van de Security Group in het subnet van de APP-PRD-VPC omgeving                                                         |
| wsrv_sg_allow_all_outbound        | *Rule* voor al het uitgaande verkeer in het subnet van de APP-PRD-VPC omgeving                                                       |
| wsrv_sg_rule_port                 | De poort waarmee via SHH toegang verkregen wordt tot het subnet van de APP-PRD-VPC omgeving                                          |
| wsrv_sg_http_rule_port            | De poort waarmee via HTTP toegang verkregen wordt tot het subnet van de APP-PRD-VPC omgeving                                         |
| wsrv_sg_https_rule_port           | De poort waarmee via HTTPS toegang verkregen wordt tot het subnet van de APP-PRD-VPC omgeving                                        |
| **Key Pairs**                     |                                                                                                                                      |
| mngt_kp                           | Key Pair voor de EC2 instance in MANAGEMENT-PRD-VPC omgeving                                                                         |
| mngt_kp_name                      | Naam van de Key Pair voor de EC2 instance in de MANAGEMENT-PRD-VPC omgeving                                                          |
| mngt_kp_description               | Omschrijving van de Key Pair voor de EC2 Instance in de MANAGEMENT-PRD-VPC omgeving                                                  |
| mngt_kp_store                     | Moet de *Public Key* van het Key Pair voor de EC2 instance in de MANAGEMENT-PRD-VPC omgeving worden opgeslagen: true/false           |
| wsrv_kp                           | Key Pair voor de EC2 instance in APP-PRD-VPC omgeving                                                                                |
| wsrv_kp_name                      | Naam van de Key Pair voor de EC2 instance in de APP-PRD-VPC omgeving                                                                 |
| wsrv_kp_description               | Omschrijving van de Key Pair voor de EC2 Instance in de APP-PRD-VPC omgeving                                                         |
| wsrv_kp_store                     | Moet de *Public Key* van het Key Pair voor de EC2 instance in de APP-PRD-VPC omgeving worden opgeslagen: true/false                  |
| **EC2 Instances**                 |                                                                                                                                      |
| mngt_ec2_name                     | Naam van de EC2 Instance in de MANAGEMENT-PRD-VPC omgeving                                                                           |
| mngt_ec2_instance_type            | Het type van de EC2 Instance in de MANAGEMENT-PRD-VPC omgeving                                                                       |
| mngt_ec2_device_name              | Naam van het device (EBS) bij de EC2 Instance in de MANAGEMENT-PRD-VPC omgeving                                                      |
| mngt_ec2_encrypted                | Aangeven of alles versleuteld dient te worden van de EC2 Instance in de MANAGEMENT-PRD-VPC omgeving                                  |
| wsrv_ec2_name                     | Naam van de EC2 Instance in de APP-PRD-VPC omgeving                                                                                  |
| wsrv_ec2_instance_type            | Het type van de EC2 Instance in de APP-PRD-VPC omgeving                                                                              |
| wsrv_ec2_device_name              | Naam van het device (EBS) bij de EC2 Instance in de APP-PRD-VPC omgeving                                                             |
| wsrv_ec2_encrypted                | Aangeven of alles versleuteld dient te worden van de EC2 Instance in de APP-PRD-VPC omgeving                                         |
| **Webscript**                     |                                                                                                                                      |
| wsrv_asset_name                   | Naam van de asset die je gebruikt om het webscript te lanceren                                                                       |
| wsrv_asset_path                   | Lokaal pad waar het webscript te vinden is                                                                                           |
| wsrv_asset_region                 | Regio waarin het webscript gelanceerd moet worden                                                                                    |
| **Tags**                          |                                                                                                                                      |
| mngt_tag_key                      | De key waarde van de tag in de MANAGEMENT-PRD-VPC omgeving                                                                           |
| mngt_tag_value                    | De Value behorende bij de key in de MANAGEMENT-PRD-VPC omgeving                                                                      |
| wsrv_tag_key                      | De key waarde van de tag in de APP-PRD-VPC omgeving                                                                                  |
| wsrv_tag_value                    | De Value behordende bij de key in de APP-PRD-VPC omgeving                                                                            |
| **Bus** Backup Vaults/Plans/Rules |                                                                                                                                      |
| mngt_vault_key                    | Naam van de sleutel van de Backup Vault in de MANAGEMENT-PRD-VPC omgeving                                                            |
| mngt_vault_name                   | Naam van de vault in de MANAGEMENT-PRD-VPC omgeving                                                                                  |
| mngt_backup_vault_name            | Naam van de Backup Vault in de MANAGEMENT-PRD-VPC omgeving                                                                           |
| mngt_backup_plan                  | Naam van het Plan in de MANAGEMENT-PRD-VPC omgeving                                                                                  |
| mngt_backup_plan_name             | Naam van het Backup Plan in de MANAGEMENT-PRD-VPC omgeving                                                                           |
| mngt_rule_name                    | Naam van de Backup Rule in de MANAGEMENT-PRD-VPC omgeving                                                                            |
| mngt_minute                       | De minuut van de cron job in de Backup Rule in de MANAGEMENT-PRD-VPC omgeving                                                        |
| mngt_hour                         | Het uur van de cron job in de Backup Rule in de MANAGEMENT-PRD-VPC omgeving                                                          |
| mngt_month                        | De maand(en) van de cron job in de Backup Rule in de MANAGEMENT-PRD-VPC omgeving                                                     |
| mngt_weekday                      | De dag(en) van de week van de cron job in de Backup Rule in de MANAGEMENT-PRD-VPC omgeving                                           |
| mngt_duration                     | Het aantal dagen dat de backups bewaart blijven in de MANAGEMENT-PRD-VPC omgeving                                                    |
| wsrv_vault_key                    | Naam van de sleutel van de Backup Vault in de APP-PRD-VPC omgeving                                                                   |
| wsrv_vault_name                   | Naam van de vault in de APP-PRD-VPC omgeving                                                                                         |
| wsrv_backup_vault_name            | Naam van de Backup Vault in de APP-PRD-VPC omgeving                                                                                  |
| wsrv_backup_plan                  | Naam van het Plan in de APP-PRD-VPC omgeving                                                                                         |
| wsrv_backup_plan_name             | Naam van het Backup Plan in de APP-PRD-VPC omgeving                                                                                  |
| wsrv_rule_name                    | Naam van de Backup Rule in de APP-PRD-VPC omgeving                                                                                   |
| wsrv_minute                       | De minuut van de cron job in de Backup Rule in de APP-PRD-VPC omgeving                                                               |
| wsrv_hour                         | Het uur van de cron job in de Backup Rule in de APP-PRD-VPC omgeving                                                                 |
| wsrv_month                        | De maand(en) van de cron job in de Backup Rule in de APP-PRD-VPC omgeving                                                            |
| wsrv_weekday                      | De dag(en) van de week van de cron job in de Backup Rule in de APP-PRD-VPC omgeving                                                  |
| wsrv_duration                     | Het aantal dagen dat de backups bewaart blijven in de APP-PRD-VPC omgeving                                                           |
