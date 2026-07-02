def blackjack():

    cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10]

    estadisticas = {
        "ganadas": 0,
        "perdidas": 0,
        "empatadas": 0
    }

    while True:

        print("\n=== BLACKJACK ===")
        print("1. Jugar")
        print("2. Ver estadísticas")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

    
        while opcion not in ["1", "2", "3"]:

            opcion = input("Opción inválida. Ingrese 1, 2 o 3: ")

        
        if opcion == "1":

            jugador = []
            dealer = []

            jugador.append(random.choice(cartas))
            jugador.append(random.choice(cartas))

            dealer.append(random.choice(cartas))
            dealer.append(random.choice(cartas))

            print("Tus cartas:", jugador)
            print("Tu total:", sum(jugador))

            input("Presiona Enter para continuar...")

            # TURNO DEL JUGADOR
            while sum(jugador) < 21:

                decision = input("¿Pedir carta? (s/n): ").lower()

                
                while decision not in ["s", "n"]:

                    decision = input("Ingrese solo s o n: ").lower()

                if decision == "s":

                    nueva_carta = random.choice(cartas)

                    jugador.append(nueva_carta)

                    print("Robaste:", nueva_carta)
                    print("Tus cartas:", jugador)
                    print("Tu total:", sum(jugador))

                    input("Presiona Enter para continuar...")

                else:
                    break

          
            if sum(jugador) > 21:

                print("Te pasaste de 21.")
                print("Perdiste.")

                estadisticas["perdidas"] += 1

            else:

                print("Turno del dealer...")
                input("Presiona Enter para continuar...")

             
                while sum(dealer) < 17:

                    nueva_carta = random.choice(cartas)

                    dealer.append(nueva_carta)

                    print("Dealer roba:", nueva_carta)
                    print("Cartas dealer:", dealer)
                    print("Total dealer:", sum(dealer))

                    input("Presiona Enter para continuar...")

                # RESULTADOS
                print("=== RESULTADOS ===")

                print("Tus cartas:", jugador)
                print("Tu total:", sum(jugador))

                print("\nCartas dealer:", dealer)
                print("Total dealer:", sum(dealer))

                if sum(dealer) > 21:

                    print("El dealer se pasó.")
                    print("Ganaste.")

                    estadisticas["ganadas"] += 1

                elif sum(jugador) > sum(dealer):

                    print("Ganaste.")

                    estadisticas["ganadas"] += 1

                elif sum(jugador) < sum(dealer):

                    print("Perdiste.")

                    estadisticas["perdidas"] += 1

                else:

                    print("Empate.")

                    estadisticas["empatadas"] += 1

   

        elif opcion == "2":

            print("=== ESTADISTICAS ===")

            print("Ganadas:", estadisticas["ganadas"])
            print("Perdidas:", estadisticas["perdidas"])
            print("Empatadas:", estadisticas["empatadas"])

            input("Presiona Enter para continuar...")



        elif opcion == "3":

            print("Gracias por jugar.")
            break


blackjack()