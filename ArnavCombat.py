import random
import time

class Player:
    def __init__(self, name, playerClass):
        self.name = name
        self.playerClass = playerClass
        self.moveSets = []
        self.hp = 100
        self.attack = 10
        self.gold = 5

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100

class Animal:
    def __init__(self, type, name, owner):
        self.type = type
        self.name = name
        self.owner = owner
        self.hp = 100
class RandomEvents:
    def __init__(self):
        self.enemyNames = list(enemyData.keys())

    def random_spawn(self, enemy_count):
        enemies = []
        for n in range(enemy_count):
            enemies.append(Player(f"Enemy_{n}", random.choice(self.enemyNames)))
        return enemies

    def random_damage(self, min_dmg, max_dmg):
        return random.randint(min_dmg, max_dmg)

    def random_heal(self, min_heal, max_heal):
        return random.randint(min_heal, max_heal)

# Define classes, animals, and skills
classes = [
    "Warrior", "Wizard", "Archer", "Rogue", "Cleric", "Druid", "Builder",
    "Necromancer", "Bard", "Sorcerer", "Monk"
]

classData = {
    "Warrior": ["Slash", "Shield Block", "Rush Attack", "Rage"],
    "Wizard": ["Fireball", "Lightning Bolt", "Heal", "Ice Shards"],
    "Archer": ["Rope Arrow", "Ambusher", "Fire Arrows", "Explosive Arrows"],
    "Rogue": ["Sneak Attack", "Poison Blade", "Ambusher", "Invisibility"],
    "Cleric": ["Heal", "Poison", "Stethoscope Whip", "Revive"],
    "Druid": ["Transform", "Camouflage", "Summon Animal", "Bleed"],
    "Builder": ["Build", "Repair", "Reinforce", "Explode"],
    "Necromancer": ["Summon Undead", "Blood Magic", "Curse", "Burn"],
    "Bard": ["Cure Wounds", "Illusion", "Mind Reading", "See Invisibility"],
    "Sorcerer": ["Fire Bolt", "Shocking Grasp", "Acid Splash", "Ray of Frost"],
    "Monk": ["Multiattack", "Wind Attack", "Meditation", "Mind Cleanse"],
    "Arnavs Totally Not Secret Password 76": ["Kill All", "Steal Hero", "Win", "Steal Gold"]
}

animalData = {
    "Dog": ["Bite", "Lick", "Poop"],
    "Cat": ["Scratch", "Climb", "Meow"],
    "Fox": ["Steal", "Sneak Attack", "Trap"],
    "Wolf": ["Bite", "Howl", "Pounce"],
    "Bear": ["Bite", "Dinner", "Scratch"],
    "Lion": ["Bite", "Roar", "Bloody Slash"],
    "Tiger": ["Growl", "Pounce", "Slash"],
    "Horse": ["Dash", "Stampede", "Tail Whip"],
}

HealingSkills = [
    "Meow", "Heal", "Lick", "Revive", "Cure Wounds", "Meditation",
    "Mind Cleanse"
]
DmgIncreaseSkills = ["Growl", "Howl", "Roar", "Rage"]
SpecialSkills = [
    "Illusion", "Mind Reading", "See Invisibility", "Summon Undead",
    "Steal Gold", "Build", "Repair", "Reinforce"
]

DmgSkills = [
    "Bite", "Roar", "Bloody Slash", "Stampede", "Tail Whip", "Pounce",
    "Sneak Attack", "Scratch", "Slash", "Rush Attack", "Fireball",
    "Lightning Bolt", "Ice Shards", "Multiattack", "Stethoscope Whip",
    "Fire Arrows", "Explosive Arrows", "Poison Blade", "Ambusher", "Bleed",
    "Kill All", "Steal Hero", "Acid Splash", "Ray of Frost", "Poison",
    "Fire Breath", "Shocking Grasp", "Rock Throw", "Rock Smash", "Earthquake",
    "Snipe", "Shoot", "Stab", "Mace Smash", "Wind Attack", "Burn", "Curse"
]

enemyData = {
    "Goblin": ["Slash", "Stab", "Steal"],
    "Orc": ["Slash", "Stab", "Run"],
    "Troll": ["Slash", "Stab", "Mace Smash"],
    "Giant": ["Stomp", "Jump", "Slap"],
    "Dragon": ["Bite", "Fly", "Fire Breath"],
    "Golem": ["Rock Throw", "Rock Smash", "Earthquake"],
    "Ghost": ["Fade", "Haunt", "Curse"],
    "Skeleton": ["Shoot", "Rebuild", "Snipe"],
    "Zombie": ["Bite", "Infect", "Undead"],
    "Vampire": ["Bite", "Blood Rage", "Drain"],
    "Werewolf": ["Bite", "Full Moon", "Howl"],
    "Witch": ["Poison", "Curse", "Heal"]
}

