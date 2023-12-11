from controllers.games_controller import games
from controllers.auth_controller import auth
from controllers.currently_playing_controller import currently_playing
# from controllers.backlog_controllercontroller import 
# from controllers.wishlist_controller_controller import 

registerable_controllers = [
    auth,
    games,
    currently_playing
    # backlog
    # wishlist
]