define s2 = Character("Sora", color="#e01919", image ="sora1",) #Male main character
define s3 = Character("Shiro",color="#fbf7f7", image="shiro1") #"Female main character"
define player_name = Character("[player]", color="#fbf7f7", image = "user_player")

#questions
define q1 = Character("[ques1]")
define q2 = Character("[ques2]")
define q3 = Character("[ques3]")
define q4 = Character("[ques4]")
define q5 = Character("[ques5]")
define q6 = Character("[ques6]")
define q7 = Character("[ques7]")
define q8 = Character("[ques8]")
define q9 = Character("[ques9]")

label start:
    show picture_01
    with dissolve
    "This game is about Sora who lost his sister, Shiro."
    "The only thing he can remember is that his sister has been taken away by unknown entities."
    "You and Sora is now set to search for her sister in an adventure filled with challenges and trials that will give him clue on the whereabouts of his sister."
    "REMINDER FROM THE CREATORS: PAY ATTENTION TO EVERY DETAILS TO WIN THIS GAME AND LASTLY ENJOY!!!"

    hide picture_01
    show picture_0
    with fade
    show shiro sad1
    show sora worry at right

    play music "audio/music3.mp3"

    s2 icon111 "Hello Sister. Your are late. What happenned?"
    s3 icon22 "Sorry Onii-san the Donut store is crowded that's why I'm late."
    s3 icon22 "and I feel I'm being followed so I go where there are full of people."

    hide shiro sad1
    hide sora worry at right

    show shiro happy1
    with dissolve
    show sora happy at right
    with dissolve

    s2 icon1 "Ah ok. It's alright shiro. "
    s2 icon1 "Let's just go to the View Deck and eat there because I'm starving."
    s3 icon2 "Ok Onii-chan."

    hide shiro happy1
    hide sora happy
    hide picture_0

    show picture_1
    with fade

    "30 minutes later..."
    show sora serious
    with dissolve

    s2 icon1111 "What happenned? why am I here at the View Deck?"
    s2 icon1111 "What are you looking at?"
    s2 icon1111 "Who are you? what is your name?"

    python:
        player = renpy.input("ENTER YOUR NAME:")#input the  player name here
        player = player.strip()

        if player == "":
            player = "Stultus"

    player_name icon3 "Sorry to disturb you and my name is [player_name]."

    hide sora serious
    with dissolve
    show sora happy

    s2 icon1 "Hello [player_name]."
    player_name "Is there a problem?"
    s2 icon1 "It just I can't remember anything after...."
    player_name "after.... what happen after?"

    hide sora happy
    with dissolve
    show sora worry

    s2 icon111 "I'm with my sister!!! she was here with me!!!"
    s2 icon111 "Where is my sister?"
    s2 icon111 "I need to find her!!!"
    s2 icon111 "Someone might have took her."

    hide sora worry
    with dissolve
    show sora sad

    player_name icon3 "Calm down Sora. Just breath."
    s2 icon11 "[player_name] help me find my sister. I really need your help."
    player_name  "Ok I'll help you, lets find your sister."
    player_name "Where we should go first?"
    s2 icon11"I dont know. I don't have any clue where we can find her."
    s2 icon11 "All I know is she was with me in here at the View deck."
    s2 icon11"what do you think [player_name] we should do first?"

    menu:
        "lets search this place first to find any clue.":
            jump search
        "Ask him what is the last thing he remember.":
            pass

    s2 icon11"I remember we are here and we are eating a donut that she bought in the town."
    s2 icon11 "and I can't remember what happen after that."
    hide sora sad
    hide picture_1
    jump remember

label search:

    hide picture_1
    show picture_5
    hide sora sad
    show sora sad at right
    with fade

    s2 icon11 "this is the place where we ate a donut."
    s2 icon11 "and I can't remember anything after that."
    s2 icon11"Do you see any clue [player_name]?"

    call screen findingDonut

label after:

    hide sora sad
    hide picture_5
    show picture_1
    show sora worry at right
    with fade

    player_name icon3 "Is this donut is yours??"
    s2 icon111 "Yes. My sister bought that Donut and we ate it in here."
    player_name icon3  "Do you remember what happened after you eat this Donut?"
    s2 icon111 "I can't remember anything after that. It's weird."

    jump remember

