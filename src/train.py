import gymnasium as gym

# Breakout environment
env = gym.make("Breakout-v5", render_mode="human")
obs, info = env.reset()
done = False

while not done:
    action = env.action_space.sample()  # random action
    obs, reward, terminated, truncated, info = env.step(action)
    print("Reward:", reward, "Terminated:", terminated, "Truncated:", truncated)
    done = terminated or truncated

env.close()
