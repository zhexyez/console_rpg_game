# console_rpg_game
A small project to create an RPG Console Game

<b>Task</b>: create a game without any graphic library. Just a pure console and Python 3.<br/>
<b>Architecture</b>: gameme file which loads first screen and first map, checking whether it is new game or loading existing. As well listening to the user input and routing to the functions.<br/>
<b>Schema of the main loop</b>: <code>gameme -> user input -> check is next point avialable to interact with -> check is any interactions with objects -> do something if iteractions, otherwisejust move player to the next position -> draw points from the get_map_points -> user input -> ...</code><br/><br/>
<b>Functionality</b>:
<ul>
    <li>player stats</li>
    <li>inventory</li>
    <li>map switching</li>
    <li>next-to-the-door placement when map is changed</li>
    <li>memorization of interactions with the objects</li>
    <li>save game and then load saved</li>
</ul><br/>
<b>Features</b>:
<ul>
    <li>custom maps</li>
    <li>custom map namings</li>
    <li>custom story telling</li>
</ul>