label remember:

    hide sora worry
    show picture_1
    show sora serious at right
    with dissolve

    player_name icon3 "are you saying that after you eat the donut, you can't remember what happened after that?"
    s2 icon1111 "Yes, It's weird. Do you think the Donut cause this?"

    menu:
        "Yes and I Think we should go to that Donut Store and to investigate also.":
            pass
        "I think it is impossible because someone should have alarm everyone about the food.":
            jump home1

    player_name icon3 "I think we should go to that Donut store to see it for ourself."
    s2 icon1111 "I don't know where is that Donut Store because my sister bought those donuts."
    player_name icon3 "do you have any idea how we can find that place?"
    s2 icon1111 "Yes, lets go to my home and we can search it to find where is that donut store."

    hide sora serious
    jump home2

label home1:

    hide sora serious
    show sora worry at right


    player_name icon3 "I think it is impossible."
    player_name icon3 "so lets just go to your house maybe your sister is there."
    s2 icon111 "Ok. You are right she might be there."

    jump home2

label home2:

    hide sora worry
    hide picture_1
    show picture_3
    with fade
    show sora sad

    s2 icon11 "This is our room and shiro isn't here."
    s2 icon11 "Where do you think she could be [player_name]?"
    player_name icon3 "wait what is that Sora?"
    player_name icon3 "I think there is something wrong with your computer."
    s2 icon11 "Where is it?"

    hide sora happy
    call screen warning

label message:

    show picture_4 at truecenter
    with fade

    player_name icon3 "What is wrong with your computer?"
    s2 icon111 "I don't know, I've never experience this before."

    hide picture_4
    call screen threat
    with fade

label clue:

    show picture_3
    show picture_6 at truecenter
    with fade

    "There is a letter in the 'TABLE' that will give you a clue for our demand. Find this place!!!"

    hide picture_6
    with fade
    show sora serious

    s2 icon1111 "We have to find that place."
    player_name icon3 "Yes Sora, we should go there and do you know where is that place Sora?"
    s2 icon1111 "I don't have any idea where is that place."
    player_name icon3 "That place is full of books and we need to guess a place of full of books."
    s2 icon1111 "Yes your right [player_name],What do you think is that place [player_name]?"

    call question1 from _call_question1

label question1:

    $ ques1 = renpy.input("Word start with L then six small letters: ")
    $ ques1 = ques1.strip()
    if (ques1 == "Library" or ques1 == "library"):
        pass
    else:
        call question1 from _call_question1_1

label place:

    hide sora serious
    with dissolve
    show sora happy

    s2 icon1 "You are right. That picture is the Library, that's why there are so many books there."
    player_name icon3 "OK We just need to find where is that place."
    player_name icon3 "Do you have any idea Sora about where is that place?"
    s2 icon1 "I don't know  but let's search it in the computer."
    s2 icon1 "We just need to open the map app in my computer and we can figure out where is that place."
    player_name icon3 "OK let's do it."

    hide sora happy
    hide picture_3
    call screen map1
    with fade

label map:

    call screen map
    with fade

label Library:

    show picture_7
    with fade
    show sora worry

    player_name icon3 "We are here and this is that place."
    s2 icon111 "We just have to find that letter in this place."
    player_name icon3 "Now is where is it?"
    s2 icon111 "I think they have said something on the message they have sent to us about where we could find those letter in here."

label question2:

    $ ques2 = renpy.input("where is the letter in the library?")

    if (ques2 == "table" or ques2 == "Table" or ques2 =="TABLE"):
        pass
    else:
        call question2 from _call_question2

    s2 icon111 "Yeah your right it is the table. Now we just need to go to that table."
    s2 icon11 "and look for a letter that they have written."
    hide sora worry
    hide picture_7
    call screen table

label Library1:

    show picture_8
    with dissolve

    player_name icon3 "There are so many papers in here."
    s2 icon111 "Now is which of this paper is that letter that will tell their demands."

    hide picture_8
    call screen letter

label quest1:

    show picture_8
    show picture_10 at truecenter
    with dissolve

    player_name icon3 "Why are they doing this? Sora this might be too difficult for you."
    s2 icon11 "[player_name], please help me. I need your help to find my sister."
    player_name icon3 "Ok so let's do this and we will find your sister."

    hide picture_10
    call screen letter1

