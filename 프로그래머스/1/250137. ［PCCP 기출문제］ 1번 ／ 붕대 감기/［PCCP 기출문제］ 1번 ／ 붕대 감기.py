def solution(bandage, health, attacks):
    time = 0
    serial = 0
    atk = 0
    atkTime=len(attacks)
    first_hp = health
    while health != -1:
        time += 1
        serial += 1
        
        if attacks[atk][0] == time:
            health = health - attacks[atk][1]
            serial = 0
            atk += 1
        else:
            health = health + bandage[1]

            if serial == bandage[0]:
                health = health + bandage[2]
                serial = 0

            if health > first_hp:
                health = first_hp
        if health <= 0:
            health = -1
            break
            
        if attacks[atkTime-1][0] <= time:
            break
            
    answer = health
    return answer