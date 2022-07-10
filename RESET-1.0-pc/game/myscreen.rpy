screen map():
    imagemap:
        ground "map1"
        text "CLICK your desire destination."
        hotspot(1315, 463, 246, 141)action Call("Library")

screen map1():
    imagemap:
        ground "home1.png"
        text "CLICK the Computer."
        hotspot(728, 423, 329, 314)action Call("map")

screen map2():
    imagemap:
        ground "map1"
        hotspot(1336, 298, 188, 138)action Call("quest11")


screen findingDonut():
    imagemap:
        ground "findingDonut.png"
        text "FIND then CLICK the Clue."
        hotspot(131, 916, 61, 81)action Call("after")

screen warning():
    imagemap:
        ground "warning.png"
        text "CLICK the Warning Sign."
        hotspot(812, 424, 201, 90)action Call("message")

screen threat():
    imagemap:
        ground "threat.png"
        hotspot(1016, 768, 184, 36)action Call("clue")

screen table():
    imagemap:
        ground "clue1.jpg"
        hotspot(937, 632, 520, 261)action Call("Library1")

screen letter():
    imagemap:
        ground "letter.png"
        text "Find the Letter for Sora."
        hotspot(272, 233, 68, 42)action Call("quest1")
        hotspot(274, 275, 32, 15)action Call("quest1")
        hotspot(308, 278, 26, 10)action Call("quest1")
        hotspot(278, 300, 22, 68)action Call("quest1")
        hotspot(301, 332, 21, 34)action Call("quest1")

screen letter1():
    imagemap:
        ground "quest1.png" at truecenter
        hotspot(647, 929, 87, 39)action Call("question3")

screen atm():
    imagemap:
        ground "bank.png"
        hotspot(202, 642, 170, 332)action Call("ATM")

screen password():
    imagemap:
        ground "letter1.png" at truecenter
        hotspot(318, 727, 334, 57)action Call("question5")

screen reward2():
    imagemap:
        ground "reward2.png" at truecenter
        hotspot(421, 471, 109, 51) action Call("bank2")

screen task2():
    imagemap:
        ground "home.png"
        text "CLICK the Computer."
        hotspot(731, 423, 355, 318)action Call("task2")

screen letter2():
    imagemap:
        ground "letter2.1.png"
        hotspot(805, 711, 297, 73)action Call("home3")

screen map3():
    imagemap:
        ground "map1.png"
        text "FIND THE TREEHOUSE."
        hotspot(1441, 702, 234, 128)action Call("treehouse1")

screen treehouse():
    imagemap:
        ground "treehouse0.jpg"
        hotspot(1007, 627, 87, 310)action Call("treehouse2")

screen treehouse1():
    imagemap:
        ground "treehouse1.jpg"
        hotspot(934, 56, 186, 120)action Call("treehouse3")

screen treehouse2():
    imagemap:
        ground "treehouse2.jpg"
        hotspot(48, 953, 299, 84)action Call("treehouse4")

screen map4():
    imagemap:
        ground "map1.png"
        hotspot(784, 325, 377, 289)action Call("school1")



#....................task in sport academy..................
screen school1():
    imagemap:
        ground "school1.jpg"
        hotspot(830, 457, 344, 237)action Call("mainhall")

screen mainhall():
    imagemap:
        ground "school2.jpg"
        hotspot(1598, 270, 242, 642)action Call("french")
        hotspot(1151, 606, 78, 211)action Call("music")
        hotspot(689, 596, 66, 218)action Call("science")

screen mainhall1():
    imagemap:
        ground "school2.jpg"
        hotspot(1598, 270, 242, 642)action Call("french")
        hotspot(1151, 606, 78, 211)action Call("music")
        hotspot(689, 596, 66, 218)action Call("science")

screen mainhall2():
    imagemap:
        ground "school2.jpg"
        hotspot(1598, 270, 242, 642)action Call("french2")
        hotspot(1151, 606, 78, 211)action Call("music1")
        hotspot(689, 596, 66, 218)action Call("science1")

screen mainhall3():
    imagemap:
        ground "school2.jpg"
        hotspot(1598, 270, 242, 642)action Call("french2")
        hotspot(1151, 606, 78, 211)action Call("music1")
        hotspot(689, 596, 66, 218)action Call("science1")
        hotspot(1290, 321, 210, 77)action Call("subhall1")

screen mainhall4():
    imagemap:
        ground "school2.jpg"
        hotspot(420, 322, 205, 65)action Call("subhall2")
        hotspot(1598, 270, 242, 642)action Call("one1")
        hotspot(1151, 606, 78, 211)action Call("two1")
        hotspot(689, 596, 66, 218)action Call("three1")

