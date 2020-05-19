""" Implementation of Army Battle game of two players.

The objective of this is to design and implement in Python classes that require inheritance
and use readily available Stack and Queue ADTs, use and modify UnitTest code and continue
practicing the implementation of correct, high quality and well documented code.

This game has two players. Each has a budget of $30 to buy an army that can be composed of
three different kinds of fighter units: soldiers, archers, and cavalry.
After each player buys as many units as it wants with the $30 available, the army of each
player takes positions to get ready for battle as follows: all soldiers are positioned first,
then all archers, and finally all the cavalry. That way, soldiers will battle first, then
archers, and finally the cavalry and the winner of the battle is return.
"""

__author__ = "Derek Anyanwu"

from typing import Any, Tuple
from abc import ABCMeta, abstractmethod
from stack import ArrayStack
from queue import CircularQueue


class Fighter(metaclass=ABCMeta):
    """Fighter Abstract base class"""

    def __init__(self, life: int, experience: int) -> None:
        """ it initialises the variables using the amounts received as input.
            precondition: they both must be greater or equal to 0
        """
        assert life >= 0, "life must be greater or equal to 0"
        assert experience >= 0, "experience must be greater or equal to 0"
        self.life = life
        self.experience = experience

    def is_alive(self) -> bool:
        """it returns True if the fighter’s life is greater than 0, False otherwise.

        @complexity: Best O(1) and worst O(1)
        """
        return True if self.life > 0 else False

    def lose_life(self, lost_life: int) -> None:
        """ it decreases the life of the unit by the amount indicated by lost life

        @complexity: Best O(1) and worst O(1)
        precondition: lost_life must be ≥ 0
        """
        assert lost_life >= 0, "lost_life must be greater or equal to 0"
        self.life -= lost_life

    def gain_experience(self, gained_experience: int) -> None:
        """ it increases the experience of the unit by the amount indicated by gained experience

        @complexity: Best O(1) and worst O(1)
        precondition: gained_experience must be ≥ 0
        """
        assert gained_experience >= 0
        self.experience += gained_experience

    def get_experience(self) -> int:
        """it returns the experience of the unit"""
        return self.experience

    @abstractmethod
    def get_speed(self) -> int:
        """it returns the speed of the unit"""
        pass

    def get_cost(self) -> int:
        """it returns the cost of the unit"""
        pass

    @abstractmethod
    def attack_damage(self) -> int:
        """ it returns the amount of damage performed by the unit when it attack """
        pass

    def defend(self, damage: int) -> None:
        """ it decreases the life of the unit by the amount lost (if any) after defending
            from an attack that inflicted the amount of damage indicated by damage

            precondition: must be ≥ 0
        """
        assert damage >= 0
        self.life -= damage

    @abstractmethod
    def __str__(self) -> str:
        """ it returns a string indicating the type of unit, its current life and experience """
        pass


# Soldier...Soldier...Soldier...Soldier...Soldier...Soldier...Soldier...
class Soldier(Fighter):
    """ Soldier class inheriting from parent class Fighter and implementing its abstract function"""
    cost = 1  # static variable of the Soldier class

    def __init__(self) -> None:
        """ create a new instance of Soldier, setting up the variables in the object. """
        self.life = 3
        self.experience = 0
        Fighter.__init__(self, self.life, self.experience)  # call super constructor

    def get_speed(self) -> int:
        """" Returns soldier's speed which is soldier's experience + 1 """
        return self.experience + 1

    def get_cost(self) -> int:
        """ Returns the soldier's cost """
        return self.cost

    def attack_damage(self) -> int:
        """ Returns Soldier's damage on attack """
        return self.experience + 1

    def defend(self, damage: int) -> None:
        """ Returns Soldier's Lost life after defence """
        if damage > self.experience:
            self.life -= 1

    def __str__(self) -> str:
        """ Returns soldier's current life and experience """
        return "Soldier's life = {} and experience = {}".format(self.life, self.experience)


