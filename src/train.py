import gymnasium as gym

env = gym.make("Breakout-v5", render_mode="human")
obs = env.reset()
done = False

while not done:
    action = env.action_space.sample()  # random action
    obs, reward, done, truncated, info = env.step(action)
    print("Reward:", reward)  # console lo reward kanipistundi

env.close()
