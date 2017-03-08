import random
import numpy as np
import matplotlib.pyplot as plt
import deepmind_lab
import gym
from gym import spaces

def _action(*entries):
  return np.array(entries, dtype=np.intc)


class DeepMindEnv:
  def __init__(self, level):
    width, height, fps = 256, 256, 60
    self.deep_env = deepmind_lab.Lab(
      level, ['RGB_INTERLACED'],
      config={
          'fps': str(fps),
          'width': str(width),
          'height': str(height)
      })

    self.action_space = spaces.Discrete(11)
    self.observation_space = spaces.Box(low=0, high=255, shape=(height, width, 3))
    self.reward_range = None

    self.ACTIONS = {
      'look_left': _action(-20, 0, 0, 0, 0, 0, 0),
      'look_right': _action(20, 0, 0, 0, 0, 0, 0),
      'look_up': _action(0, 10, 0, 0, 0, 0, 0),
      'look_down': _action(0, -10, 0, 0, 0, 0, 0),
      'strafe_left': _action(0, 0, -1, 0, 0, 0, 0),
      'strafe_right': _action(0, 0, 1, 0, 0, 0, 0),
      'forward': _action(0, 0, 0, 1, 0, 0, 0),
      'backward': _action(0, 0, 0, -1, 0, 0, 0),
      'fire': _action(0, 0, 0, 0, 1, 0, 0),
      'jump': _action(0, 0, 0, 0, 0, 1, 0),
      'crouch': _action(0, 0, 0, 0, 0, 0, 1)
  }

  def step(self, index):
    obs = self.deep_env.observations()
    # print('obs: ',obs)
    # print('i: ',index)
    # print('action: ', self.ACTIONS.values()[index])
    reward = self.deep_env.step(self.ACTIONS.values()[index], num_steps=1)
    # print('reward: ', reward)
    # print('done: ', self.deep_env.is_running())
    done = self.deep_env.is_running()
    return obs['RGB_INTERLACED'], reward, done

  def reset(self):
    self.deep_env.reset()

  def render(self):
    pass

  def close(self):
    pass

  def configure(self, *args, **kwargs):
    pass

  def seed(self, seed=None):
    pass




env = DeepMindEnv('tests/demo_map')
env.seed(0)
env.reset()

#allow gym code to use deepmind lab
#passing an index is discrete
for i in range(10):
    ob = env.reset()
    for j in range(1000):
        action = (env.action_space).sample()
        ob, reward, done = env.step(action)
        assert ob.shape == env.observation_space.sample().shape, 'If this fails, you have the wrong observation space'
  
        print i, ob, reward
        if done:
            break
env.close()


'''
class RandomAgent(object):

  ACTIONS = {
      'look_left': _action(-20, 0, 0, 0, 0, 0, 0),
      'look_right': _action(20, 0, 0, 0, 0, 0, 0),
      'look_up': _action(0, 10, 0, 0, 0, 0, 0),
      'look_down': _action(0, -10, 0, 0, 0, 0, 0),
      'strafe_left': _action(0, 0, -1, 0, 0, 0, 0),
      'strafe_right': _action(0, 0, 1, 0, 0, 0, 0),
      'forward': _action(0, 0, 0, 1, 0, 0, 0),
      'backward': _action(0, 0, 0, -1, 0, 0, 0),
      'fire': _action(0, 0, 0, 0, 1, 0, 0),
      'jump': _action(0, 0, 0, 0, 0, 1, 0),
      'crouch': _action(0, 0, 0, 0, 0, 0, 1)
  }

  ACTION_LIST = ACTIONS.values()

  def step(self, unused_reward, unused_image):
    return random.choice(RandomAgent.ACTION_LIST)



def run(length, width, height, fps, level):
  env = deepmind_lab.Lab(
      level, ['RGB_INTERLACED'],
      config={
          'fps': str(fps),
          'width': str(width),
          'height': str(height)
      })

  env.reset()
  agent = RandomAgent()

  reward = 0

  for _ in xrange(length):
    if not env.is_running():
      print('Environment stopped early')
      env.reset()
      agent.reset()
    obs = env.observations()
    action = agent.step(reward, obs['RGB_INTERLACED'])
    reward = env.step(action, num_steps=1)
    plt.imshow(obs['RGB_INTERLACED'])
    plt.show()

if __name__ == '__main__':
  run(100, 280, 280, 60, 'tests/demo_map')
'''





# length = 100
# width = 256
# height = 256
# fps = 60
# level = 'tests/demo_map'
# env = deepmind_lab.Lab(
#     level, ['RGB_INTERLACED'],
#     config={
#         'fps': str(fps),
#         'width': str(width),
#         'height': str(height)
#     })

# env.reset()
# obs = env.observations()
# print('obs: ', obs)