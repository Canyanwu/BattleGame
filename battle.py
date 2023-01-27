""" Implementation of the Battler class and its methods.

This method reads and creates an army for each player, say army1 and army1,
sets them in stack formation or Queue formation depending on the formation
and calls internal method __conduct_combat(self, army1, army2, 0) and returns
the winner

methods implemented:
gladiatorial_combat(self, player_one: str, player_two: str)
fairer_combat(self, player_one: str, player_two: str)
__conduct_combat(self, army1: Army, army2: Army, formation: int)

"""

__author__ = "Chukwuudi (Chuchu) Anyanwu"

from army import Army


class Battle:
    """creates two player with stack of armies and method to battle"""

    def gladiatorial_combat(self, player_one: str, player_two: str) -> int:
        """ This method reads and creates an army for each player, say army1
            and army1, sets them in stack formation

        @complexity: Best O(n) and worst O(n)
        """
        FORMATION = 0   # constant
        army_1 = Army()  # creating an instance of Army
        army_1.choose_army(player_one, FORMATION)  # creating player stack

        army_2 = Army()  # creating an instance of Army
        army_2.choose_army(player_two, FORMATION)  # creating player stack

        return self.__conduct_combat(army_1, army_2, FORMATION)

    def fairer_combat(self, player_one: str, player_two: str) -> int:
        """ Conducts a battle between two armies in queue formation and  whenever a
        fighter survives, it gets appended at the end of the queue and at the end it
        return the winner from the conduct_combat method

        @complexity: Best O(n) and worst O(n)
        """
        FORMATION = 1
        army_1 = Army()  # creating an instance of Army
        army_1.choose_army(player_one, FORMATION)  # creating player stack

        army_2 = Army()  # creating an instance of Army
        army_2.choose_army(player_two, FORMATION)  # creating player stack

        return self.__conduct_combat(army_1, army_2, FORMATION)

    def __conduct_combat(self, army1: Army, army2: Army, formation: int) -> int:
        """ conducts battle between two armies based on the formation and return the winner

        the worst-case run-time complexity for queue and stack operations is O(1)
        @complexity: Best O(n) and worst is O(n) for both formation 0 and formation 1
        where n is length of the army force.
        """

        if formation == 0:
            while len(army1.force) != 0 and len(army2.force) != 0:  # if both are stack are still not empty
                pop_play1 = army1.force.pop()   # pop the player one army
                pop_play2 = army2.force.pop()   # pop the player two army

                x = pop_play1.attack_damage()   # get player one attack damage
                y = pop_play2.attack_damage()   # get player two attack damage

                pop_play1.defend(x)     # decrease player one life based on the player 2 attack damage
                pop_play2.defend(y)     # decrease player two life based on the player 1 attack damage

                if pop_play1.is_alive():
                    army1.force.push(pop_play1)     # push back army if still alive

                if pop_play2.is_alive():
                    army2.force.push(pop_play2)

            if army1.force.is_empty() and army2.force.is_empty():
                return 0  # draw

            elif not army1.force.is_empty() and army2.force.is_empty():
                return 1  # Player one win

            else:
                return 2  # Player two

        if formation == 1:
            while len(army1.force) != 0 and len(army2.force) != 0:
                pop_play1 = army1.force.serve()     # relax the player one army in the front
                pop_play2 = army2.force.serve()     # relax the player two army in the front

                x = pop_play1.attack_damage()
                y = pop_play2.attack_damage()

                pop_play1.defend(x)
                pop_play2.defend(y)

                if pop_play1.is_alive():
                    army1.force.append(pop_play1)  # return player one army at the rear of the queue

                if pop_play2.is_alive():
                    army2.force.append(pop_play2)   # return player two army at the rear of the queue

            if army1.force.is_empty() and army2.force.is_empty():
                return 0  # draw

            elif not army1.force.is_empty() and army2.force.is_empty():
                return 1  # Player one win
            else:
                return 2  # Player two win


# TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING

# battle = Battle()
# print(battle.gladiatorial_combat("James", "John"))
#
# battle = Battle()
# print(battle.fairer_combat("Judas", "Joshua"))
