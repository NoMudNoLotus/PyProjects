#!/usr/bin/env Python
# rock paper scissors game :)

import random

class RockPaperScissors:

    def Start(self):

        rps = input("Choose: \nRock (r)\nPaper (p)\nOr Scissors (s)")
        if rps == 'r' or rps == 'p' or rps == 's':  # check if valid

            # init cpu
            rand = random.randint(0, 2)
            cpu = ''
            if rand == 0:
                cpu = 'r'
            elif rand == 1:
                cpu = 'p'
            else:
                cpu = 's'

            if rps == cpu:
                print(f"DRAW! {rps} vs {cpu} ")
            else:
                if rps == 'r' and cpu == 'p':
                    print(f"YOU LOSE! {cpu} beats {rps}")
                elif rps == 'p' and cpu == 's':
                    print(f"YOU LOSE! {cpu} beats {rps}")
                elif rps == 's' and cpu == 'r':
                    print(f"YOU LOSE! {cpu} beats {rps}")
                elif rps =='r' and cpu == 's':
                    print(f"YOU WIN! {rps} beats {cpu}")
                elif rps == 'p' and cpu == 'r':
                    print(f"YOU WIN! {rps} beats {cpu}")
                elif rps == 's' and cpu == 'p':
                    print(f"YOU WIN! {rps} beats {cpu}")

        else:
            print(f'ERROR {rps} Not a valid option.')


game = RockPaperScissors()
game.Start()