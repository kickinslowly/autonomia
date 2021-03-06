Autonomia is an automated environment in which creatures spawn, evade, hunt, reproduce and die. The goal of this project was to work with Python concepts that I had not yet used.

The Python concepts I tried to focus on here are classes, matplotlib and sqlite3. I used Turtle to visually represent each creature in real time.

By far the most extensively used concept in this project are classes. I defined creature classes with set attributes such as name, rank, oxygen, carbon, location etc. I defined
methods that would allow the creature to interact with its environment and other creatures, such as spawn, evade, hunt, reproduce, die. I also created the world environment using 
classes. The world has a set amount of resources such as carbon, oxygen. The world tracks time since it came into existence and creatures inside it.

I used matplotlib to plot the population totals of creatures within the world during every cycle it runs. This is basic, but implementation was successful and provided a visual 
aid to track total creature population over time.

I used sqlite3 as a database to store creature data. ![image](https://user-images.githubusercontent.com/13421736/103305249-78d8fe00-49bf-11eb-97bf-9a794fe486d2.png)

Each cycle of the world the sqlite3 database is updated with all creatures in the world. This is basic, but implementation was
successful and provided an aid in understanding creature characteristics and creature population patterns.

This project is completely automated and only needs to be 'run' and then observed. The point was to create a system that could interact with itself and output world/creature data 
to an external database as well as provide visual representation in real time. 
