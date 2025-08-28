# Designing Databases 
Portfolio Exercise 
## Brief 
Design the each of the databases listed below:
1. A database to store computers and their specs. (eg, GHz, cores, etc).
   ```mermaid
   ---
   config:
   layout: dagre
   theme: redux-dark
   look: classic
   ---
   erDiagram
      direction LR
   Computer {
         int id PK
         varchar name
         varchar owner
         varchar OS
      }
   HDD {
         int id PK
         int computer_id FK
         bigint capacity
         int IO_rate
         bool is_SSD
         varchar manufacturer
         int rpm
      }
   CPU {
         int id PK
         int computer_id FK
         int cores
         int ghz
         varchar manufacturer
      }
   RAM {
         int id PK
         int computer_id FK
         int capacity
         int ghz
         varchar manufacturer
      }

      Computer ||--|{ HDD :"  "
      Computer ||--|{ CPU :"  "
      Computer ||--|{ RAM :"  "
   ```
2. A database to store foods and their expiry dates for a home. It should also record whether the food has been frozen (in which case the expiry date doesn’t matter).
   ```mermaid
   ---
   config:
   layout: dagre
   theme: redux-dark
   look: classic
   ---
   erDiagram
      direction LR
   House {
         int id PK
         varchar name
         varchar address
         varchar owner
      }
   Food {
         int id PK
         int house_id FK
         int count
         varcahr name
         timestamp purchase_date
         date expiry_date
         bool frozen
      }

      House ||--|{ Food :"  "
   ```
3. A shared office space needs a database to record which computing devices (computers, phones and tablets) brought in by the people working there belongs to who. 
   ```mermaid
   ---
   config:
   layout: dagre
   theme: redux-dark
   look: classic
   ---
   erDiagram
      direction LR
   Owner {
         int id PK
         varchar first_name
         varchar last_name
         varchar department
      }
   Device {
         int id PK
         int owner_id FK
         int count
         varchar device_type
      }

      Owner ||--|{ Device :"  "
   ```
4. Create a database that stores in which room of a house various expensive items are kept for insurance purposes. The items could include things like fridges, TVs, washing machines, computers, artwork, furniture... Anything stationary and expensive. 
   ```mermaid
   ---
   config:
   layout: dagre
   theme: redux-dark
   look: classic
   ---
   erDiagram
      direction LR
   Room {
         int id PK
         varchar room_name
      }
   Item {
         int id PK
         int room_id FK
         varchar item_description
         varchar item_type
         money value
      }

      Room ||--|{ Item :"  "
   ```
   ```sql
   CREATE DATABASE IF NOT EXISTS Valuables;
   USE Valuables;

   CREATE TABLE IF NOT EXISTS Rooms (
      id INT PRIMARY KEY AUTO_INCREMENT,
      room_name VARCHAR(255)
   );

      CREATE TABLE IF NOT EXISTS Items (
      id INT PRIMARY KEY AUTO_INCREMENT,
      room_id INT NOT NULL,
      item_description VARCHAR(255),
      item_type VARCHAR(255) DEFAULT 'Appliance',
      `value` DECIMAL NOT NULL,
      FOREIGN KEY (room_id) REFERENCES Rooms(id) 
   );
   ```
5. Create a database to store books and their authors. 
   ```mermaid
   ---
   config:
   layout: dagre
   theme: redux-dark
   look: classic
   ---
   erDiagram
      direction LR
   Author {
         int id PK
         varchar first_name
         varchar last_name
      }
   Book {
         int id PK
         int author_id FK
         varchar title
         varchar ISBN
         int pages
      }

      Author ||--|{ Book :"  "
   ```
6. Create a database to record which movies are being shown at which cinemas in a chain. 
   ```mermaid
   erDiagram
      Cinema {
         string id PK
         string name
         string location
         date theatres
         string phone
         string address
      }
      Screening {
         string id PK
         string Film_id FK
         string Cinema_id FK
         integer quantity
      }
      Film {
         string id PK
         string name
         time runtime
         char rating
      }

      Cinema ||--o{ Screening : "   "
      Film ||--o{ Screening : "   "
   ```
7. Create a database for TAFE. You should include students, lecturers, clusters, units and rooms. This is a more complex database than any previous, so take it slow and consider everything carefully. 
      ```mermaid
   ---
   config:
   layout: dagre
   theme: redux-dark
   look: classic
   ---
   erDiagram
   Students {
         int id PK
         int cluster_id FK
         varchar first_name
         varchar last_name
         varchar e_mail
         varchar address
         string phone
      }
   Lecturers {
         int id PK
         int cluster_id FK
         int Units_ID FK
         varchar first_name
         varchar last_name
         varchar e_mail
         varchar address
         string phone
      }
   Clusters {
         int id PK
         int Units_id FK
         varchar unit
         varchar last_name
      }
   Units_Clusters {
         string id PK
         string Units_id FK
         string Clusters_id FK
      }
   Units {
         int id PK
         int Clusters_id FK
         int Lecturers_id FK
         int Rooms_id FK
         varchar subject
         varchar code
         int hours
         bool online
      }
      Units_Rooms {
         string id PK
         string Units_id FK
         string Rooms_id FK
      }
   Rooms {
         int id PK
         int Units_id FK
         varchar campus
         int capacity
         varchar facilities
      }
      Students }|--|| Clusters :"  "
      Lecturers }|--|| Clusters :"  "
      Units_Clusters }|--|| Clusters :"  "
      Units_Clusters }|--|| Units :"  "
      Units_Rooms }|--|| Rooms :"  "
      Units_Rooms }|--|| Units :"  "
   ```

A few notes:
* To make it easy, you don’t have to use the crows feet to denote the many side of a relationship if you don’t want to. Instead, put a “1” on the side of the line which is the one side of the relationship and a “M” on the many side.
* Don’t forget to include a primary key for every table. 
* Consider carefully the relationships between tables. It may help to put the relationship in a sentence and see if it makes sense in English. For example: “A person has one driver’s license and each driver’s license belongs to one person.”
* No many-to-many relationships are allowed. Use join tables. 
* If you create a join table, try to give it a good name where ever possible. 
* Consider carefully what you will need to store in each table. You should have all the information you need and nothing you don’t.

## Notes
Create the tables diagrammatically; can use https://app.diagrams.net/.  
Actually create one example in SQL as well.


## Tips