label question3:

    show picture_9 at truecenter
    with dissolve

    s2 icon1111 "What is this?"
    player_name icon3 "I think it is a riddle."
    s2 icon1111 "Why is there a riddle? what is the meaning of this?"
    player_name icon3 "I think we need to decipher this riddle, it might give us a clue about where we can find your sister."
    s2 icon1111 "I don't know what is this, I need your help [player_name]."

label question:
    $ ques3 = renpy.input("What is the answer for the Riddle: ")
    if (ques3 == "bank" or ques3 == "Bank" or ques3 == "BANK"):
        pass
    else:
        call question from _call_question

    hide picture_9
    show picture_7
    show sora happy
    with dissolve

    s2 icon1 "Good Job [player_name]. So it is a Bank."
    player_name icon3 "Yes and I guess we need to go there because they might give us another clue."
    s2 icon1 "Ok [player_name], let's go to the Bank."

    hide sora happy
    hide picture_7
    call screen map2
    with fade

label quest11:

    hide picture_8
    show picture_11
    with dissolve
    show sora serious

    s2 icon1111 "I guess were here. But what are we going to do in here?"
    player_name icon3 "I think the riddle might give us another hint to guess what we should do in here."
    s2 icon1111 "'I have branches yet no leaves, no trunks and no fruits but people go to me to reap what they sow.' I wonder what is the other hint there?"
    player_name icon3 "We know that the riddle is pointing out the Bank and we are here now."
    player_name icon3 "but in where in the bank we will reap what we sow?"

    call question4 from _call_question4

label question4:

    $ ques4 = renpy.input("Where in the Bank we will reap what we sow? = A _ _")
    if (ques4 == "ATM"):
        pass
    else:
        call question4 from _call_question4_1
    hide sora serious
    show sora happy
    with dissolve

    s2 icon1 "So it is the ATM."
    player_name icon3 "And I think we need to go to that ATM."
    s2 icon1 "ok lets go to that ATM [player_name]"

    hide sora happy
    call screen atm

label ATM:
    hide picture_11
    show picture_12 at truecenter

    s2 icon111 "How do you think we can get the clue here?"

    hide picture_12
    show picture_13
    with dissolve

    s2 icon1 "Ow there we go. It is working now."

    hide picture_13
    show picture_14
    with dissolve

    s2 icon111 "What is this? There is something wrong in here"
    player_name icon3 "I don't have any idea what is wrong in this ATM."

    hide picture_14
    with dissolve
    call screen password

label question5:

    show picture_12 at truecenter
    with dissolve
    $ ques4 = renpy.input("What is the 9 digits password: _ _ _ _ _ _ _ _ _:")
    if (ques4 == "101000001"):
        call ATM2 from _call_ATM2
    else:
        pass

    "CLUE#1: password is in the recent 'LIBRARY TABLE'"

    $ ques6 = renpy.input("What is the password: _ _ _ _ _ _ _ _ _")
    if (ques6 == "101000001"):
        call ATM2 from _call_ATM2_1
    else:
        pass
    "CLUE#2: password is the 'BINARY OF 321.''"

    $ ques5 = renpy.input("What is the password: _ _ _ _ _ _ _ _ _")
    if (ques5 == "101000001"):
        call ATM2 from _call_ATM2_2
    else:
        call question5 from _call_question5

label ATM2:
    show picture_15 at truecenter
    s2 icon1 "I'm impress [player_name], I didn't expect you could still remember that."
    hide picture_12
    hide picture_15

    call screen reward2
    with dissolve


label bank2:

    show picture_11
    with dissolve
    show sora happy

    s2 icon1 "You have a good memory [player_name]."
    player_name icon3 "Let's open that clue if we have the rest of the clue so that we can focus on the task that will be given to us."
    s2 icon1 "Ok [player_name], now is let's wait for them to give us another hint for the other clues."
    player_name icon3 "Yes but let's go home for now they might send you another task."
    s2 icon1 "Ok [player_name], let's go home for now."


    hide picture_11
    hide sora happy
    show picture_16
    with dissolve
    show sora sad

    s2 icon11 "I wonder why are they doing this. I'm getting tired and I want to see my sister."
    player_name icon3 "Calm down Sora. Just take a deep breath and relax."
    player_name icon3 "Don't worry, we can do this and we will find your sister."

    hide sora sad
    show sora happy
    with dissolve

    s2 icon1 "Thank you [player_name]. Let's do our best to find Shiro."

    hide picture_16
    show picture_17
    with dissolve

    player_name icon3 "There are something wrong again with you computer Sora."
    s2 icon1111 "Ow man here we go again."
    hide sora happy
    with dissolve
    hide picture_17
    call screen task2

