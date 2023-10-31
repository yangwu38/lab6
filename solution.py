import math
#from render import InitRender, Render

G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]

def calculate_distance(body1, body2):
    _, (x1, y1), _ = body1
    _, (x2, y2), _ = body2
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx**2 + dy**2)

    return distance
    pass

def calculate_force(body1, body2):
    mass1, (x1, y1), _ = body1
    mass2, (x2, y2), _ = body2
    dx = x2 - x1
    dy = y2 - y1
    r = math.sqrt(dx**2 + dy**2)
    magnitude = (G * mass1 * mass2) / (r**2)
    force_x = magnitude * (dx / r)
    force_y = magnitude * (dy / r)
    return (force_x, force_y)
    pass
    

def calculate_net_force_on(body, system):
    net_force_x = 0.0
    net_force_y = 0.0
    mass1, (x1, y1), _ = body
    for other_body in system:
        if other_body != body:
            mass2, (x2, y2), _ = other_body
            dx = x2 - x1
            dy = y2 - y1
            r = math.sqrt(dx**2+dy**2)
            magnitude = (G * mass1 * mass2) / (r**2)
            force_x = magnitude * (dx / r)
            force_y = magnitude * (dy / r)
            net_force_x += force_x
            net_force_y += force_y
    return (net_force_x, net_force_y)
    pass

def calculate_acceleration(body, system):
   mass, _, _ = body
   net_force_x, net_force_y = calculate_net_force_on(body, system)
   acceleration_x = net_force_x / mass
   acceleration_y = net_force_y / mass
   return (acceleration_x, acceleration_y)
   pass


def update_velocity(system, dt):
    updated_system = []
    for body in system:
        mass, (x, y), (vx, vy) = body
        (ax, ay) = calculate_acceleration(body, system)
        new_vx = vx + ax * dt
        new_vy = vy + ay * dt
        updated_body = (mass, (x, y), (new_vx, new_vy))
        updated_system.append(updated_body)
    return updated_system
    pass
   

def update(system, dt):
    updated_system = update_velocity(system, dt)
    for i, body in enumerate(updated_system):
        (mass, (x, y), (vx, vy)) = body
        new_x = x + vx * dt
        new_y = y + vy * dt
        updated_body = (mass, (new_x, new_y), (vx, vy))
        updated_system[i] = updated_body
    return updated_system  
    pass

def simulate(system, dt, num_steps):
    for _ in range(num_steps):
        system = update(system, dt)
    return system
    pass

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    pass

if __name__ == '__main__':
    pass





