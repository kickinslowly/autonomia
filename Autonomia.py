import random
import time
import turtle
import matplotlib.pyplot as plt
import math
import sqlite3

conn = sqlite3.connect('creature.db')

c = conn.cursor()
# c.execute("""CREATE TABLE creatures (
#                 rank blob,
#                 name blob,
#                 oxygen blob,
#                 carbon blob,
#                 location blob
#                 )""")

class Creature:
    # turtle.delay(0)

    def __init__(self):
        self.rank = 'Eubacteria'
        self.name = random.randint(0, 100000)
        self.health = 20
        self.speed = 1
        self.nutrition = ['oxygen']
        self.intelligence = 0
        self.offense = 1
        self.defense = 0
        self.oxygen = 20
        self.carbon = 20
        self.elements = {'oxygen': self.oxygen, 'carbon': self.carbon}
        self.location = [random.randint(-400, 400), random.randint(-400, 400)]
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(self.location[0], self.location[1])
        self.turtle.shape('circle')
        self.turtle.color('violet')
        self.turtle.turtlesize(self.health / 100)
        self.turtle.speed(2)

    def move(self, x=random.randint(-50, 50), y=random.randint(-50, 50)):
        if self.rank == 'Eubacteria':
            pass
        else:
            self.location[0] += x
            self.location[1] += y
            self.turtle.penup()
            self.turtle.goto(self.location[0], self.location[1])
            self.turtle.pendown()

# if capable, creature searches for predator and moves away from nearest threat
    def evade(self):
        # if len(world.protista) > 0 or len(world.animalia) > 0:
        if self.rank == 'Eubacteria':
            pass
        if self.rank == 'Chromista' or self.rank == 'Protista' or self.rank == 'Fungi':
            counter = 0
            prev_loc = 101
            loc_dif = 0
            predator = None
            for rank in world.alive:
                for creature in rank:
                    if creature.rank == 'Eubacteria':
                        pass
                    elif creature.rank == 'Plantae':
                        pass
                    elif creature.rank == 'Chromista':
                        pass
                    elif self.name == creature.name:
                        pass
                    elif creature.rank == 'Fungi':
                        pass
                    else:
                        counter += 1
                        loc_difx = self.location[0] - creature.location[0]
                        loc_dify = self.location[1] - creature.location[1]
                        loc_dif = math.sqrt(loc_difx ** 2 + loc_dify ** 2)
                        if counter == 1:
                            prev_loc = loc_dif
                            predator = creature
                        if loc_dif**2 <= prev_loc**2:
                            prev_loc = loc_dif
                            predator = creature
            if predator:
                loc_difx = self.location[0] - predator.location[0]
                loc_dify = self.location[1] - predator.location[1]
                if loc_dify and loc_difx == 0:
                    pass
                elif prev_loc < 300:
                    if loc_difx < 0:
                        self.location[0] -= 10
                    elif loc_difx > 0:
                        self.location[0] += 10
                    if loc_dify < 0:
                        self.location[1] -= 10
                    elif loc_dify > 0:
                        self.location[1] += 10
                    self.turtle.penup()
                    self.turtle.goto(self.location[0], self.location[1])
                    self.turtle.pendown()
        elif self.rank == 'Plantae':
            pass

        elif self.rank == 'Animalia':
            counter = 0
            prev_loc = 101
            loc_dif = 0
            predator = None
            for rank in world.alive:
                for creature in rank:
                    if creature.rank != 'Animalia' or creature.rank != 'Protista':
                        pass
                    elif self.name == creature.name:
                        pass
                    elif self.health > creature.health:
                        pass
                    else:
                        counter += 1
                        loc_difx = self.location[0] - creature.location[0]
                        loc_dify = self.location[1] - creature.location[1]
                        loc_dif = math.sqrt(loc_difx ** 2 + loc_dify ** 2)
                        if counter == 1:
                            prev_loc = loc_dif
                            predator = creature
                        if loc_dif ** 2 <= prev_loc ** 2:
                            prev_loc = loc_dif
                            predator = creature
            if predator:
                loc_difx = self.location[0] - predator.location[0]
                loc_dify = self.location[1] - predator.location[1]
                if loc_dify and loc_difx == 0:
                    pass
                elif prev_loc < 400:
                    if loc_difx < 0:
                        self.location[0] -= 10
                    elif loc_difx > 0:
                        self.location[0] += 10
                    if loc_dify < 0:
                        self.location[1] -= 10
                    elif loc_dify > 0:
                        self.location[1] += 10
                    self.turtle.penup()
                    self.turtle.goto(self.location[0], self.location[1])
                    self.turtle.pendown()

