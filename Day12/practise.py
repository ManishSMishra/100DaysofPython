##################### Scope #####################:
# Global Scope
enemies=20

def increase_enemies():
    global enemies
    enemies=15
    print(f" enemies in function {enemies}")

increase_enemies()
print(f" enemies outside function {enemies}")
