# Treasure Hunt
Treasure Hunt is a  hybrid mobile app game developed during the 24 hour FuseHack Hackathon. The prototype was written in collaboration with Okke van Garderen, Jaap Wijnen, Rick Hutten, and Gael le Mignot. The app won two prizes, being Overall Most Creative and Best Use of API.

In this multiplayer game, players form a team after which they must each travel to different locations to solve puzzles and clues, with each completed task granting more chance of dismantling the ticking time bomb that awaits them before it explodes. All orders and clues are given through automated, personalized, calls using Messagebird's API. After the participating players have chosen a storyline to follow, the game starts by calling each player within a set time period and guiding them to their first location, at which a puzzle must be solved to receive the next clue concerning the bomb. The entire app was written during the 24 hour lasting event, and code was uploaded to github without further modification or commenting (except for removal of test keys). Keep in mind that this is solely a quick, albeit functioning, prototype.

### Implementation
The backend is written in python and ran locally on a laptop during the hackathon, with localtunnel facilitating the connections. The hybrid iphone and android apps were written using the Ionic framework, utilizing the MessageBird API for contacting contenders during the game. The time bomb ran on a display connected to a Raspberry Pi.