# if capable, creature searches for prey and moves in that direction
    def hunt(self):
        world.update()

        if len(world.protista) > 0 or len(world.animalia) > 0:
            if self.rank == 'Eubacteria':
                pass
            elif self.rank == 'Plantae':
                pass
            elif self.rank == 'Chromista':
                pass
            elif self.rank == 'Protista':
                counter = 0
                prev_loc = 101
                loc_dif = 0
                prey = None
                for rank in world.alive:
                    for creature in rank:
                        if creature.health == 0:
                            pass
                        elif creature.rank == 'Animalia':
                            pass
                        elif self.name == creature.name:
                            pass
                        else:
                            counter += 1
                            loc_difx = self.location[0] - creature.location[0]
                            loc_dify = self.location[1] - creature.location[1]
                            loc_dif = math.sqrt(loc_difx ** 2 + loc_dify ** 2)
                            if counter == 1:
                                prev_loc = loc_dif
                                prey = creature
                            if loc_dif**2 <= prev_loc**2:
                                prev_loc = loc_dif
                                prey = creature
                if prey:
                    prey.evade()
                    loc_difx = self.location[0] - prey.location[0]
                    loc_dify = self.location[1] - prey.location[1]
                    if prev_loc < 100:
                        self.eat(prey)
                    else:
                        if loc_difx < 0:
                            self.location[0] -= 10
                        elif loc_difx > 0:
                            self.location[0] += 10
                        if loc_dify < 0:
                            self.location[1] -= 10
                        elif loc_dify > 0:
                            self.location[1] += 10
                        self.turtle.penup()
                        self.turtle.goto(self.location[0], self.location[1])
                        self.turtle.pendown()
                if self.health > 600:
                    self.reproduce()
                    self.die()
            elif self.rank == 'Animalia':
                counter = 0
                prev_loc = 101
                loc_dif = 0
                prey = None
                for rank in world.alive:
                    for creature in rank:
                        if self.name == creature.name:
                            pass
                        else:
                            counter += 1
                            loc_difx = self.location[0] - creature.location[0]
                            loc_dify = self.location[1] - creature.location[1]
                            loc_dif = math.sqrt(loc_difx ** 2 + loc_dify ** 2)
                            if counter == 1:
                                prev_loc = loc_dif
                                prey = creature
                            if loc_dif**2 <= prev_loc**2:
                                prev_loc = loc_dif
                                prey = creature
                if prey:
                    prey.evade()
                    loc_difx = self.location[0] - prey.location[0]
                    loc_dify = self.location[1] - prey.location[1]
                    if prev_loc < 100:
                        self.eat(prey)
                    else:
                        if loc_difx < 0:
                            self.location[0] -= 10
                        elif loc_difx > 0:
                            self.location[0] += 10
                        if loc_dify < 0:
                            self.location[1] -= 10
                        elif loc_dify > 0:
                            self.location[1] += 10
                        self.turtle.penup()
                        self.turtle.goto(self.location[0], self.location[1])
                        self.turtle.pendown()
                if self.health > 600:
                    self.reproduce()
                    self.die()

            elif self.rank == 'Fungi':
                counter = 0
                prev_loc = 101
                loc_dif = 0
                prey = None
                for rank in world.alive:
                    for creature in rank:
                        if self.name == creature.name:
                            pass
                        elif creature.rank == 'Eubacteria':
                            counter += 1
                            loc_difx = self.location[0] - creature.location[0]
                            loc_dify = self.location[1] - creature.location[1]
                            loc_dif = math.sqrt(loc_difx ** 2 + loc_dify ** 2)
                            if counter == 1:
                                prev_loc = loc_dif
                                prey = creature
                            if loc_dif**2 <= prev_loc**2:
                                prev_loc = loc_dif
                                prey = creature
                if prey:
                    prey.evade()
                    loc_difx = self.location[0] - prey.location[0]
                    loc_dify = self.location[1] - prey.location[1]
                    if prev_loc < 100:
                        self.eat(prey)
                    else:
                        if loc_difx < 0:
                            self.location[0] -= 10
                        elif loc_difx > 0:
                            self.location[0] += 10
                        if loc_dify < 0:
                            self.location[1] -= 10
                        elif loc_dify > 0:
                            self.location[1] += 10
                        self.turtle.penup()
                        self.turtle.goto(self.location[0], self.location[1])
                        self.turtle.pendown()
                if self.health > 600:
                    self.reproduce()
                    self.die()
        else:
            turtle.done()
            
    def live(self):
        world.update()
# hunt
        if random.randint(0, 100) > 0:
            self.hunt()
            world.update()
            if random.randint(0, 100) > 50:
                self.hunt()
                world.update()
