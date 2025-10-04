import gymnasium as gym

# Breakout environment
env = gym.make("Breakout-v5", render_mode="human")

obs = env.reset()
done = False

while not done:
    action = env.action_space.sample()  # random action for now
    obs, reward, done, truncated, info = env.step(action)

env.close()
