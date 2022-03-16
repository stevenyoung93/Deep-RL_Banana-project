 # Deep-RL_Banana-project

The goal of this project is to train an agent to navigate the 'Banana Collector'-environment and learn to get an average score of at least +13 over 100 consecutive episodes. 

## Project environment
### General 
The environment used is similar to UnityML's Banana Collector environment, provided by Udacity. 

The applied environment can be downloaded here: TBD

### Environment details
The environment is a finite square world with borders. Within this world, there are blue and yellow bananas at randomly distributed locations:
- States: The state space has 37 dimensions
  - Agent's velocity
  - Ray-based perception of objects around agent's forward direction (sight)
- Actions: The action space is discrete and has four dimensions
  - Move forward, backward
  - Turn left, right
- Rewards: Rewards are provided upon collection of a banana
  - Blue banana provides reward of -1
  - Yellow banana provides reward of +1
- Solved: This environment is ended by a max number of timesteps per episode, e.g., later defined in the DQN model

## Method

The approach of my implementation considers the following elements:
- Reinforcement learning (no prior knowledge for the agent about the environment, rewards or policies)
- Application of reinforcement learning parameters to handle exploration-exploitation trade-off:
  - Epsilon-greedy policies
  - Learning rate
- Combination of deep learning with reinforcement learning -> Deep reinforcement learning (representation of the action-value function Q as neural network instead of classical Q-table)
  - Neural network with two hidden layers (Input with 37 nodes for states -> 128-node-fc-layer -> ReLU -> 64-node-fc-layer -> ReLU -> Dropout p=0.4 -> 4-node-fc-layer for actions)
- Application of stabilizing techniques to converge and efficiently approach optimal value function q*
  - Experience replay memory
  - Fixed Q-targets
  - Dropout layer

## 	Instructions for installing dependencies or downloading needed files.
- numpy
- Install Unityagents
- torch

## 	How to run the code in the repository, to train the agent
tbd