label task2:
    call screen letter2

label home3:
    show picture_16
    show sora serious
    with dissolve

    s2 icon1111 "I'm feeling nervous right now [player_name]."
    player_name icon3 "Don't worry sora if we can end this task we can finally see your sister."
    player_name icon3 "We just need to be ready and alert so that we can accomplish this task."
    s2 icon1111 "Yeah your right. Let's do this [player_name]."

    hide sora serious
    hide picture_16
    with dissolve
    show picture_19

    player_name icon3 "What it could be inside of that box?"
    s2 icon111 "I don't know [player_name]."
    s2 icon111 "But we have to go there and let's find out."
    player_name icon3 "Yeah your right. Let's now go there."

    hide picture_19
    call screen map3
    with dissolve

label treehouse1:
    show picture_20
    with dissolve

    s2 icon1111 "I guess we are here [player_name]."
    player_name icon3 "Yeah we are here and I guess we have to climb at that ladder."

    hide picture_20
    call screen treehouse

label treehouse2:
    call screen treehouse1

label treehouse3:
    show picture_21
    with dissolve

    player_name icon3 "This place is beautiful."
    s2 icon1 "Yes you are rigth [player_name]."
    s2 icon1 "I didn't know that this place is beautiful."
    player_name icon3 "Hey Sora, we need to focus."
    player_name icon3 "We have to find that box in here so that we can find you sister."
    player_name icon3 "Let's don't forget that we are doing this to find your sister."
    s2 icon11 "I'm sorry [player_name], so now where is that box?"

    hide picture_21
    call screen treehouse2
    with dissolve

label treehouse4:
    show picture_22
    with dissolve

    "You have to find all 8 FOLDERS that been scatter in the Sport Academy"
    "Every folder have a clue to find your sister."
    "In order for you to open is you need to find all the 8 folders that been scatter there."
    "Good Luck Sora."

    hide picture_22
    show picture_21
    with dissolve

    s2 icon111 "We have to go there [player_name]."
    player_name icon3 "Yes we shoudl go there to find those 8 Folders."
    player_name icon3 "But first we have to find where is that Sports Academy."
    s2 icon111 "I know where is that because me and my sister have study there."
    player_name icon3 "Ok lets now go there Sora."

    hide picture_21
    call screen map4
    with dissolve

label school1:
    show picture_23
    with dissolve
    show sora worry

    s2 icon111 "We are here now [player_name]."
    player_name icon3 "This school is huge."
    s2 icon111 "Yes you right this place is huge."
    s2 icon111 "How are we going to find those folders in here."
    player_name icon3 "I think this might be difficult because this place is huge."
    player_name icon3 "And those 8 folders have been scatter in this school."
    s2 icon111 "But we have to this, there is no other choice but to find those folders."
    player_name icon3 "Yeah there is no other choice so let's go."

    hide picture_23
    hide sora worry
    call screen school1
    with dissolve


#.................................................................................
label mainhall:
    show picture_24
    with dissolve
    show sora serious

    s2 icon1111 "[player_name] this is the Main Hall way."
    s2 icon1111 "Where do you think we should start [player_name]?"
    player_name icon3 "I think we should focus in this hall let's search all the rooms in here first."
    s2 icon1111 "Ok [player_name]."

    hide picture_24
    hide sora serious
    call screen mainhall
    with dissolve

label mainhall1:# without french folder
    call screen mainhall1

label mainhall2:
    call screen mainhall2

label mainhall3:
    show picture_24
    show sora happy
    with dissolve

    s2 icon1 "We have found 1st folder in here at the main hall way."
    s2 icon1 "So let's to go at the Right sub hall way."
    player_name icon3 "Where is that Right Sub hall way?"
    s2 icon1 "We just have to click the theater sign that is in here that pointing at the right."
    player_name icon3 "Ok Sora."

    hide sora happy
    hide picture_24
    call screen mainhall3
    with dissolve

