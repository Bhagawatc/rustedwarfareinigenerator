import os
from os import path


x = input('Spawner no.: ')

n_vehicle_class = 1
spawner_file_name = "spawner" + x
if(path.isfile(spawner_file_name) == False):
    f = open(spawner_file_name + ".ini", "w")
    print("File created called " + str(spawner_file_name))
    
    thats_it = False
    while(thats_it == False):
        vehicle_name = input("What is the vehicle code? ")
        quantity_vehicles = input("How many? ")
        finished = input('Another vehicle? Y or N')
        if(finished.lower() == 'y'):
            thats_it = False
        if(finished.lower() == 'n'):
            thats_it = True
            n_vehicle_class = n_vehicle_class + 1
        else:
            finished = input("Didn't catch that. Try again. Another vehicle (Y or N)? ")
        
    f.write("[core]\n") #line 1
    f.write("name: " + spawner_file_name + "\n") #line 2
    f.write("displayText: " + spawner_file_name[:7].upper() +" "+ spawner_file_name[7:8] + "\n") #line 3
    f.write("displayDescription: Spawns \\n - " + vehicle_name + " x " + quantity_vehicles + "\n") #line 4
    f.write("class: CustomUnitMetadata\n") #line 5
    f.write("price: 0\n") #line 6
    f.write("maxHp: 4000\n") #line 7
    f.write("mass: 0 \n" ) #line 8
    f.write("radius: 0 \n") #line 9
    f.write("\n") #line 10
    f.write("// n/a\n") #line 11
    f.write("\n") #line 12
    f.write("isBuilding: true \n") #line 13
    f.write("\n") #line 14
    f.write("[hiddenAction_Spawn]\n") #line 15
    f.write("autoTrigger: if numberOfUnitsInEnemyTeam(withTag='commandCenter', equalTo=1)\n") #line 16
    f.write("\n")#line 17
    f.write("spawnUnits:" + vehicle_name+"*"+str(quantity_vehicles)+"(offsetRandomY=115, offsetRandomX=115)\n") #line 18
    f.write("\n")#line 19
    f.write("alsoTriggerActions:delete\n") #line 20
    f.write("\n") #line 21
    f.write("[hiddenAction_delete]\n") #line 22
    f.write("deleteSelf:true \n") #line 23
    f.write("\n")#line 24
    f.write("[graphics]\n")#line 25
    f.write("image: picker.png \n")#line 26
    f.write("imageScale:0 \n")#line 27
    f.write("\n")#line 28
    f.write("[attack]\n")#line 29
    f.write("canAttack: false" + "\n" + "canAttackFlyingUnits: false" + "\n" + "canAttackLandUnits: false" + "\n" + "canAttackUnderwaterUnits: false\n") #line 30-33
    f.write("\n")# line 34
    f.write("[movement]" + "\n" + "movementType: NONE") #line 35-36