screen one1():
    imagemap:
        ground "school3.jpg"
        hotspot(737, 398, 172, 364)action Call("mainhall4")
screen two1():
    imagemap:
        ground "school4.jpg"
        hotspot(783, 429, 151, 320)action Call("mainhall4")
screen three1():
    imagemap:
        ground "school5.jpg"
        hotspot(770, 390, 183, 360)action Call("mainhall4")


screen french():
    imagemap:
        ground "schoolfolder3.jpg"
        hotspot(815, 768, 133, 28)action Call("french1")
        hotspot(734, 398, 169, 357)action Call("mainhall1")
screen french1():
    imagemap:
        ground "school3.jpg"
        hotspot(737, 398, 172, 364)action Call("mainhall3")

screen french2():
    imagemap:
        ground "school3.jpg"
        hotspot(737, 398, 172, 364)action Call("mainhall4")

screen music():
    imagemap:
        ground "school4.jpg"
        hotspot(783, 429, 151, 320)action Call("mainhall1")
screen music1():
    imagemap:
        ground "school4.jpg"
        hotspot(783, 429, 151, 320)action Call("mainhall3")

screen music2():
    imagemap:
        ground "school4.jpg"
        hotspot(783, 429, 151, 320)action Call("mainhall4")

screen science():
    imagemap:
        ground "school5.jpg"
        hotspot(770, 390, 183, 360)action Call("mainhall1")
screen science1():
    imagemap:
        ground "school5.jpg"
        hotspot(770, 390, 183, 360)action Call("mainhall3")
screen science2():
    imagemap:
        ground "school5.jpg"
        hotspot(770, 390, 183, 360)action Call("mainhall4")

#.....................................................................................
screen subhall1():
    imagemap:
        ground "school10.jpg"
        hotspot(786, 925, 315, 67)action Call("subhall1")
        hotspot(1294, 554, 116, 274)action Call("stage")
        hotspot(591, 564, 86, 250)action Call("pe")

screen subhall111():
    imagemap:
        ground "school10.jpg"
        hotspot(786, 925, 315, 67)action Call("subhall1")
        hotspot(1294, 554, 116, 274)action Call("stage")
        hotspot(591, 564, 86, 250)action Call("pe")

screen subhall11():#without pe folder
    imagemap:
        ground "school10.jpg"
        hotspot(786, 925, 315, 67)action Call("mainhall4")
        hotspot(1294, 554, 116, 274)action Call("stage1")
        hotspot(591, 564, 86, 250)action Call("pe1")

screen pe():
    imagemap:
        ground "schoolfolder5.jpg"
        hotspot(815, 942, 282, 68)action Call("subhall111")
        hotspot(1670, 875, 105, 135)action Call("pe1")

screen pe1():
    imagemap:
        ground "school12.jpg"
        hotspot(788, 958, 267, 66)action Call("subhall11")

screen stage():
    imagemap:
        ground "school11.jpg"
        hotspot(1436, 497, 162, 182)action Call("subhall111")

screen stage1():
    imagemap:
        ground "school11.jpg"
        hotspot(1436, 497, 162, 182)action Call("subhall11")


#...............................................................................
screen subhall2():
    imagemap:
        ground "school6.jpg"
        hotspot(736, 942, 361, 60)action Call("subhall2")
        hotspot(473, 458, 115, 360)action Call("girls")
        hotspot(1250, 496, 117, 350)action Call("boys")
        hotspot(1639, 358, 186, 584)action Call("art2")
screen boys():
    imagemap:
        ground "school8"
        hotspot(765, 917, 371, 98)action Call("subhall2")

screen boys1():
    imagemap:
        ground "school8"
        hotspot(765, 917, 371, 98)action Call("subhall22")
screen boys3():
    imagemap:
        ground "school8"
        hotspot(765, 917, 371, 98)action Call("subhall222")
screen subhall22():
    imagemap:
        ground "school6.jpg"
        hotspot(736, 942, 361, 60)action Call("subhall2")
        hotspot(473, 458, 115, 360)action Call("girls")
        hotspot(1250, 496, 117, 350)action Call("boys1")
        hotspot(1639, 358, 186, 584)action Call("art2")

screen subhall222():
    imagemap:
        ground "school6.jpg"
        hotspot(736, 942, 361, 60)action Call("floor")
        hotspot(473, 458, 115, 360)action Call("girls1")
        hotspot(1250, 496, 117, 350)action Call("boys3")
        hotspot(1639, 358, 186, 584)action Call("art1")
