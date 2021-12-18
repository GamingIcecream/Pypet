import asyncio
data = {
    'name': str("Ace"),
    'happiness': 0,
    'hungry': True,
    'normal': "υ´•ﻌ•`υ",
    'peace': "u´˘ﻌ˘`u",
}
time = 0

async def waitwalk():
    while True:
        await asyncio.sleep(1)
        time += 1

print("Ace is sitting at your feet. " + data['normal'])
while True:
    if data['happiness'] <= 0:
        data['hungry'] = True
        print("WAN! FOOD!")
    else:
        data['hungry'] = False
    match input("> "):
        case "feed":
            print("You feed " + data['name'] + " some dog food. They wag their tail happily.")
        case "stats":
            print("")
        case "name":
            print("Choose a name for your pypet.")
            data['name'] = input()
            print("Your pypet's name is now " + data['name'] + ".")
        case "exit":
            print("Are you sure you want to leave " + data['name'] + "? (y to exit)")
            match input():
                case "y":
                    print("You walk away from " + data['name'] + ", and he whines. Come back soon!")
                    exit()
                case "n":
                    print("Phew! You wouldn't want to leave a pet behind, would ya?")
                case _:
                    print("You are deciding on leaving when " + data['name'] + " clings onto your leg.")
                    print("You decide to stay.")
        case _:
            print(data['name'] + " tilts their head in confusion.")
