# custom-files/reward-fn-examples/reward-fn-follow-the-center-line.py

# This example determines how far away the agent is from the center line and gives higher reward
# if it is closer to the center of the track. It will incentivize the agent to closely follow the
# center line.

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = abs(params['steering_angle'])  # Absolute steering angle
    speed = params['speed']  # Current speed of the agent

    # Calculate dynamic markers based on track width
    marker_1 = 0.05 * track_width
    marker_2 = 0.2 * track_width
    marker_3 = 0.4 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.8
    elif distance_from_center <= marker_3:
        reward = 0.5
    else:
        reward = 0.1  # likely crashed/ close to off track

    # Incorporate steering angle and speed to encourage smooth driving
    steering_penalty = max(0.0, (steering_angle - 15.0) / 30.0)  # Penalize excessive steering
    speed_penalty = max(0.0, (3.0 - speed) / 3.0)  # Penalize low speed
    reward *= (1.0 - 0.3 * steering_penalty - 0.2 * speed_penalty)

    return float(reward)
