## AirGoon Mission generation

### Description

This is a script that generates goon missions based on a mission template combined with the sign-up sheet. 

The idea is to use the mission editor to create the mission template with all the enemies, vehicles, refuelers and what-have-you. But this is not a good way of handling the less static and more fickle aspects of the mission. Of course, the most fickle aspect is the goons themselves, occasionally distracted by something they call 'life'. To make organizing a mission not a soul crushing experience, all the things that might get adjusted along the way such as participants and radio frequencies are added on top of the template to create the finished mission. 

### Creating a mission template

A good way to start is the existing templates for the different maps. Place all the objects, enemies, triggers, et.c. you normally would to create an exciting mission. When it comes to the goons themselves, don't think too much: just place placeholder units for each flight, give them the name of the flight, the waypoints of the flight and place them where and how you want the flight to spawn.

### What the script does

The script with take the flight name from the signup sheet and create groups with those names and missions. Then, all the placeholder groups are fetched from the mission and their flight plans and positions are assigned to the new groups. 

Radio presets are also automatically assigned: ATC, and package frequencies from the signup sheet is set as channel 1 and 2 respectively on radio 2. The flight frequency from the signup sheet is set as channel 1 on radio 1. 

Then, all the refuelers are fetched from the mission and their frequencies as set as channel 2 and onwards on radio 1. The name of the refuel flight is also updated to include the channel number.