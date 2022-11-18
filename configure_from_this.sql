create database analytics;
use analytics;
create table analytics
(
Searchword VARCHAR(500) ,
EMOTION INT,
starttime TIMESTAMP,
endtime TIMESTAMP,
duration INT
);
create table tmstp
(
x timestamp
);


create database emot;
use emot;
create table emot
(
EMOTION varchar(20),
duration INT
);
insert into emot(EMOTION,duration)VALUES("angry" , 0 );
insert into emot(EMOTION,duration)VALUES("disgust" , 0 );
insert into emot(EMOTION,duration)VALUES("fear" , 0 );
insert into emot(EMOTION,duration)VALUES("Happy" , 0 );
insert into emot(EMOTION,duration)VALUES("Sad" , 0 );
insert into emot(EMOTION,duration)VALUES("Surprise" , 0 );
insert into emot(EMOTION,duration)VALUES("Neutral" , 0 );

create database Playlists;
use Playlists;
