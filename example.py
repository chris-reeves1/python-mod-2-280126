# budget = 20

# milkshakes = {
#     "1": (3, "Whole"),
#     "2": (4, "choc"),
#     "3": (5, "vanilla")
# }

# while True:
#     print("drinks menu:")
#     for option, (price, flavour) in milkshakes.items():
#         print(f"{option} - {flavour} - ${price}")

    
#     choice = input("enter you choice of drink? ")

#     if choice not in milkshakes:
#         print("invalid choice")
#         continue

#     if choice.upper() == "Q":
#         print("bye")
#         break

#     price, flavour = milkshakes[choice]
#     if price > budget:
#         print("kicked out!")
#         break
    
#     print(f"enjoy {flavour} drink")
#     budget -= price
#     print(f"budget is now {budget}")

# typing module
# typedDict
# dataclass

# 


# from typing import TypedDict, Dict

# class Shake(TypedDict):
#     price: int
#     flavour: str

# milkshakes: Dict[str, Shake] = {
#     "1": {3, "Whole"},
#     "2": {"price": 4, "flavour": "choc"},
#     "3": {"price": 5, "flavour": "vanilla"}
# }


# from dataclasses import dataclass

# @dataclass
# class Shake:
#     price: int
#     flavour: str