label french:# with french folder
    call screen french
label one1:
    call screen one1
label two1:
    call screen two1
label three1:
    call screen three1
label french1:# without french folder
    show picture_25
    show sora happy
    with dissolve

    s2 icon1 "GoodJob [player_name]"
    s2 icon1 "We have found the first folder."
    player_name icon3 "Yes, now there are 7 folders left."
    player_name icon3 "Let's search again for the remaining folders."

    hide picture_25
    hide sora happy
    call screen french1
    with dissolve

label french2:
    call screen french1
label french3:
    call screen french2

label music:
    call screen music
label music1:
    call screen music1
label music2:
    call screen music2

label science:
    call screen science
label science1:
    call screen science1
label science2:
    call screen science1

#...............................................................................
label mainhall4:
    call screen mainhall4

label subhall1:
    show picture_26
    "YOU HAVE TO FIND THE SECOND FOLDER HERE."
    hide picture_26
    call screen subhall111
    with dissolve
label subhall111:
    call screen subhall111
label subhall11:
    show picture_26
    show sora happy

    s2 icon1 "We have found 2nd folder in here at the right sub hall way."
    s2 icon1 "So let's to go at the left sub hall way."
    player_name icon3 "Where is that Left Sub hall way?"
    s2 icon1 "We just to go to the main hallway and we have to click the restroom sign that is in there that pointing at the left."
    player_name icon3 "Ok Sora."

    hide picture_26
    hide sora happy
    call screen subhall11

label stage:
    call screen stage
label stage1:
    call screen stage1

label pe:
    call screen pe
label pe1:
    show picture_27
    show sora happy

    s2 icon1 "GoodJob [player_name]"
    s2 icon1 "We have found the second folder."
    player_name icon3 "Yes, now there are 6 folders left."
    player_name icon3 "Let's search again for the remaining folders."

    hide sora happy
    hide picture_27
    call screen pe1
    with dissolve

#..............................................................................
label subhall2:
    show picture_28
    "WE HAVE TO FIND THE FOLDERS HERE."
    hide picture_28
    call screen subhall22

label sub22:
    show picture_28
    "WE HAVE TO FIND THE FOlDERS HERE."
    hide picture_28
    call screen sub1
label boys:
    call screen boys
label boys1:
    call screen boys1
label boys2:
    call screen boys2
label boys3:
    call screen boys3
label boys4:
    call screen boys4
label sub1:
    call screen sub1
label subhall22:
    call screen subhall22
label subhall222:
    show picture_28
    show sora happy
    with dissolve

    s2 icon1 "We should go now to the 2nd floor because we have search the first floor very well."
    player_name icon3 "Ok Sora let's go now to the second floor."
    player_name icon3 "We might find the rest of the folders in there."
    hide sora happy
    hide picture_28
    call screen subhall222

label girls:
    call screen girls

label girls1:
    show picture_29
    show sora happy

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide sora happy
    hide picture_29
    call screen girls1

label girls2:
    call screen girls2

label girls3:
    show picture_29
    show sora happy

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide sora happy
    hide picture_29
    call screen girls3

label art11:
    call screen art11

label art1:
    show picture_30
    show sora happy

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide sora happy
    hide picture_30
    call screen art1
label sub2:
    call screen sub2
label art2:
    call screen art2

label art3:
    show picture_30
    show sora happy

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide sora happy
    hide picture_30
    call screen art3
#.................................................................................
label floor:
    call screen floor

label one:
    call screen one
label two:
    call screen two
label three:
    call screen three
label floor2:
    show picture_31
    with dissolve

    s2 icon1111 "We are now at the second floor [player_name]."
    player_name icon3 "They don't have much rooms in here compare to the first floor."
    s2 icon1111 "Yes you are right [player_name]."
    s2 icon1111 "Because the cafetria is in here at the second floor and the cafeteria here is huge."
    player_name icon3 "Ow ok, the might take all the free spaces here at the second floor thats why there are less rooms in here."
    s2 icon1111 "Yup, that's why there are less room in here than the first floor."
    player_name icon3 "Let's continue Sora on searching for the remaining folder."
    s2 icon1111 "How many remaining folders that we need to find [player_name]?"

    call question6 from _call_question6
