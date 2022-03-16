# Report: Description of the implementation.

## Algorithm walkthrough

- Instantiate the agent
- Initialize empty scores list for tracking, and hyperparameter epsilon
- Run through episodes, number defined by hyperparameter n_episodes
  - Reset the environment and turn on train-mode
  - Get the initial state
  - Initialize a score for this instance at 0
  - Start iterating through episode until done (end defined by hyperparameter max_t)
    - Select action epsilon-greedy based on Q network and send it to the environment
    - Receive reward, done and next state
    - Update the score 
    - Save experience (s, a, r, s', d) in replay memory and learn from it every t'th step, defined as hyperparameter (if the experience memory is larger than the batch size)
      - Clone the local Q network into an identical but separated Q_target, to fixate the learning parameters that don't change during the learning step
      - Learn by minimizing the MSE loss between Q_expected and Q_target, where:
        - Q_expected is received from local model
        - Q_target = rewards + gamma * Q_target(next_state)
      - Optimizer uses gradient descent with Adam optimizer and a soft update with hyperparameter tau
    - Roll over to the next state
  - Append and occasionally print scores for monitoring of learning process
  - Decay epsilon down to hyperparameter eps_end
- Save trained DQN model to a pth-file
- return scores

## Learning Algorithm
Neural network architecture: Two hidden layers, only fully connected and activation
- 37-nodes-input-layer (for states)
- 128-nodes-fc-layer
- ReLU
- 64-nodes-fc-layer
- ReLU
- Dropout p=0.4
- 4-nodes-fc-layer (for actions)

<img width="497" alt="image" src="https://user-images.githubusercontent.com/23191357/158647180-acce75a3-87ad-4c40-8bc8-c35b080a8127.png">

Hyperparameters:
- n_episodes = 2000, number of episodes
- max_t = 300, number of timesteps per episode
- eps_start = 1.0, eps_end = 0.01, eps_decay = 0.095, epsilon values for epsilon-greedy policy
- BATCH_SIZE = 64, minibatch size for experience replay
- GAMMA = 0.99, discount factor for future expected reward
- TAU = 1e-3, learning factor for soft update of target parameters (Q_target and Q_local updates)
- alpha = LR = 5e-4, learning rate
- UPDATE_EVERY = 4, how frequent (in terms of steps) to update the Q network

## Plot of Rewards
<img width="497" alt="image" src="https://user-images.githubusercontent.com/23191357/158651893-f3f356f1-865b-4d0e-b365-2d834a6c6265.png">

The plot shows that the agent was able to receive an average reward over 100 episodes of +16.3 after 2.000 episodes. The agent was able to surpass the minimium requirement of +13 after 393 episodes.

## Ideas for Future Work

Future ideas for improving the agent's performance:
- Conduct more hyperparameter tuning
- Implement prioritized experience replay
- Enhance NN architecture (e.g., Dueling DQN or Rainbow)
