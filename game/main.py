import random

options = ['piedra', 'papel', 'tijera']
player_points = 0
pc_points = 0

def selecciones():
    player_option = ""
    while player_option not in options:
        player_option = input("Ingrese su opcion (piedra, papel o tijera): ")
        if player_option not in options:
            print("Esa opción no es válida.")
            StopIteration()
    computer_option = random.choice(options)
    return player_option, computer_option

def logica(player_option, computer_option):
    print(f"Usted eligió: {player_option}")
    print(f"La PC eligió: {computer_option}")
    if player_option == computer_option:
        print("Empate, nadie suma puntos")
        return "Empate"
    elif player_option == options[0] and computer_option==options[1] or player_option==options[1] and computer_option==options[2] or player_option==options[2] and computer_option==options[0]:
        print("Gana PC, suma 1 punto")
        return "PC"
    else:
        print("Gana Usted, suma 1 punto")
        return("Player")

def points():
    global pc_points
    global player_points
    player_option,computer_option = selecciones()
    logic = logica(player_option, computer_option)
    if logic=="Empate":
        return True
    elif logic=="PC":
        pc_points += 1
        return pc_points
    else:
        player_points += 1
        return player_points

def jugar():
    while True:
        points()
        if player_points == 3:
            print("Felicitaciones!! Usted gana!!")
            break
        elif pc_points == 3:
            print("La PC gana. Mas suerte la próxima")
            break
        print("Usted tiene %s punto/s" % (player_points)) 
        print("La PC tiene %s punto/s" % (pc_points))
    
        print("------------------------------------------------------------------------")
        print("Siguiente Ronda")
        print("------------------------------------------------------------------------")


jugar()