screen sub1():
    imagemap:
        ground "school6.jpg"
        hotspot(736, 942, 361, 60)action Call("sub1")
        hotspot(473, 458, 115, 360)action Call("girls1")
        hotspot(1250, 496, 117, 350)action Call("boys2")
        hotspot(1639, 358, 186, 584)action Call("art11")
screen boys2():
    imagemap:
        ground "school8"
        hotspot(765, 917, 371, 98)action Call("sub1")
screen boys1():
    imagemap:
        ground "school8"
        hotspot(765, 917, 371, 98)action Call("subhall22")
screen girls():
    imagemap:
        ground "schoolfolder7.jpg"
        hotspot(1397, 927, 161, 75)action Call("girls1")
        hotspot(1412, 432, 444, 362)action Call("subhall22")

screen girls1():
    imagemap:
        ground "school9.jpg"
        hotspot(1410, 434, 443, 363)action Call("sub1")

screen art11():
    imagemap:
        ground "schoolfolder4.jpg"
        hotspot(1216, 893, 183, 70)action Call("art1")
        hotspot(817, 402, 167, 347)action Call("sub1")

screen art1():
    imagemap:
        ground "school7.jpg"
        hotspot(822, 411, 160, 333)action Call("subhall222")
#............................................................................
screen sub2():
    imagemap:
        ground "school6.jpg"
        hotspot(736, 942, 361, 60)action Call("sub2")
        hotspot(473, 458, 115, 360)action Call("girls2")
        hotspot(1250, 496, 117, 350)action Call("boys4")
        hotspot(1639, 358, 186, 584)action Call("art3")
screen boys4():
    imagemap:
        ground "school8"
        hotspot(765, 917, 371, 98)action Call("sub2")
screen art2():
    imagemap:
        ground "schoolfolder4.jpg"
        hotspot(1216, 893, 183, 70)action Call("art3")
        hotspot(817, 402, 167, 347)action Call("subhall22")
screen art3():
    imagemap:
        ground "school7.jpg"
        hotspot(822, 411, 160, 333)action Call("sub2")


screen girls2():
    imagemap:
        ground "schoolfolder7.jpg"
        hotspot(1397, 927, 161, 75)action Call("girls3")
        hotspot(1412, 432, 444, 362)action Call("sub2")

screen girls3():
    imagemap:
        ground "school9.jpg"
        hotspot(1410, 434, 443, 363)action Call("subhall222")

#.................................................................................
screen floor():
    imagemap:
        ground "school2.jpg"
        hotspot(1598, 270, 242, 642)action Call("one")
        hotspot(1151, 606, 78, 211)action Call("two")
        hotspot(689, 596, 66, 218)action Call("three")
        hotspot(1253, 564, 58, 263)action Call("floor2")
        hotspot(1164, 481, 102, 28)action Call("floor2")

screen one():
    imagemap:
        ground "school3.jpg"
        hotspot(737, 398, 172, 364)action Call("floor")
screen two():
    imagemap:
        ground "school4.jpg"
        hotspot(783, 429, 151, 320)action Call("floor")
screen three():
    imagemap:
        ground "school5.jpg"
        hotspot(770, 390, 183, 360)action Call("floor")

screen floor2():
    imagemap:
        ground "school13.jpg"
        hotspot(901, 478, 159, 383)action Call("computer")
        hotspot(1164, 528, 250, 294)action Call("cafe")
        hotspot(1624, 570, 164, 245)action Call("staff1")
screen floor222():
        imagemap:
            ground "school13.jpg"
            hotspot(901, 478, 159, 383)action Call("computer")
            hotspot(1164, 528, 250, 294)action Call("cafe")
            hotspot(1624, 570, 164, 245)action Call("staff1")
screen floor22():
    imagemap:
        ground "school13.jpg"
        hotspot(901, 478, 159, 383)action Call("computer22")
        hotspot(1164, 528, 250, 294)action Call("cafe3")
        hotspot(1624, 570, 164, 245)action Call("staff22")
        hotspot(34, 614, 272, 284)action Call("floor3")

screen cafe3():
    imagemap:
        ground "school15.jpg"
        hotspot(804, 958, 287, 79)action Call("floor22")
screen cafe():
    imagemap:
        ground "school15.jpg"
        hotspot(804, 958, 287, 79)action Call("floor222")

screen computer():
    imagemap:
        ground "schoolfolder8.jpg"
        hotspot(1542, 804, 81, 73)action Call("computer1")
        hotspot(32, 420, 198, 332)action Call("floor222")