label question6:
    $ ques7 = renpy.input("How many remaining folders? ")
    if (ques7 == "4" or ques7 == "four" or ques7 == "Four" or ques7 == "FOUR"):
        pass
    else:
        call question6 from _call_question6_1

    s2 icon1111 "So there are four remaining folders."
    player_name icon3 "Yup so let's continue our searching for the remaining folders."

    hide picture_31
    call screen floor222

label computer:
    call screen computer

label computer1:
    show picture_32

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide picture_32
    call screen computer1
label comp:
    call screen comp
label comp1:
    call screen comp1
label cafe:
    call screen cafe
label cafe1:
    call screen cafe1
label cafe2:
    call screen cafe2
label cafe3:
    call screen cafe3
label staff2:
    call screen staff2

label staff22:
    show picture_33
    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide picture_33
    call screen staff22

label floor222:
    call screen floor222

label staff1:
    call screen staff1

label staff11:
    show picture_33
    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide picture_33
    call screen staff11

label computer2:
    call screen computer2

label computer22:
    show picture_32

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide picture_32
    call screen computer22
label floor22:
    show picture_31
    with dissolve
    show sora happy

    s2 icon1 "We should go now to the third floor because we have search the second floor very well."
    s2 icon1 "Let's just go to that stair."
    player_name icon3 "Ok Sora let's go now to the third floor."
    player_name icon3 "We might find the rest of the folders in there."
    hide sora happy
    hide picture_31
    call screen floor22

#.................................................................................
label floor3:
    show picture_34
    show sora happy

    s2 icon1 "We are now here at the third floor [player_name]."
    s2 icon1 "Here is the office of the Professors and Principal in this school."
    player_name icon3 "Ok let's find the remaining two folders so that we can find your sister now."
    s2 icon1 "Yup you are right, let's finish this."

    hide sora happy
    hide picture_34
    call screen floor33
label floor33:
    call screen floor33
label prof1:
    call screen prof1

label prof2:
    call screen prof2
label prof222:
    call screen prof222
label prof22:
    show picture_35

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide picture_35
    call screen prof22
label prof2222:
    show picture_35

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."

    hide picture_35
    call screen prof2222

label prof11:
    call screen prof11
label prof111:
    call screen prof111
label prof3:
    call screen prof3

label prof4:
    call screen prof4

label prof5:
    call screen prof5

label prof33:
    call screen prof33
label prof333:
    call screen prof333

label prof44:
    call screen prof44
label prof444:
    call screen prof444

label floor0:
    call screen floor0
label floor00:
    call screen floor00

label prof55:
    show picture_36

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."

    hide picture_36
    call screen prof55

label prof555:
    call screen prof555

label prof5555:
    show picture_36

    s2 icon1 "GoodJob [player_name]."
    s2 icon1 "We have found a folder."
    player_name icon3 "Let's search again for the remaining folders."

    hide picture_36
    call screen prof5555

label schoolend:
    show picture_34

    "CONGRATS!!!!YOU HAVE FOUND ALL THE FOLDERS!!!"
    show sora happy

    s2 icon1 "GoodJob [player_name], thank you so much on helping me."
    s2 icon1 "We have found all the folders [player_name]."
    player_name icon3 "You are welcome Sora."
    player_name icon3 "Now is do we need to open that in here?"
    s2 icon1 "I don't know [player_name], where do you think we should open this?"
    player_name icon3 "Let's go to the park because we need to take a rest before we open those folders."
    s2 icon1 "Yeah you are right and I really need a rest too."
    player_name icon3 "Ok let's go now there."

    hide picture_34
    hide sora happy
    call screen map5
    with dissolve

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

label park:
    show picture_37
    show sora happy

    player_name icon3 "We are here now at the park, Sora."
    s2 icon1 "This place is beautiful."
    s2 icon1 "We can rest here peacefully."
    hide sora happy
    show sora sad
    with dissolve
    s2 icon11 "Do you think we can find my sister,[player_name]?"
    player_name icon3 "Of course Sora. Have trust in yourself."
    player_name icon3 "Trust me we can find your sister in no time."

    hide sora sad
    show sora happy
    with dissolve

    s2 icon1 "Thank you [player_name]."
    player_name icon3 "I guess we can now open those folders, right?"
    s2 icon1 "Ok [player_name], let's open them now."

    hide sora happy
    hide picture_37
    show picture_38

    s2 icon111 "What are this [player_name]?"
    s2 icon111 "What is the meaning of this?"
    player_name icon3 "It is a puzzle, this might be a another task to solve."
    player_name icon3 "To find the whereabouts of your sister."
    s2 icon111 "Help me [player_name]."

    hide picture_38
    call screen puzzle