secret = "arnavs totally not secret password 76"

print("=" * 30)
print("      || Arnav Combat ||")
print("=" * 30)

print("Welcome to Arnav Combat!")
username = input("Enter your username: ")


# Show available classes
for i, class_name in enumerate(classes, start=1):
    print(f"{i}. {class_name}")

# Player class selection
userClass = input("Enter your class: ").title()
if userClass in ["Necromancer", "Sorcerer"]:
    print(f"Do you want to buy a {userClass} for 5 gold? (yes/no)")
    user_input = input().lower()
    if user_input == "yes":
        print(f"You have bought a {userClass} for 5 gold")
        # player.gold -= 5
    else:
        print(f"You have not bought a {userClass}")
        userClass = ''

if userClass not in classes and userClass != "Arnavs Totally Not Secret Password 76":
    print(f"Sorry, {userClass} is not a valid class.")
    exit(0)
else:
    print(f"{userClass} is what you selected!")
    player = Player(username, userClass)
    player.moveSets = classData.get(userClass, [])

print("-" * 30)

# Show available animals
for animal in animalData.keys():
    print(animal)

# Animal selection
animalChoice = input("Choose an animal: ").title()
if animalChoice not in animalData:
    print(f"Sorry, {animalChoice} is not a valid animal.")
else:
    print(f"{animalChoice} is what you selected!")
    animal = Animal(animalChoice, "Animal #1", player.name)

# Initialize players and enemies
Shaab = Player("Shaan", "Sorcerer")
arnav = Player("Arnav", "Necromancer")
Aj = Player("Aj", "Monk")

randomEvents = RandomEvents()
enemyTeam = randomEvents.random_spawn(4)
team = [Shaab, arnav, Aj, player]

print("="*50)

import pygame  
import time 
import random 
pygame.init()
white = (255, 255, 255) 
yellow = (255, 255, 102) 
black = (0, 0, 0) 
red = (213, 50, 80) 
green = (0, 255, 0) 
blue = (50, 153, 213)
display;dimensions 
dis_width = 800 
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Arnav Combat')


# Game loop
while team and enemyTeam:
    # Player's turn
    for person in team[:]:  # iterate over a copy of the list
        if person.hp <= 0:
            print(f"{person.name} has been defeated!")
            team.remove(person)
            continue

        enemyWeAreAttacking = random.choice(enemyTeam)
        
        if len(person.moveSets) > 0:
            randomAttack = random.choice(person.moveSets)
        else:
            randomAttack = ""

        if randomAttack in DmgSkills:
            randomDamage = randomEvents.random_damage(5, 15)
            print(f"{person.name} ({person.hp}) is attacking {enemyWeAreAttacking.name} with {randomAttack} for {randomDamage} damage")
            enemyWeAreAttacking.take_damage(randomDamage)
        elif randomAttack in HealingSkills:
            randomHealAmount = randomEvents.random_heal(5, 10)
            print(f"Healing {person.name} for {randomHealAmount} HP")
            person.heal(randomHealAmount)
        else:
            print(f"{person.name} ({person.hp}) casted {randomAttack}")
            time.sleep(0.5)
    
    time.sleep(1)

    # Enemies' turn
    for enemy in enemyTeam[:]:  # iterate over a copy of the list
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")
            enemyTeam.remove(enemy)
            continue

        enemyAttack = random.choice(enemyData[enemy.playerClass])
        if enemyAttack in DmgSkills:
            randomDamage = randomEvents.random_damage(5, 15)
            if len(team) == 0:
                print("Game Over")
                break
                
            target = random.choice(team)
            print(f"{enemy.name} is attacking {target.name} with {enemyAttack} for {randomDamage} damage")
            target.take_damage(randomDamage)
        elif enemyAttack in HealingSkills:
            randomHealAmount = randomEvents.random_heal(5, 10)
            print(f"{enemy.name} is healing for {randomHealAmount} HP")
            if enemyTeam:  # Healing is only done if there are still enemies to heal
                random.choice(enemyTeam).heal(randomHealAmount)
        else:
            print(f"{enemy.name} casted {enemyAttack}")
            time.sleep(0.5)

    print("\n\n")
    time.sleep(1)
