import time

def on_start(game):
    print "HOI"
    locations = ["the far corner of the room","the main stage","the Yacht stand"]

    players = game.players.keys()
    for player in players[:3]:
        objectives["entercode"].add_subobj(player)
        subobj = objectives['entercode'].subobj.index(player)        

        message = "Hello? Who is there? Is it you %s?" % player +  \
        "It is the facility supervisor here. \
We seem to have a problem with one of the valves that refrigerates the core reactor. You must go to \
%s to get the access code to the central computer.\
I will call you again when you are there." % locations[subobj]

        print message
        print
        print
        print
        game.players[player].send_voice(message)

def doorcode1_onstart(game):
    codes = ["1337", "6969", "1235"]
    user = objectives['entercode'].subobj[0]
    message =  "Hello again, are you allright? \
Damn, this is getting worse by the moment. \
I've got the access code right here remember it well. \
It is %s. Use it in the keypad of your device and you will receive additional instructions." % codes[0]

    game.players[user].send_voice(message)

def doorcode2_onstart(game):
    codes = ["1337", "6969", "1235"]
    user = objectives['entercode'].subobj[1]
    message =  "Hello again, are you allright? \
Damn, this is getting worse by the moment. \
I've got the access code right here remember it well. \
It is %s. Use it in the keypad of your device and you will receive additional instructions." % codes[1]

    game.players[user].send_voice(message)

def doorcode3_onstart(game):
    codes = ["1337", "6969", "1235"]
    user = objectives['entercode'].subobj[2]
    message =  "Hello again, are you allright? \
Damn, this is getting worse by the moment. \
I've got the access code right here remember it well. \
It is %s. Use it in the keypad of your device and you will receive additional instructions." % codes[2]

    game.players[user].send_voice(message)

def do_doorcode(obj, game, data):
    user = data['username']
    subobj = obj.subobj.index(user)

    def succes():
        game.add_objective("findcore")

    codes = ["1337", "6969", "1235"]
    clues = ["brown will probably not blow up the facility",
             "if yellow doesn't shut it down then green won't either",
             "the yellow cable doesn't seem active, I don't know about the red one though"
    ]


    message = str(user) + ", it is your supervisor again, the phone system has died. You must cut one of the wires of the central computer to restart the cooling system. But be careful, if you cut the wrong one the cooling system might blow up. I know that %s." % \
              clues[subobj]

    hints = ["Well done %s. Watch out when pulling wires, one of them locks up a pressure valve!! \
              It's probably not the yellow and the red ones. Or was it yellow and brown?.", 
             "Well done %s. You should pull one of the brighter wires to shut the reactor down.",
             "Well done %s. "]

    if data["code"] == codes[subobj]:
        # succes
        if obj.sub_complete(subobj):
            succes()
        game.players[user].send_text(message)
        # send hint
    else:
        # failed
        user.send_text("You failed to find the right code buddy.")

    if subobj == 0:
        obj.completed = True            
    elif subobj == 1:
        objectives['entercoded2'].completed = True
    elif subobj == 2:
        objectives['entercoded3'].completed = True


class Objective:
    def __init__(self, name, title, onstart = None, do = None, subobj = None):
        self.name = name
        self.title = title
        self.completed = False
        self.onstart = onstart
        self.do = do
        self.subobj = []
        self.subcompleted = []

    def start(self, game):
        if self.onstart:
            self.onstart(self, game)

    def try_complete(self, game, data):
        if self.do:
            return self.do(self, game, data)
        else:
            return "Look around you."

    def add_subobj(self, user):
        self.subobj.append(user)
        self.subcompleted.append(False)

    def sub_complete(self, index):
        self.subcompleted[index] = True
        print self.subcompleted
        print filter(lambda x: x!= True, self.subcompleted)
        return (len(filter(lambda x: x != True, self.subcompleted)) == 0)

    def toggle(self, value):
        self.completed = value

    def reset(self):
        self.toggle(False)
        self.subobj = []

objectives = {
    "entercode" : Objective("entercode", "Find the first code.", do = do_doorcode),
    "entercoded2" : Objective("entercoded2", "Find the second code."),
    "entercoded3" : Objective("entercoded3", "Find the third code."),
    "findcore" : Objective("findcore", "Find the reactor core.")
}

# timer state
class GameState:
    def __init__(self):
        self.started = False
        self.players = dict()

        self.won = False
        self.lost = False
        self.timer = Timer(self, 6 * 60)

        global objectives
        self.reset_objectives()

    def reset_objectives(self):
        self.objectives = []
        self.add_objective("entercode")
        self.add_objective("entercoded2")
        self.add_objective("entercoded3")

    # players
    def add_player(self, name, number):
        global players
        assert (number.isdigit() or
                (number[0] == '+' and number[1:].isdigit()))
        assert len(name) < 30
    
        if number.isdigit():
            self.players[name] = Player(name,number)   
        else:
            self.players[name] = Player(name,number[1:])  
        print ">> New Player:", name, number

    def get_players(self):
        return self.players.keys()

    def players_ready(self):
        if len(filter(lambda x: not x.ready, self.players.values())):
            return False
        else:
            return True

    def get_keypad(self, user):
        return self.players[user].hasarrived

    def set_keypad(self, user, value):
        self.players[user].hasarrived = value

    # objectives
    def add_objective(self, name):
        global objectives
        self.objectives.append(objectives[name])
        objectives[name].start(self)
        return objectives[name]

    def get_objective(self, name):
        objs = filter(lambda x: x.name == name, self.objectives)
        if objs:
            return objs[0]
        else:
            return None

    # control
    def start(self):
        self.timer.running = True
        self.started = True
        on_start(self)

    def stop(self):
        self.timer.running = False
        self.started = True

    def reset(self):
        self.players = dict()

        self.timer.reset()

        self.won = False
        self.lost = False
        self.started = False
        
        self.reset_objectives()
        global objectives
        for objective in objectives.values():
            objective.reset()

    # win conditions
    def win(self):
        self.started = False
        self.won = True

    def lose(self):
        self.started = False
        self.won = True

class Timer:
    def __init__(self, game, time):
        self.game = game
        self.start_time = time
        self.reset()

    def reset(self):
        self.running = False
        self.speed = 1000
        self.delta_time = 0

    def is_running(self):
        return self.running

    def set_speed(self, speed):
        self.speed = float(speed)

    def get_speed(self):
        return self.speed

    def set_delta_time(self, dt):
        self.delta_time = int(dt)

    def get_delta_time(self):
        dt = self.delta_time
        self.delta_time = 0
        return dt

    def alert(self):
        print "GAME OVER!"
        self.running = False
        self.game.lost = True

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.ready = False
        self.hasarrived = False

    def set_ready():
        self.ready = True

    def send_voice(self, message):
        from balance_test import send_voice_message
        if message.find('%s') == -1:
            return send_voice_message(self.number, message)
        else:
            return send_voice_message(self.number, message % self.name)
        
    def send_text(self, message):
        from balance_test import send_text_message
        if message.find('%s') == -1:
            return send_text_message(self.number, message)
        else:
            return send_text_message(self.number, message % self.name)
