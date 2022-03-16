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

![image](https://user-images.githubusercontent.com/23191357/158647094-dbb301b1-00ce-4243-b65e-2ff235b0b216.png)


Hyperparameters:
- a 
- b
- 

## Plot of Rewards

A plot of rewards per episode is included to illustrate that the agent is able to receive an average reward (over 100 episodes) of at least +13. The submission reports the number of episodes needed to solve the environment.

## Ideas for Future Work

The submission has concrete future ideas for improving the agent's performance.
- Prioritized experience replay
- Dueling DQN or Rainbow
