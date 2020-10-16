# Team Notes
Try to check this document whenever you start working on the project to see any notes we need to share with each other. We used this project template for the warmup project and it worked really well as we used it alongside Trello. -JH

BS = Ben Sylvester
JH = Jackson Hall
JM = Jordan Marchese
PS = Parker Sawbridge

## Announcements for Everyone
Post notes here that everyone should see and try to check it whenever you start working. Put your initials in the "(seen by: <initials>)" when you read each thing.

###### Note - just do 1. before every list item and it wil auto number

1. It seemed like we agreed on repl.it for development so [here's a link](https://repl.it/@jackson_hall/CS205-Final-Project#TeamNotes.md) to where the project will be. Make sure to go into settings on the left and change `Indent size` to 4 and `Indent type` to spaces since Python can error out when mixing spaces and tabs. It's so much easier to set this up from the beginning -JH (seen by: PS BS )
1. Jason said in his notes on our warmup project we should have followed [pep8](https://www.python.org/dev/peps/pep-0008/) Python formatting and use snake_case for vars and functions, and CapWords for classes -JH (seen by: PS BS)
1. I try to keep classes organized into these sections so just dropping them here to copy-paste when we make new classes -JH (seen by: PS BS)
  ```
  class ClassName:
      ''' ========== Constant Class Variables ========== '''
      ''' ========== Regular Class Variables ========== '''
      ''' ========== Constructor ========== '''
      def __init__(self):
          pass
      ''' ========== Magic Methods ========== '''
      ''' ========== Static Methods ========== '''
      ''' ========== Instance Methods ========== '''
  ```
1. Github changed their default branch name from master to main, so now if you do git commands like "git pull/push origin master" on the repo just make sure to change "master" to "main" wherever it comes up. Repl.it also has builtin git support on the left sidebar so we shouldn't have to do that unless we are testing something on a local copy -JH (seen by: PS BS)
1. Just remembered Jason said not to commit to master (main) branch for this project so maybe let's make GUI and backend branches next time we work -JH (seen by: )

## Messages
Other messages for specific people can go here.

1. BS, JM, PS: Yooo here's an example message -JH (seen by: )
1. JH, BS, PS: Yooo here's an example reply -JM (seen by: JH)


## Resources
#### To Do
- [Trello Board](https://trello.com/invite/b/sMzGchBf/a4ef900d6968ac4c0c88568dd14a20ef/cs-205-othello)

#### Ideas

#### Notes
- Class hierarchy: Game has a Board, Board has a 2d list of Tiles, Tile has an optional GamePiece (optionals don't exist in Python but can either be a GamePiece object or `None`, we can just check if the element is `None` wherever we need to). All of these classes can become GUI elements so they should all implement some sort of `display(position_on_screen)` method for Pygame or whatever we use to be able to draw it

#### Links
- Play Othello online: https://www.eothello.com/
- Openings guide: http://www.soongsky.com/othello/en/strategy2/ch11.php
- WZebra move evaluation engine: http://www.radagast.se/othello/download.html
- Trello: https://trello.com/b/sMzGchBf/cs-205-othello