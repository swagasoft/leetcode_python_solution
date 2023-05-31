from typing import List

def rocket_launched(rocket_pos: List[int], rocket_speed: List[int], base_point):
    
    while (base_point < 50): # at max 50 steps i will conclude there is no meeting point
      for index, rocket_num in enumerate(rocket_pos): # loop through rocket number
        rocket_pos[index] = rocket_num + rocket_speed[index] # increment rocket number by it given speed

      base_point += 1 #increment base  point
      if rocket_pos[0] == rocket_pos[1]: # check if there is a meeting between both rocket
        return 1 # both rocket has combine to 1
    
    return 2 # after 50 attempt, no meeting point for both rocket
        
        

    


rocket_pos = [3, 11]
rocket_speed = [5, 1]
# rocket_pos = [2, 3]
# rocket_speed = [1, 2]

print(rocket_launched(rocket_pos, rocket_speed, 0))
      



        



