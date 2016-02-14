import flask

from crossserver import *
from gamefuncs import *

app = flask.Flask(__name__)
game = GameState()

def page(path):
    global app
    def wrapper(f):
        app.route(path, methods = ['OPTIONS', 'POST', 'GET'])(
            appconnection(f))
    return wrapper

@page('/')
def hello_world(data, result):
    return 'Game Server!'

# player
@page('/add_player')
def page_add_player(data, result):
    game.add_player(data['username'], data['phonenumber'])
    result["players"] = game.get_players()

@page('/player_ready')
def page_player_ready(data, result):
    game.players[data['username']].ready()

    if game.players_ready():
        game.start()

@page('/player_list')
def page_player_list(data, result):
    result["players"] = game.get_players()

# objectives
@page('/objectives')
def page_objectives(data, result):
    objs = []
    for obj in game.objectives:
        objs.append({"title" : obj.title,
                     "completed" : obj.completed})
    
    result["objectives"] = objs

    result["available"] = game.get_keypad(data['username'])
    game.set_keypad(data['username'], False)


@page('/try_objective')
def page_try_objective(data, result):
    obj = data["objective"]
    print obj
    obj = objectives[obj]
    print obj
    result["message"] = obj.try_complete(game, data)
    result["completed"] = obj.completed
    print result

# control
@page('/reset_game')
def page_reset_game(data, result):
    game.reset()

@page('/start_game')
def page_start_game(data, result):
    game.start()

@page('/game_info')
def page_game_info(data, result):
    result["started"] = game.started

@page('/keypad')
def page_keypad(data, result):
    result["available"] = game.get_keypad(data['username'])
    game.set_keypad(data['username'], False)

@page('/activate_a')
def page_activate_a(data, result):
    print objectives["entercode"].subobj
    game.players[objectives["entercode"].subobj[0]].hasarrived = True
    doorcode1_onstart(game)

@page('/activate_b')
def page_activate_b(data, result):
    game.players[objectives["entercode"].subobj[1]].hasarrived = True
    doorcode2_onstart(game)

@page('/activate_c')
def page_activate_c(data, result):
    game.players[objectives["entercode"].subobj[2]].hasarrived = True
    doorcode3_onstart(game)

@page('/send_voice')
def page_send_voice(data, result):
    print game.players['Okke'].send_voice("Hallo %s.")

@page('/send_text')
def page_send_text(data, result):
    print game.players['Okke'].send_text("Hallo %s.")

# timer interaction
@page('/timer_info')
def page_delta_time(data, result):
    print data.keys()

    result["start_time"] = game.timer.start_time
    result["delta_time"] = game.timer.get_delta_time()
    result["timer_speed"] = game.timer.get_speed()
    result["started"] = game.timer.is_running()
    result["lost"] = game.lost
    result["winner"] = game.won

@page('/fuck_shit_up')
def page_fuck_shit_up(data, result):
    game.timer.set_speed(100)
    game.timer.set_delta_time(33 * 60)
    result["timer_speed"] = game.timer.get_speed()

@page('/pull_wire_explode')
def page_pull_wire_explode(data, result):
    if game.started:
        game.lose()
        game.timer.set_delta_time(-999999999999)

@page('/pull_wire_speedup')
def page_pull_wire_speedup(data, result):
    if game.started:
        game.timer.set_speed(100)
        print game.timer.speed

@page('/pull_wire_timepenalty')
def page_pull_wire_timepenalty(data, result):
    if game.started:
        game.timer.set_delta_time(- 1 * 60)

@page('/pull_wire_winner')
def page_pull_wire_winner(data, result):
    if game.started:
        game.win()

@page('/timer_alert') # BOOM
def page_timer_alert(data, result):
    game.timer.alert()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
