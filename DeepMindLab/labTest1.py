import random
import numpy as np

import deepmind_lab


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

  print('Finished after %i steps. Total reward received is %f'
        % (length, agent.rewards))


if __name__ == '__main__':
  run(100, 80, 80, 60, 'tests/demo_map')




# import random
# import numpy as np
# import matplotlib.pyplot as plt
# import deepmind_lab

# # def _action(*entries):
# #   return np.array(entries, dtype=np.intc)

# # class RandomAgent(object):

# #   ACTIONS = {
# #       'look_left': _action(-20, 0, 0, 0, 0, 0, 0),
# #       'look_right': _action(20, 0, 0, 0, 0, 0, 0),
# #       'look_up': _action(0, 10, 0, 0, 0, 0, 0),
# #       'look_down': _action(0, -10, 0, 0, 0, 0, 0),
# #       'strafe_left': _action(0, 0, -1, 0, 0, 0, 0),
# #       'strafe_right': _action(0, 0, 1, 0, 0, 0, 0),
# #       'forward': _action(0, 0, 0, 1, 0, 0, 0),
# #       'backward': _action(0, 0, 0, -1, 0, 0, 0),
# #       'fire': _action(0, 0, 0, 0, 1, 0, 0),
# #       'jump': _action(0, 0, 0, 0, 0, 1, 0),
# #       'crouch': _action(0, 0, 0, 0, 0, 0, 1)
# #   }

# #   ACTION_LIST = ACTIONS.values()

# #   def step(self, unused_reward, unused_image):
# #     return random.choice(RandomAgent.ACTION_LIST)



# # def run(length, width, height, fps, level):
# length = 100
# width = 280
# height = 280
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
# #agent = RandomAgent()

# # run(100, 280, 280, 60, 'tests/demo_map')