screen computer1():
    imagemap:
        ground "school14"
        hotspot(38, 416, 182, 342)action Call("comp")
screen comp():
        imagemap:
            ground "school13.jpg"
            hotspot(901, 478, 159, 383)action Call("computer1")
            hotspot(1164, 528, 250, 294)action Call("cafe1")
            hotspot(1624, 570, 164, 245)action Call("staff2")
screen cafe1():
    imagemap:
        ground "school15.jpg"
        hotspot(804, 958, 287, 79)action Call("comp")
screen staff2():
    imagemap:
        ground "schoolfolder1.jpg"
        hotspot(1548, 771, 88, 93)action Call("staff22")
        hotspot(134, 330, 182, 589)action Call("comp")
screen staff22():
    imagemap:
        ground "school16.jpg"
        hotspot(134, 330, 182, 589)action Call("floor22")

screen comp1():
        imagemap:
            ground "school13.jpg"
            hotspot(901, 478, 159, 383)action Call("computer2")
            hotspot(1164, 528, 250, 294)action Call("cafe2")
            hotspot(1624, 570, 164, 245)action Call("staff1")

screen cafe2():
    imagemap:
        ground "school15.jpg"
        hotspot(804, 958, 287, 79)action Call("comp1")

screen staff1():
    imagemap:
        ground "schoolfolder1.jpg"
        hotspot(1548, 771, 88, 93)action Call("staff11")
        hotspot(134, 330, 182, 589)action Call("floor222")

screen staff11():
    imagemap:
        ground "school16.jpg"
        hotspot(134, 330, 182, 589)action Call("comp1")
screen computer2():
    imagemap:
        ground "schoolfolder8.jpg"
        hotspot(1542, 804, 81, 73)action Call("computer22")
        hotspot(32, 420, 198, 332)action Call("comp1")

screen computer22():
    imagemap:
        ground "school14"
        hotspot(38, 416, 182, 342)action Call("floor22")


#.................................................................................
screen floor3():
    imagemap:
        ground "school17.jpg"
        hotspot(538, 392, 220, 495)action Call("prof1")
        hotspot(867, 470, 177, 389)action Call("prof2")#
        hotspot(1114, 520, 150, 308)action Call("prof3")
        hotspot(1324, 565, 111, 257)action Call("prof4")
        hotspot(1632, 580, 138, 237)action Call("prof555")#

screen floor33():
    imagemap:
        ground "school17.jpg"
        hotspot(538, 392, 220, 495)action Call("prof1")
        hotspot(867, 470, 177, 389)action Call("prof2")#
        hotspot(1114, 520, 150, 308)action Call("prof3")
        hotspot(1324, 565, 111, 257)action Call("prof4")
        hotspot(1632, 580, 138, 237)action Call("prof555")#

screen prof1():
    imagemap:
        ground "school18.jpg"
        hotspot(807, 930, 273, 98)action Call("floor33")

screen prof3():
    imagemap:
        ground "school20.jpg"
        hotspot(854, 917, 274, 85)action Call("floor33")
screen prof4():
    imagemap:
        ground "school20.jpg"
        hotspot(843, 953, 271, 67)action Call("floor33")

screen floor0():
    imagemap:
        ground "school17.jpg"
        hotspot(538, 392, 220, 495)action Call("prof11")
        hotspot(867, 470, 177, 389)action Call("prof22")#
        hotspot(1114, 520, 150, 308)action Call("prof33")
        hotspot(1324, 565, 111, 257)action Call("prof44")
        hotspot(1632, 580, 138, 237)action Call("prof5")#
screen prof11():
    imagemap:
        ground "school18.jpg"
        hotspot(807, 930, 273, 98)action Call("floor0")

screen prof33():
    imagemap:
        ground "school20.jpg"
        hotspot(854, 917, 274, 85)action Call("floor0")
screen prof44():
    imagemap:
        ground "school20.jpg"
        hotspot(843, 953, 271, 67)action Call("floor0")
screen prof2():
    imagemap:
        ground "schoolfolder2.jpg"
        hotspot(575, 841, 101, 50)action Call("prof22")
        hotspot(856, 958, 240, 62)action Call("floor33")
screen prof22():
    imagemap:
        ground "school19.jpg"
        hotspot(864, 955, 263, 79)action Call("floor0")
screen prof5():
    imagemap:
        ground "schoolfolder6.jpg"
        hotspot(173, 789, 204, 60)action Call("prof55")
        hotspot(744, 932, 319, 70)action Call("floor0")