# reproduce
        if random.randint(0, 100) > 50:
            self.reproduce()
            world.update()
# random chance to die
        if random.randint(0, 100) > 90:
            self.die()
            world.update()

    def eat(self, creature):
        # turtle.delay(0)
        if self.rank == 'Eubacteria':
            pass
        elif self.rank == 'Plantae':
            pass
        elif self.rank == 'Chromista':
            pass
        elif self.name == creature.name:
            pass
        elif self.rank == 'Protista':
            if creature.rank == 'Animalia':
                pass
            else:
                self.health += creature.health
                self.oxygen += creature.oxygen
                self.carbon += creature.carbon
                self.location = creature.location
                self.turtle.penup()
                self.turtle.goto(self.location[0], self.location[1])
                self.turtle.pendown()
                self.turtle.turtlesize(self.health / 100)
                creature.health = 0
                creature.die()
                print(f'{self.name} just ate {creature.name}!\n')
        elif self.rank == 'Fungi':
            if creature.rank == 'Eubacteria':
                self.health += creature.health
                self.oxygen += creature.oxygen
                self.carbon += creature.carbon
                self.location = creature.location
                self.turtle.penup()
                self.turtle.goto(self.location[0], self.location[1])
                self.turtle.pendown()
                self.turtle.turtlesize(self.health / 100)
                creature.health = 0
                creature.die()
                print(f'{self.name} just ate {creature.name}!\n')
            else:
                pass
        elif self.rank == 'Animalia':
            self.health += creature.health
            self.oxygen += creature.oxygen
            self.carbon += creature.carbon
            self.location = creature.location
            self.turtle.penup()
            self.turtle.goto(self.location[0], self.location[1])
            self.turtle.pendown()
            if self.health > 0:
                self.turtle.turtlesize(self.health / 100)
            creature.health = 0
            creature.die()
            print(f'{self.name} just ate {creature.name}!\n')

    def reproduce(self):
        if len(world.eubacteria) > 100:
            pass
        elif world.oxygen < 1000 or world.carbon < 1000:
            world.status()
            turtle.done()
        elif random.randint(0, 100) > 0:
            turtle.delay(0)
            i = Creature()
            j = Creature()
            i.location[0] = self.location[0] + 10
            i.location[1] = self.location[1] + 10
            j.location[0] = self.location[0] - 10
            j.location[1] = self.location[1] + 10
            i.move(i.location[0], i.location[1])
            j.move(j.location[0], j.location[1])
            i.turtle.showturtle()
            j.turtle.showturtle()
            turtle.delay(10)
            world.eubacteria.append(i)
            world.eubacteria.append(j)
            world.balance_life(i)
            world.balance_life(j)

    def attack(self, creature):
        (creature.health * .5) - 10
        if creature.health <= 0:
            creature.die()

    def die(self):
        if self.health == 0:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.eubacteria:
                world.eubacteria.remove(self)
            print(f'{self.name} has been eaten!')
        else:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.eubacteria:
                world.eubacteria.remove(self)
            print(f'{self.name} has died!')
            world.balance_death(self)

    def status(self):
        print(f'{self.name} has {self.health} health remaining. {self.name} has {self.elements} total resources.')

class Plantae(Creature):
    def __init__(self):
        super().__init__()
        self.turtle.color('green')
        self.rank = 'Plantae'
        self.health = 100
        self.oxygen = 100
        self.carbon = 100
        self.turtle.turtlesize(self.health/100)

    def die(self):
        if self.health == 0:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.plantae:
                world.plantae.remove(self)
            print(f'{self.name} has been eaten!')
        else:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.plantae:
                world.plantae.remove(self)
            print(f'{self.name} has died!')
            world.balance_death(self)

    def reproduce(self):

        if world.oxygen < 1000 or world.carbon < 1000:
            world.status()
            turtle.done()
        elif random.randint(0, 100) > 25:
            turtle.delay(0)
            i = Plantae()
            i.location[0] = self.location[0] + 10
            i.location[1] = self.location[1] + 10
            i.move(i.location[0], i.location[1])
            i.turtle.showturtle()
            turtle.delay(10)
            world.plantae.append(i)
            world.balance_life(i)

