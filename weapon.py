class Weapon:
    def __init__(self,
                name: str,
                weapon_type: str,
                damage: int,
                value: int
                ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

iron_sword = Weapon(name="Iron sword",
                    weapon_type="sharp",
                    damage=5,
                    value=10)

short_bow = Weapon(name="Short bow",
                    weapon_type="ranged",
                    damage=3,
                    value=8)

fists = Weapon(name="Fists",
                    weapon_type="sharp",
                    damage=2,
                    value=0)

spider_trident = Weapon(name="Spider trident",
                    weapon_type="sharp",
                    damage=20,
                    value=20)
        
