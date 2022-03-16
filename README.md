 # Deep-RL_Banana-project

## General 
The goal of this project is to train an agent to navigate the 'Banana Collector'-environment and learn to get an average score of at least +13 over 100 consecutive episodes. 

## Project environment
The environment used is similar to UnityML's Banana Collector environment, provided by Udacity (see below).

<img width="398" alt="Bildschirmfoto 2022-03-16 um 16 48 40" src="https://user-images.githubusercontent.com/23191357/158631214-219431d1-dced-4dfa-a484-d5f68520a6db.png">

The applied environment can be downloaded from this repository: https://github.com/udacity/Value-based-methods.git (which was also cloned into this git repo).

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
  - Neural network with two hidden layers 
- Application of stabilizing techniques to converge and efficiently approach optimal value function q*
  - Experience replay memory
  - Fixed Q-targets
  - Dropout layer

## 	Instructions for installing dependencies or downloading needed files.
- Make sure to use Python v3.6 (I set up a separate environment in my Anaconda to run this)
- Install packages:
  - numpy
  - torch
- Clone and extract this git repository which includes the environment (unityagents)

## 	How to run the code in the repository, to train the agent
- Follow instructions above to install dependencies and do required download
- Open the notebook "Navigation" in the folder "p1_navigation"
- Run all cells in shown order
- Notebook include options to (re-)train the model, or to load the trained model and replay without further learning
- Hyperparameters can be adjusted when calling the dqn function

## Results
Results are reported and documented in Report.md