label done:
    show picture_37
    show sora sad

    s2 icon11 "Good job at solving that puzzle."
    s2 icon11 "but what is that thing that you have solved [player_name]?"

    call question7 from _call_question7

label question7:
    $ ques8 = renpy.input("What it is called? T _ _ _ l _ r  ")
    if (ques8 == "Trailer"):
        pass
    else:
        call question7 from _call_question7_1

    hide sora sad
    show sora happy
    with dissolve
    s2 icon1 "Yeah you are right it is the trailer."
    s2 icon1 "But where is it [player_name]?"
    player_name icon3 "Let's just go to your house and let's search it in your map app."
    s2 icon1 "Yes you are right, let's go now."

    hide picture_37
    hide sora happy
    call screen home4
    with dissolve

label map6:
    call screen map6

label truck:
    show picture_39
    show sora worry

    s2 icon111 "We are here now [player_name]."
    player_name icon3 "Yeah we are here now, and at our right we can see the trailer in there."
    s2 icon111 "Let's check out that trailer first [player_name]."

    hide picture_39
    call screen truck1

label truck1:
    call screen truck2

label truck2:
    show picture_40

    s2 icon111 "There is no one in here [player_name]."
    player_name icon3 "Yes you are right. Let's check out the other house."
    hide picture_40
    call screen truck3

label barn:
    call screen barn

label end:
    call screen end
label end1:
    show picture_41
    show sora worry at right

    s2 icon111 "This might that place [player_name]."
    player_name icon3 "I think so too. This place is dangerous."
    s2 icon111 "Look [player_name] there are a underground floor."
    player_name icon3 "Ow yeah you are right. do you want to check it out Sora?"
    s2 icon111 "Let's go [player_name] my sister might be there and she would really need my help."
    player_name icon3 "Ok sora let's go."

    hide picture_41
    call screen end1
    with dissolve

label end2:
    show picture_42

    player_name icon3 "There is another way there."
    player_name icon3 "Let's check that place also."
    s2 icon1111 "Ok [player_name]."

    hide picture_42
    call screen end2
    with dissolve
label end3:
    show picture_43
    show shiro happy
    show sora happy at right

    s3 icon222 "Oni-channn, oh my god!!!"
    s3 icon222 "I knew you will find me!!!"
    s2 icon1 "At last my sister. I've miss you so much."
    s2 icon1 "how are you? are your hurt Shiro?"
    s3 icon222 "I'm fine Oni-chan, I'm just happy that you find me."
    player_name icon3 "Let's get out here first."
    player_name icon3 "Before someone would caught us."
    s2 icon1 "Ok [player_name]. let's go  shiro."

    hide sora happy
    hide shiro happy
    hide picture_43
    with dissolve
    call end4 from _call_end4

label end4:
    show picture_16
    show sora happy
    show shiro happy at right

    s2 icon1 "We are safe now, Thank to you [player_name]."
    s3 icon222 "Thank you very much [player_name]."
    s3 icon222 "I'm very thankful and glad that you helped my brother from the start."
    player_name icon3 "It is not problem, I'm also glad that you are safe."
    player_name icon3 "Are you going to report this to the police?"
    s2 icon1 "yes [player_name]. We will report this to the police."
    player_name icon3 "If you want I can go with you Sora."
    s2 icon1 "It's ok [player_name], you have done enough."
    s2 icon1 "And we are very thankful for helping me on finding my sister."
    player_name icon3 "You are very welcome Sora."
    s2 icon1 "BYEEEEEE [player_name]."
    s3 icon222 "BYEEEEE [player_name]."

    hide sora happy
    hide shiro happy
    hide picture_16
    with dissolve
    jump storyend
label storyend:
    show picture_01
    "<<<<<<<<<<<<<<<<<<THE END>>>>>>>>>>>>>>>>"
    return