class Protista(Creature):
    def __init__(self):
        super().__init__()
        self.turtle.color('purple')
        self.rank = 'Protista'
        self.health = 100
        self.oxygen = 100
        self.carbon = 100
        self.turtle.turtlesize(self.health/100)

    def reproduce(self):
        if world.oxygen < 1000 or world.carbon < 1000:
            world.status()
            turtle.done()
        elif random.randint(0, 100) > 80:
            turtle.delay(0)
            i = Protista()
            i.location[0] = self.location[0] + 10
            i.location[1] = self.location[1] + 10
            i.move(i.location[0], i.location[1])
            i.turtle.showturtle()
            turtle.delay(10)
            world.protista.append(i)
            world.balance_life(i)

    def die(self):
        if self.health == 0:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.protista:
                world.protista.remove(self)
            print(f'{self.name} has been eaten!')
        else:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            print(world.protista)
            if self in world.protista:
                world.protista.remove(self)
            print(f'{self.name} has died!')
            world.balance_death(self)

class Animalia(Creature):
    def __init__(self):
        super().__init__()
        self.turtle.color('red')
        self.rank = 'Animalia'
        self.health = 100
        self.oxygen = 100
        self.carbon = 100
        self.turtle.turtlesize(self.health/100)

    def reproduce(self):
        if world.oxygen < 1000 or world.carbon < 1000:
            world.status()
            turtle.done()
        elif random.randint(0, 100) > 66:
            turtle.delay(0)
            i = Animalia()
            i.location[0] = self.location[0] + 10
            i.location[1] = self.location[1] + 10
            i.move(i.location[0], i.location[1])
            i.turtle.showturtle()
            turtle.delay(10)
            world.animalia.append(i)
            world.balance_life(i)

    def die(self):
        if self.health == 0:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.animalia:
                world.animalia.remove(self)
            print(f'{self.name} has been eaten!')
        else:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.animalia:
                world.animalia.remove(self)
            print(f'{self.name} has died!')
            world.balance_death(self)

class Chromista(Creature):
    def __init__(self):
        super().__init__()
        self.turtle.color('gold')
        self.rank = 'Chromista'
        self.health = 100
        self.oxygen = 100
        self.carbon = 100
        self.turtle.turtlesize(self.health/100)

    def reproduce(self):
        if world.oxygen < 1000 or world.carbon < 1000:
            world.status()
            turtle.done()
        elif random.randint(0, 100) > 50:
            turtle.delay(0)
            i = Chromista()
            i.location[0] = self.location[0] + 10
            i.location[1] = self.location[1] + 10
            i.move(i.location[0], i.location[1])
            i.turtle.showturtle()
            turtle.delay(10)
            world.chromista.append(i)
            world.balance_life(i)

    def die(self):
        if self.health == 0:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.chromista:
                world.chromista.remove(self)
            print(f'{self.name} has bean eaten!')
        else:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.chromista:
                world.chromista.remove(self)
            print(f'{self.name} has died!')
            world.balance_death(self)

class Fungi(Creature):
    def __init__(self):
        super().__init__()
        self.turtle.color('brown')
        self.rank = 'Fungi'
        self.health = 100
        self.oxygen = 100
        self.carbon = 100
        self.turtle.turtlesize(self.health / 100)

    def reproduce(self):
        if world.oxygen < 1000 or world.carbon < 1000:
            world.status()
            turtle.done()
        elif random.randint(0, 100) > 50:
            turtle.delay(0)
            i = Fungi()
            i.location[0] = self.location[0] + 10
            i.location[1] = self.location[0] + 10
            i.move(i.location[0], i.location[1])
            i.turtle.showturtle()
            turtle.delay(10)
            world.fungi.append(i)
            world.balance_life(i)

    def die(self):
        if self.health == 0:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.fungi:
                world.fungi.remove(self)
            print(f'{self.name} has bean eaten!')
        else:
            self.turtle.clear()
            self.turtle.color('blue')
            self.turtle.hideturtle()
            world.dead.append(self)
            if self in world.fungi:
                world.fungi.remove(self)
            print(f'{self.name} has died!')
            world.balance_death(self)

