class Solution:
    def survivedRobotsHealths(positions, healths, directions):
        robots = sorted([(positions[i], healths[i], directions[i]) for i in range(len(positions))])
        
        right_moving = []
        survivors = [] 
        
        for pos, health, direction in robots:
            if direction == 'L':
                while right_moving and health > 0:
                    _, r_health = right_moving[-1]
                    if health > r_health:
                        health -= 1
                        right_moving.pop()
                    elif health < r_health:
                        right_moving[-1][1] -= 1
                        health = 0
                    else:
                        right_moving.pop()
                        health = 0
                if health > 0:
                    survivors.append((pos, health, direction))
            else:
                right_moving.append([pos, health])
        
        for pos, health in right_moving:
            survivors.append((pos, health, 'R'))
        
        survivors.sort(key=lambda x: positions.index(x[0]))
        
        return [health for _, health, _ in survivors]
        