screen prof55():
    imagemap:
        ground "school22.jpg"
        hotspot(760, 888, 302, 97)action Call("schoolend")

screen floor00():
    imagemap:
        ground "school17.jpg"
        hotspot(538, 392, 220, 495)action Call("prof111")
        hotspot(867, 470, 177, 389)action Call("prof222")#
        hotspot(1114, 520, 150, 308)action Call("prof333")
        hotspot(1324, 565, 111, 257)action Call("prof444")
        hotspot(1632, 580, 138, 237)action Call("prof5555")#
screen prof111():
    imagemap:
        ground "school18.jpg"
        hotspot(807, 930, 273, 98)action Call("floor00")

screen prof333():
    imagemap:
        ground "school20.jpg"
        hotspot(854, 917, 274, 85)action Call("floor00")
screen prof444():
    imagemap:
        ground "school20.jpg"
        hotspot(843, 953, 271, 67)action Call("floor00")
screen prof555():
    imagemap:
        ground "schoolfolder6.jpg"
        hotspot(173, 789, 204, 60)action Call("prof5555")
        hotspot(744, 932, 319, 70)action Call("floor33")
screen prof5555():
    imagemap:
        ground "school22.jpg"
        hotspot(760, 888, 302, 97)action Call("floor00")
screen prof222():
    imagemap:
        ground "schoolfolder2.jpg"
        hotspot(575, 841, 101, 50)action Call("prof2222")
        hotspot(856, 958, 240, 62)action Call("floor00")
screen prof2222():
    imagemap:
        ground "school19.jpg"
        hotspot(864, 955, 263, 79)action Call("schoolend")

 #>>>>>>>........................................<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
screen map5():
    imagemap:
        ground "map1.png"
        text "FIND THE PARK."
        hotspot(518, 220, 242, 161)action Call("park")

screen puzzle():
    add "park3.png"

    drag:
        as carmen
        draggable True
        xpos 1600 ypos 750
        frame:
            style "empty"
            background "puzzle1.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 360, 225, 3.0)
    drag:
        as carmen
        draggable True
        xpos 1200 ypos 750
        frame:
            style "empty"
            background "puzzle2.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 627, 230, 3.0)
    drag:
        as carmen
        draggable True
        xpos 850 ypos 750
        frame:
            style "empty"
            background "puzzle3.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 900, 215, 3.0)
    drag:
        as carmen
        draggable True
        xpos 300 ypos 750
        frame:
            style "empty"
            background "puzzle4.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 1180, 230, 3.0)
    drag:
        as carmen
        draggable True
        xpos 400 ypos 20
        frame:
            style "empty"
            background "puzzle5.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 350, 500, 3.0)
    drag:
        as carmen
        draggable True
        xpos 900 ypos 20
        frame:
            style "empty"
            background "puzzle6.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 615, 500, 3.0)
    drag:
        as carmen
        draggable True
        xpos 1600 ypos 20
        frame:
            style "empty"
            background "puzzle7.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 890, 490, 3.0)
    drag:
        as carmen
        draggable True
        xpos 100 ypos 20
        frame:
            style "empty"
            background "puzzle8.png"
            xysize (100, 100)

            vbox:
                textbutton "Move" action Function(carmen.snap, 1160, 500, 3.0)
    drag:
        as carmen
        draggable False
        xpos 820 ypos 998
        frame:
            background "done.png"
            xysize (50, 20)

            vbox:
                textbutton " Done" action Jump("done")
screen home4():
    imagemap:
        ground "home1.png"
        hotspot(812, 418, 212, 349)action Call("map6")
screen map6():
    imagemap:
        ground "map1.png"
        hotspot(8, 410, 110, 139)action Call("truck")

screen truck1():
    imagemap:
        ground "last1.jpeg"
        hotspot(1344, 583, 527, 177)action Call("truck1")
screen truck2():
    imagemap:
        ground "van.png"
        hotspot(1483, 377, 153, 453)action Call("truck2")
screen truck3():
    imagemap:
        ground "last2.jpg"
        hotspot(14, 3, 195, 1065)action Call("barn")
screen barn():
    imagemap:
        ground "last1.jpeg"
        hotspot(37, 512, 342, 237)action Call("end")

screen end():
    imagemap:
        ground "last5.jpg"
        hotspot(831, 590, 171, 272)action Call("end1")
screen end1():
    imagemap:
        ground "last7.jpg"
        hotspot(238, 828, 561, 247)action Call("end2")
screen end2():
    imagemap:
        ground "last8.jpg"
        hotspot(1555, 377, 176, 315)action Call("end3")
