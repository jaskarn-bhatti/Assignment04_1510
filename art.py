def the_big_top():
    print("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠶⠶⣶⣄⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⠀⠀⠀⠈⣿⣿⡟⢿⣍⣉⣵⣶⣶⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣄⠀⠀⠀⣸⣿⣿⢛⣩⡭⠭⠟⠋⠹⣷⡀⠀⠉⠻⣉⣀⣀⣠⣤⡤⢶⣶⣞⠋⢉⠀⠀⠀⠀⠀⢀⣀⣀⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣶⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⢸⣿⣀⣀⠀⠘⢿⠿⠿⠿⠻⠛⠉⠹⠛⠉⣀⣀⣠⣤⣾⣿⠟⢉⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡋⠛⠛⠛⠳⠶⠶⠶⠶⠶⠾⠿⠛⠛⠋⠋⠀⠀⠻⣡⣤⣛⣩⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣶⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣤⠴⣿⣟⣛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⢀⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠾⠿⠿⠛⠙⠉⠙⠓⠒⠒⠊⠁⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠋⠀⠀⠀⠙⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠋⠀⠀⠀⠀⠀⠙⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢿⣿⠿⣿⣷⠤⣤⣴⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⣼⡟⠀⡿⡇⠀⠈⣿⠙⢻⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⠟⢠⣿⡇⢸⡇⣿⡆⠀⢻⣄⠈⢧⡈⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⡿⠋⢀⣿⡿⠃⢸⡇⢻⡇⠀⢸⣿⡆⠈⢳⣄⠈⠙⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠋⣨⠟⠁⠀⣼⢻⠇⠀⢸⠁⢸⣿⠀⠘⣿⡿⡄⠀⠙⣦⡀⠀⠙⠳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⡿⠟⠋⢀⡾⠋⠀⢀⣾⠃⣿⠀⠀⣼⠀⠈⢿⠀⠀⠻⣧⢿⡄⠀⠈⢳⣄⠀⠀⠈⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⠟⠋⠀⢀⡴⠋⠀⠀⢠⡟⠁⢠⡏⠀⠀⣿⠀⠀⢸⡆⠀⠀⢿⡌⢳⣦⠀⠀⠹⣷⡄⠀⠀⠀⠈⠻⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⡿⠟⠁⠀⢀⡴⠋⠀⠀⠀⣴⡟⠀⠀⣼⠁⠀⠀⣿⠀⠀⢸⡇⠀⠀⠸⣧⠀⠙⢦⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠈⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡾⠟⠛⠉⠀⠀⢀⡴⠋⠀⠀⠀⢠⣾⠋⠀⠀⣠⡟⠀⠀⠀⡏⠀⠀⠘⣇⠀⠀⠀⢻⡄⠀⠈⢳⡄⠀⠀⠈⠻⣷⣄⠀⠀⠀⠀⠀⠈⠛⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠛⠛⠀⠀⠀⠀⣠⡶⠋⠀⠀⠀⠀⣠⠟⠁⠀⠀⢰⣿⠀⠀⠀⠀⡇⠀⠀⠀⣿⠀⠀⠀⠀⣷⡀⠀⠀⠙⢦⡀⠀⠀⠈⠛⢷⣄⠀⠀⠀⠀⠀⠀⠈⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠟⠋⠁⠀⠀⠀⠀⢀⣠⠞⠁⠀⠀⠀⠀⣠⡾⠃⠀⠀⠀⢠⡿⠁⠀⠀⠀⢀⡇⠀⠀⠀⢿⠀⠀⠀⠀⠘⣿⠀⠀⠀⠀⠙⣦⡀⠀⠀⠀⠙⠷⣦⡀⠀⠀⠀⠀⠀⠀⠉⠛⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠾⠛⠋⠀⠀⠀⠀⠀⠀⣀⡴⠋⠁⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⣾⠁⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⡄⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠈⠻⣶⣄⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⠟⠛⠋⠀⠀⠀⠀⠀⠀⠀⢀⣠⠞⠉⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⠀⠈⢳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣶⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠶⠋⠁⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⣠⣿⠃⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠙⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠶⣦⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣤⣀⣀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠋⠁⠀⠀⠀⠀⠀⢀⣠⠞⠉⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠀⠀⠀⠀⠙⠿⣦⡀⠀⠀⠀⠀⠀⠈⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠈⠉⠙⠛⠻⠶⣶⣄⣴⣏⣡⣀⡀⠀⠀⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⢀⣤⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣦⡀⠀⠀⠀⠀⠀⠈⠻⠦⣄⠀⠀⠀⠀⠀⠀⢈⣙⣦⣤⣴⣾⡿⠟⠛⠉⠁⡸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⣸⡿⠋⠀⠈⠛⢿⣷⢶⣶⣶⣿⣤⣤⣤⣤⣤⠶⢶⣶⢶⣾⣋⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⢸⣿⠀⣀⣀⠀⢀⣸⣏⠀⠀⠀⠀⠀⢀⣀⣀⡀⣀⣈⣿⠶⠶⠶⢶⣤⣤⣴⣦⣿⣷⣤⣤⣴⣶⣶⡟⠛⠻⣏⠉⠀⠀⠀⠀⠀⢸⡇⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠈⣧⡀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠹⣏⠉⠉⠉⠉⠙⠛⠛⣿⣿⠋⠉⠉⠉⠉⣿⣿⠛⠛⠛⠛⠛⠉⠙⢿⡇⠀⠀⠀⠀⠀⠀⠀⠘⣧⡀⠉⠁⠀⠀⠀⠀⠀⣸⠇⠀⠀⠙⣦⡀⠀⠀⠀⠀⢸⡇⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⣠⡟⣿⠀⠀⠀⠀⠀⠀⠀⠘⢿⡄⠀⠀⠀⢀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣦⠀⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠀⠀⠸⣿⡄⠀⠀⠀⠀⠀⣤⣌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡄⠀⠀⠀⠀⠀⣸⡿⠀⠀⠀⠀⢹⣧⣄⠀⠀⢰⣿⡧⠉⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣄⣠⡿⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⠀⠀⠀⣾⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⢠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠙⣿⠀⠀⠀⠀⢰⣿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢠⠈⢿⡆⠀⠀⠀⠀⡿⠃⠀⠀⠀⠀⢸⡏⢿⡄⠀⢸⣿⡇⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡟⠉⡇⠀⢹⣷⡀⠀⠀⠀⠀⣠⣾⡟⠹⣧⠀⣰⠇⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⢿⡄⠀⠀⣼⡿⠀⠀⠀⠀⠀⠀⡀⠀⠀⠘⣧⠀⠀⢠⣿⡗⠀⠙⣧⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⣿⣄⠀⠀⣸⠇⠀⠀⠀⠀⢠⣿⠃⠀⣿⣆⠸⢿⠀⠀⠈⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⠀⡇⠀⢸⠿⠿⢤⣤⣴⣿⠇⣿⡇⠀⢹⣿⡿⠀⣿⠀⢿⣄⠀⠀⠀⣀⢠⣾⠇⠀⠀⠘⣿⣀⣾⣿⠇⠀⠀⠀⠀⠀⢀⣇⠀⠀⠀⢿⡆⢀⣿⢸⡇⠀⠀⢹⡷⢤⡀⠀⠀⠀⣸⣿⠀⠀⣿⠻⣧⠀⣿⠀⢸⣧⠴⠾⠟⢻⠀⠀⣿⠘⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠁⠀⣾⡇⠀⣿⠀⠀⠀⠀⠀⣿⠀⢸⡇⠀⠀⣿⡇⠀⣿⠀⠀⠉⠳⢶⣾⠛⢸⡿⠀⠀⠀⢠⡞⠿⣿⡿⠀⠀⠀⠀⠀⢀⣼⢻⠀⠀⠀⠈⢿⣿⠃⠸⡇⠀⠀⢸⡇⠀⢹⡗⠛⠛⠃⣿⠀⠀⣿⠀⠙⣧⣿⠀⠘⣇⠀⠀⠀⢸⠀⠀⢻⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠁⠀⢠⣿⡃⠀⣿⠀⠀⠀⠀⠀⡟⠀⣾⡇⠀⠀⣿⡇⠀⣿⡀⠀⠀⠀⠀⡟⠀⢸⡇⠀⠀⠀⢸⡇⠀⣿⡇⠀⠀⠀⠀⠀⢸⣿⠘⠀⠀⠀⠀⠀⣿⡆⠀⣇⠀⠀⢸⡇⠀⢸⡇⠀⠀⠀⣿⠀⠀⣿⠀⠀⠻⣿⠀⠀⢻⠀⠀⠀⢸⡇⠀⢸⡆⠀⠀⠀⠀⠀⠈⢻⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠘⠛⢛⣼⡏⠀⠀⠀⠀⢰⡇⠀⡿⠃⠀⠀⣿⠀⢰⣏⠉⠁⠀⠀⢠⡇⠀⣿⡇⠀⠀⠀⢸⡇⠀⣿⠇⠀⠀⠀⠀⠀⣾⡇⠀⢀⠀⠀⠀⠀⣿⡇⠀⣿⡇⠀⠀⣇⠀⢸⡇⠀⠀⠀⢹⡀⠀⢸⡀⠀⠀⠿⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠘⣷⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣻⣷⡿⢹⡇⠀⠀⠀⢀⣼⠇⢰⡇⠀⠀⢰⣿⠀⢸⣿⠀⠀⠀⠀⢸⡇⢀⡿⠃⠀⠀⠀⣸⠁⢠⣿⠀⠀⠀⠀⠀⢰⡏⠀⠀⢸⣦⠀⠀⠀⠹⡇⠀⢿⡇⠀⠀⣿⡆⠈⣧⠀⠀⠀⢸⣿⠀⢸⡇⠀⠀⣶⡆⠀⡀⠀⠀⠀⠈⡇⠀⠘⣧⠀⠀⠀⢀⡀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⠀⠀⣿⠁⠀⣾⠀⠀⠀⠀⢸⡿⠀⢸⠁⠀⠀⣸⠋⠀⣼⠁⠀⠀⠀⢠⡾⠀⢸⡇⠀⠀⠀⠀⣿⠀⢸⡿⠀⠀⠀⠀⠀⣿⠀⠀⠀⣿⣿⡀⠀⠀⠀⣿⠀⢸⣇⠀⠀⢿⡇⠀⢻⡀⠀⠀⠀⣿⡀⠈⣷⡄⠀⠸⣇⠀⢹⡄⠀⠀⠀⣿⠀⠀⢻⣄⣴⣾⠇⠛⢿⠓⣾⣷⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢰⠏⠀⢠⡏⠀⠀⠀⠀⣾⡇⠀⣿⠀⠀⢠⡏⠀⢠⡟⠀⠀⠀⠀⣼⡇⠀⣼⠀⠀⠀⠀⣼⡇⠀⣾⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠈⣿⣇⠀⠀⠀⢹⡄⠘⢿⡀⠀⢸⣷⠀⠸⣿⣀⣠⢶⣿⣇⠀⢻⣇⠀⠀⢿⡆⠈⣷⠀⠀⠀⠸⣷⠀⠸⡟⠿⣦⡄⡀⠘⢯⢹⣿⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⢠⡿⠀⢀⣾⠀⠀⠀⠀⢸⠏⠀⢿⡇⠀⣠⣾⠀⠀⣼⠁⠀⠀⠀⢸⠏⠀⢰⡇⠀⠀⠀⢠⡿⠀⢠⡏⠀⠀⠀⠀⣰⡿⠦⠀⠀⠀⠀⠙⣿⡄⠀⠀⠘⡇⠀⠸⣇⠀⠀⢹⡄⠀⢿⡿⠇⠘⢿⣿⠀⠈⢻⡀⠀⠘⢿⠀⢹⣧⠀⠀⠀⢿⡄⠀⢻⡆⠀⠀⠻⠿⠂⠘⣿⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡄⢠⡾⠁⢠⣿⠃⠀⠀⠀⢠⡟⠀⢀⡾⠀⠀⣸⠇⠀⣾⠏⠀⠀⠀⣠⠏⠀⢀⡞⠀⠀⠀⢀⣾⠀⠀⡾⠁⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠈⢿⡀⠀⠀⢻⡀⠀⢻⡄⠀⠈⢷⠀⠀⢷⡄⡀⢴⣾⣇⠀⠈⢷⡀⠀⠸⣇⠀⢿⣇⠀⠀⠀⣷⠀⠘⢿⡄⠀⠀⠀⠀⠀⠛⣿⡄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣀⡠⠤⠤⠖⠒⠻⣧⡴⠋⠀⢀⡾⠁⠀⠀⢀⣴⠟⠀⢠⣾⣃⣠⡞⠁⠀⣰⠋⠀⠀⣀⣴⠟⠀⣠⡾⠁⠀⠀⠀⡼⠃⠀⣸⠇⠀⠀⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⠀⠸⣧⡀⠈⣧⠀⠀⠘⣇⠀⠈⢿⣷⣤⡙⢻⡆⠀⠘⢧⡀⠀⢻⡄⠀⠻⣄⠀⠀⠸⣆⠀⠈⢷⡀⠀⠀⠀⠀⠀⠘⠇⠀⠀⠀⠀⠀
    ⠀⣠⣴⡶⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠷⠶⠶⠶⠾⠷⠶⠶⠟⢉⣅⣠⣴⣿⣿⡟⢩⣄⣀⣼⣯⣤⣴⣾⣭⣥⣤⣴⡟⠁⠀⢠⡤⠞⠁⢀⣴⠏⠀⣴⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠹⣇⠀⠈⢷⡄⠀⠹⣦⡀⠈⠻⣧⣤⠀⠙⣆⠀⠈⠳⢶⡄⠻⣄⠀⠙⢶⣄⡀⠘⣆⠀⠀⠛⠦⣄⡀⠐⠛⠁⠀⠀⠀⠀⠀⠀
    ⠺⣿⣯⣁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠛⠛⠓⠾⢯⣤⣤⣤⣾⣧⡴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣜⣧⡀⠀⠙⠶⢤⣿⣷⣤⣤⣬⡽⠿⠷⠿⠷⠶⠶⠦⠿⠿⠿⠶⠤⠤⠼⠟⠛⠛⠓⠶⠶⠶⠿⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⣴⡶⢾⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀
    ⠀⠀⠀⠀⠈⠻⢿⣤⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⡀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⣤⡤⠄⠾⠿⠋⠉⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠓⠶⠶⠶⠶⠤⢤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣤⣤⡤⠴⠶⠾⠶⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣠⣤⣤⠤⠖⠛⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠒⠲⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠚⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

        """)