class World:

    # creatures = [Creature(), Protista(), Plantae(), Animalia(), Chromista(), Fungi()]

    def __init__(self):
        self.time = time.time()
        self.oxygen = 100000
        self.carbon = 100000
        self.elements = {'oxygen': self.oxygen, 'carbon': self.carbon}
        self.resources = {'land': 100, 'water': 50, 'air': 10000}
        self.eubacteria = []
        self.protista = []
        self.plantae = []
        self.animalia = []
        self.chromista = []
        self.fungi = []
        self.dead = []
        self.alive = [self.eubacteria, self.protista, self.plantae, self.animalia, self.chromista, self.fungi]
        self.text = turtle.Turtle()
        self.text.penup()
        self.text.goto(0, 400)
        self.text.write(f'{self.oxygen} Oxygen and {self.carbon} Carbon', align='center', font=("Comic Sans", 80, "normal"))
        self.text.hideturtle()
        self.duration = 0
        self.x = []
        self.y = []
        self.total_eubacteria = []
        self.total_animalia = []
        self.total_plantae = []
        self.total_protista = []
        self.total_fungi = []
        self.total_chromista = []
        self.totals = [self.total_animalia, self.total_eubacteria, self.total_chromista, self.total_fungi,
                       self.total_plantae, self.total_protista]

    def update(self):
        self.alive = [self.eubacteria, self.protista, self.plantae, self.animalia, self.chromista, self.fungi]

    def balance_life(self, creature):
        self.oxygen -= creature.oxygen
        self.carbon -= creature.carbon

    def balance_death(self, creature):
        self.oxygen += creature.oxygen
        self.carbon += creature.carbon

    def status(self):
        self.text.clear()
        self.text = turtle.Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.goto(0, 400)
        self.text.write(f'{self.oxygen} Oxygen and {self.carbon} Carbon', align='center',
                        font=("Comic Sans", 80, "normal"))
        self.text.hideturtle()
        print(f'\nThe World has {self.oxygen} Oxygen and {self.carbon} Carbon remaining.\n')
        for rank in self.alive:
            if len(rank) > 0:
                print(f'\nThere are {len(rank)} {rank[0].rank} in the world.\n')
        total = 0
        for rank in self.alive:
            total += len(rank)
        print(f'\n{total}: CREATURES REMAINING! and {len(world.dead)}: CREATURES DEAD\n')

    def graph(self):
        # Creatures alive per cycle graph
        self.duration += 1
        self.x.append(self.duration)
        self.y.append(len(self.eubacteria)+len(self.animalia)+len(self.protista)+len(self.plantae)+len(self.chromista)+
                      len(self.fungi))
        # plot the graph
        plt.plot(self.x, self.y, 'b')

        self.total_plantae.append(len(self.plantae))
        self.total_protista.append(len(self.protista))
        self.total_animalia.append(len(self.animalia))
        self.total_chromista.append(len(self.chromista))
        self.total_fungi.append(len(self.fungi))
        self.total_eubacteria.append(len(self.eubacteria))


        plt.plot(self.x, self.total_eubacteria, 'c')
        plt.plot(self.x, self.total_plantae, 'g')
        plt.plot(self.x, self.total_protista, 'b')
        plt.plot(self.x, self.total_animalia, 'r')
        plt.plot(self.x, self.total_chromista, 'y')
        plt.plot(self.x, self.total_fungi, 'k')

        plt.title('Autonomia')
        plt.ylabel('Total Creatures')
        plt.xlabel('Cycles')

        plt.show()
        time.sleep(.5)

    def populate(self):
        turtle.delay(0)
        for i in range(0, 10):
            i = Creature()
            self.eubacteria.append(i)
        for i in range(0, 10):
            i = Plantae()
            self.plantae.append(i)
            i = Chromista()
            self.chromista.append(i)
            i = Fungi()
            self.fungi.append(i)
        for i in range(0, 4):
            i = Protista()
            self.protista.append(i)
            i = Animalia()
            self.animalia.append(i)

        for rank in self.alive:
            for creature in rank:
                creature.turtle.showturtle()
                world.balance_life(creature)
        print('WORLD POPULATED')
        turtle.delay(10)

    def run(self):
        turtle.clearscreen()
        turtle.hideturtle()
        turtle.getscreen()

# populates world with initial creatures
        self.populate()

# world loop
        while True:

            self.update()
            self.status()
            self.graph()
            # turtle.delay(0)
# prints elapsed time and world status every loop
            elapsed_time = time.time() - self.time
            print(f'\n{elapsed_time}\n')

# checks if a certain amount of creatures have died and stops the program
#             if len(self.dead) > 500000:
#                 turtle.done()
            alive_ranks = ()
            if len(self.eubacteria) > 0:
                alive_ranks = self.eubacteria
            if len(self.protista) > 0:
                alive_ranks += self.protista
            if len(self.plantae) > 0:
                alive_ranks += self.plantae
            if len(self.animalia) > 0:
                alive_ranks += self.animalia
            if len(self.chromista) > 0:
                alive_ranks += self.chromista
            if len(self.fungi) > 0:
                alive_ranks += self.fungi
            random.shuffle(alive_ranks)

            for creature in self.eubacteria:
                self.update()
                c.execute("INSERT INTO creatures VALUES ('{}', '{}', '{}', '{}', '{}')".format(creature.rank,
                                                                                               creature.name,
                                                                                               creature.oxygen,
                                                                                               creature.carbon,
                                                                                               creature.location))
                conn.commit()
                creature.live()


world = World()

world.run()