# CavalryCavalryCavalryCavalryCavalryCavalryCavalryCavalryCavalry........
class Cavalry(Fighter):
    """A subclass of Fighter """
    cost = 3  # static variable of the Cavalry class
    speed = 2  # static variable of the Cavalry class

    def __init__(self) -> None:
        """ create a new instance of Cavalry """
        self.life = 4
        self.experience = 0
        Fighter.__init__(self, self.life, self.experience)

    def get_speed(self) -> int:
        """" Returns Cavalry's speed """
        return self.speed

    def get_cost(self) -> int:
        return self.cost

    def attack_damage(self) -> int:
        """ Returns cavalry's damage on attack """
        return (2 * self.experience) + 1

    def defend(self, damage: int) -> None:
        """ Returns Cavalry's Lost life after defence.
            cavalry life reduces when damage is greater than experience

            @complexity: Best O(1) and worst O(1)
        """
        if damage > (self.experience / 2):
            self.life -= 1

    def __str__(self) -> str:
        """ Returns Cavalry's current life and experience """
        return "Cavalry's life = {} and experience = {}".format(self.life, self.experience)


# Archer...Archer...Archer...Archer...Archer...Archer...Archer...Archer..
class Archer(Fighter):
    """ A subclass of Fighter"""
    cost = 2  # static variable of the Archer class
    speed = 3  # static variable of the Archer class

    def __init__(self) -> None:
        self.life = 3
        self.experience = 0
        Fighter.__init__(self, self.life, self.experience)

    def get_speed(self) -> int:
        return self.speed

    def get_cost(self) -> int:
        return self.cost

    def attack_damage(self) -> int:
        """ Returns Archer'sdamage on attack"""
        attack_damage = self.experience + 1
        return attack_damage

    def defend(self, damage: int) -> None:
        """ Returns Archer's Lost life after defence """
        self.life -= 1

    def __str__(self) -> str:
        """ Returns Archer's current life and experience """
        return "Archer's life = {} and experience = {}".format(self.life, self.experience)


