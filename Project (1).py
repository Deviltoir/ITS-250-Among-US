##We aren't sure who wrote what honestly
##As we say in a later comment, we were talking to one another the whole time, and trading the file back and forth.
##We put an equal amount of work in, and you should be able to take our collective word for that.

crewmate1  = "Blue"
crewmate2  = "Orange"
crewmate3  = "Red"
crewmate4  = "Green"
imposter = "Purple"
Imposters = 1
BlueSus = 0
OrangeSus = 0
RedSus = 0
GreenSus = 0
PurpleSus = 0
##The goal of this code is to sort of emulate a game called Among Us, where a crew is slowly being killed off by an imposter among them, and they must
##either complete tasks or deduce who the imposter is in order to win. The Imposter wins if they can kill off all of the Crewmates, or convince the others of their
##innocence, and have them fight among each other, voting one another off of the ship.
##If you couldn't tell by now, Among Us is a multiplayer social deduction game, and we're very obviously going to be limited in what we can represent here.
##Me and Dylan traded off several times to write this code while in a Discord call the entire time. We're very professional, and not joking the entire time
##I promise.

##A lot of print statements are required because the game has been condensed to what is effectively a text-based adventure
##Many outcomes are the same because the Imposters win whenever there is only one crewmate remaining, because at that point they are defenseless against them.
##Because there are five crewmates, and each round is triggered by someone finding a body (usually), it sort of greatly simplified our code
while Imposters > 0:
    print ("In our game of Among Us, there are 4 crewmates and 1 imposter. The crewmates must work together in order to find the imposter among them.")
    print ("The imposter must kill all of the crewmates.")
    print ("Find the Imposter by deciding which crew member is the most suspicious")
    print ("Game Starts")
    print ("30 seconds into the round Blue is found dead, his body in the Cafeteria.")
##This is to register that because Blue is dead, there is one less Crewmate overall. The 'game' ends when either there
##are no Imposters or no Crewmates remaining.
    print ("Purple reported the body and casted the blame on Green as he was close by as well.")
    print ("Green stutters his way through a defense and everyone seems to blame him for the death of their comrade") 
    print ("Red says he was rewiring in Electrical")
    print ("And finally, Orange says that he was in Navigation, charting a course for the ship.")
    print ("Now, it is your job to decide which crewmate is the most suspicious and rank them on a scale of 1 to 10, please do not repeat numbers.")
    print ("How suspicious is Purple, on a scale of 1 to 9?")
##For some reason, 10 never worked. If Purple was 10 and Green was 7, Green would come out as the largest,
##and frankly we're too lazy to actually fix this issue
##It has been well over an hour, of trying to solve this, and the solution is
##10 is lame, we're using 9, it solved our problem.
##The user-input code is extremely fragile and we've spent way too long troubleshooting and instead, are forced to hope that whoever running the code
##can read, and actually decides to follow our instructions.
##Besides, it has clearly written instructions, and, y'know don't void the manufacturer's warranty.
##Seriously please don't mistreat the input.
    PurpleSus = input()
    print ("How suspicious is Green, on a scale of 1 to 9?")
    GreenSus = input()
    print ("How suspicious is Red, on a scale of 1 to 9?")
    RedSus = input()
    print ("How suspicious is Orange, on a scale of 1 to 9?")
    OrangeSus = input()
    if PurpleSus > GreenSus :
        if PurpleSus > RedSus :
            if PurpleSus > OrangeSus :
                print ("Purple was the imposter, there are 0 imposters remaining.")
##So, when someone is "voted out" in game, they are shunted out of an airlock. It isn't pretty, but the game also isn't actually graphic.
##The game is fairly colorful and fun to play with friends. It is however super duper dark if you actually put like three braincells together and think
##about it for at least five minutes. Buuuuuuuuuuuuuuuuuut we needed inspiration and Among Us was it sooooooooo
##don't think about it too hard
##mmkay?
                Imposters = Imposters - 1
            else:
                print ("Orange was not an imposter, there is 1 imposter remaining")
                print ("Green decides to watch the security cameras in the next round.")
                print ("Green watches Purple murder Red in the hallway.")
                print ("Green panics, and tries to leave the Security Room, when the door slams shut on him.")
                print ("Purple clamors out of the vent in the corner of the room and kills Green.")
                print ("There are no crewmates remaining. The imposter has won.")
                Imposters = Imposters - 1
        else:
            if RedSus > OrangeSus :
                print ("Red was not an imposter, there is 1 imposter remaining")
                print ("After a minute, Green finds Orange's body in Communications. He was going to turn them back on.")
                print ("The only other crewmember aboard is Purple, Purple is the imposter, Purple HAS to be the imposter... Purple is standing behind Green.")
                print ("Purple kills Green")
                print ("There are no crewmates remaining. The imposter has won.")
                Imposters = Imposters - 1
##This code ends the game, even though in this ending it isn't technically true, it justs the easiest way to do it.
##work smart not hard
            else:
                print ("Orange was not an imposter, there is 1 imposter remaining")
                print ("Green decides to watch the security cameras in the next round.")
                print ("Green watches Purple murder Red in the hallway.")
                print ("Green panics, and tries to leave the Security Room, when the door slams shut on him.")
                print ("Purple clamors out of the vent in the corner of the room and kills Green.")
                print ("There are no crewmates remaining. The imposter has won.")
                Imposters = Imposters - 1
    else: 
        if GreenSus > RedSus:
            if GreenSus > OrangeSus :
                print ("Green was not an imposter, there is 1 imposter remaining")
                print ("After a minute, Red finds Orange's body in Reactor. He was trying to stop a meltdown.")
                print ("The core suffers a critical failure and the ship is lost in space.")
                print ("There are no crewmates remaining. The imposter has won.")
                Imposters = Imposters - 1
            else:
                print ("Orange was not an imposter, there is 1 imposter remaining")
                print ("Green decides to watch the security cameras in the next round.")
                print ("Green watches Purple murder Red in the hallway.")
                print ("Green panics, and tries to leave the Security Room, when the door slams shut on him.")
                print ("Purple clamors out of the vent in the corner of the room and kills Green.")
                print ("There are no crewmates remaining. The imposter has won.")
                Imposters = Imposters - 1
        else:
            if RedSus > OrangeSus :
                print ("Red was not an imposter, there is 1 imposter remaining")
                print ("After a minute, Green finds Orange's body in Communications. He was going to turn them back on.")
                print ("The only other crewmember aboard is Purple, Purple is the imposter, Purple HAS to be the imposter... Purple is standing behind Green.")
                print ("Purple kills Green")
                print ("There are no crewmates remaining. The imposter has won.")
                Imposters = Imposters - 1
            else:
                print ("Orange was not an imposter, there is 1 imposter remaining")
                print ("Green decides to watch the security cameras in the next round.")
                print ("Green watches Purple murder Red in the hallway.")
                print ("Green panics, and tries to leave the Security Room, when the door slams shut on him.")
                print ("Purple clamors out of the vent in the corner of the room and kills Green.")
                print ("There are no crewmates remaining. The imposter has won.")
                Imposters = Imposters - 1
    Imposters = Imposters - 1
   
