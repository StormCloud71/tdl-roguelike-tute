def handle_keys(user_input):
    # Movement keys
    # deviating from the tutorial in implementing WASD keys
    key_char = user_input.char
    
    if user_input.key == 'UP' or key_char=='w':
        return {'move': (0, -1)}
    elif user_input.key == 'DOWN' or key_char=='s':
        return {'move': (0, 1)}
    elif user_input.key == 'LEFT' or key_char=='a':
        return {'move': (-1, 0)}
    elif user_input.key == 'RIGHT' or key_char=='d':
        return {'move': (1, 0)}
    elif key_char=='q':
        return {'move': (-1,-1)}
    elif key_char=='e':
        return {'move': (1,-1)}
    elif key_char=='z':
        return {'move': (-1,1)}
    elif key_char=='c':
        return {'move': (1,1)}

    if user_input.key == 'ENTER' and user_input.alt:
        # Alt+Enter: toggle full screen
        return {'fullscreen': True}
    elif user_input.key == 'ESCAPE':
        # Exit the game
        return {'exit': True}

    # No key was pressed
    return {}