class Army:
    """ Instances contain the name of the army’s player together with an ADT containing
        the fighters purchases by the player.
    """

    def __init__(self) -> None:
        self.name = None
        self.force = None

    def __display_info(self, name: str) -> None:
        """ Internal method that Display message to player to choose army

        precondition: name must be string
        @complexity: Best O(1), worst O(1)
        """
        # assert isinstance(name, str), "Input variable(name) should be strings"
        line1 = "Player {} choose your army as S A C".format(name)
        line2 = "where S is the number of soldiers"
        line3 = 6 * ' ' + "A is the number of archers"
        line4 = 6 * ' ' + "C is the number of cavalry"
        print(line1, line2, line3, line4, sep='\n')

    def choose_army(self, name: str, formation: int) -> None:
        """" method ensures players three input (s, a and c) are valid for the game

        @throws: ValueError if the formation is either an int, less than 0, or greater than 1
        @complexity: Best O(n) and worst O(n)
        """
        # Formation validator with if / else and thrown exception if not given 0 or 1.
        try:
            N = int(formation)
        except ValueError:
            raise ValueError('Formation must be integer')
        if N < 0 or N > 1:
            NError = ValueError('Formation must be either 0 or 1, and not {}'.format(N))
            raise NError

        self.__display_info(name)  # call method display_info with the player name
        s, a, c = self.__read_input(name, formation)  # read the armies using __read_input method
        self.__correct_army_given(s, a, c)  # Pass the read input for validation
        if self.__correct_army_given(s, a, c):  # if returned True, call assign_army method
            self.__assign_army(name, s, a, c, formation)
        else:
            self.choose_army(name, formation)  # if False return back to the function to try again

    def __read_input(self, name, formation) -> Tuple[Any, Any, Any]:
        """ Internal method read input from players, method also makes sure input is three digit spaced out

        @complexity: The complexity of "s1, a1, c1 = list(map(int, input("Enter your army as S A C: ").split()))"
        is Best O(n) and worst O(n)
        input().split() part read stuff from the input. This will be proportional to the length of the input,
        so it is linear. Map() takes in two inputs arguments, one of which is a list, and the other one is a
        integer function and  it then transforms each item in the list by applying integer function and returns
        the new transformed list So the overall complexity is linear.
        """
        try:
            # here input are read and then split function split them based on space
            # then it is converted to integer and the map function mapped them to list
            s1, a1, c1 = list(map(int, input("Enter your army as S A C: ").split()))
        except ValueError:
            print("----Please {} enter a valid input containing three numbers spaced out-----".format(name))
            self.choose_army(name, formation)  # call choose army again to try again
        else:
            return s1, a1, c1

    def __calculate_cost(self, soldiers: int, archers: int, cavalry: int) -> Tuple[int, int]:
        """ Internal method calculates the total cost player has spent and return to caller.

        @complexity: Best O(n) and worst O(n) where n is the size of elements to sum and  the elements to return
        the minimum element. Since the elements are fixed ( 3) , so the Best O(1) and worst O(1)
        """
        army_1 = Soldier()  # calling Soldier object
        army_2 = Archer()  # calling Archer object
        army_3 = Cavalry()  # calling Cavalry object

        # getting cost of each army using their get_cost method
        soldier_cost = army_1.get_cost()
        archer_cost = army_2.get_cost()
        cavalry_cost = army_3.get_cost()

        # Calculating total cost each player has spent on each army
        s_total_cost = soldier_cost * soldiers
        a_total_cost = archer_cost * archers
        c_total_cost = cavalry_cost * cavalry
        total_cost = sum([s_total_cost, a_total_cost, c_total_cost])
        min_cost = min([soldiers, archers, cavalry])

        return min_cost, total_cost  # minimum and total cost player spent for his/her army

    def __correct_army_given(self, soldiers: int, archers: int, cavalry: int) -> bool:
        """ Internal method that validates the army input

        @complexity: Best O(1) and worst O(1)
        """

        BUDGET = 30  # Maximum budget allowed to spend for each player

        # call _calculate_cost
        min_cost, player_spent_cost = self.__calculate_cost(soldiers, archers, cavalry)

        # checking the total cost of the army chosen is within the budget
        if player_spent_cost <= BUDGET and min_cost >= 0:
            return True
        else:
            return False

    def __assign_army(self, name: str, sold: int, arch: int, cav: int, formation: int) -> str:
        """ method sets the formation of the army to either stack or queue form, depending on
            the value of formation (0 = stack and 1 = queue)

        # @ Complexity: The inner loop runs O(n), n been the size of each army chosen and the outer
        run is constant, so the best case is O(1) and the worst case is O(n) for both formation 0
        and formation 1
        """
        sol_object = Soldier()  # calling Soldier object
        ach_object = Archer()  # calling Archer object
        cav_object = Cavalry()  # calling Cavalry object

        player_input = [sold, arch, cav]    # list containing player input
        size = len(player_input)    # length of the player input -- 3
        player_object = [sol_object, ach_object, cav_object]  # player soldier, archer, cavalry
        stack_size = sum([sold, arch, cav])  # size of the players

        # reverse the stack to enable the soldiers be the FirstInFirstOut  and Cavalry LastInLastOut
        # pushing in a reverse order, solders first and cavalry last.
        if formation == 0:
            player_stack = ArrayStack(stack_size)  # created stack to hold the armies purchased
            for i in range(size - 1, -1, -1):   #
                army_object = player_object[i]
                quantity = player_input[i]
                for j in range(quantity):
                    player_stack.push(army_object)
            self.force = player_stack

        # Circular Queue implementation
        # appending in a queue style
        if formation == 1:
            player_queue = CircularQueue(stack_size)  # created Queue to hold the armies purchased
            for i in range(size):
                army_object = player_object[i]
                quantity = player_input[i]
                for j in range(quantity):
                    player_queue.append(army_object)
            self.force = player_queue

        self.name = name

    def __str__(self) -> str:
        """Computes a string from the stack items - top to bottom."""
        return str(self.force)



# TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING TESTING

# army = Army()
# army.choose_army("James", 1)
# print(army)

# army = Army()
# army.choose_army("James", 1)
# print(army)
