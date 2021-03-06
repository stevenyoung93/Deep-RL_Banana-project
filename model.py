import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed, fc1_units=128, fc2_units=64):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
            fc1_units (int): # of nodes in 1st hidden layer
            fc2_units (int): # of nodes in 2nd  hidden layer
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)

        
        # initialize for linear transformation of the layers
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc2_drop = nn.Dropout(p=0.4)
        self.fc3 = nn.Linear(fc2_units, action_size)



    def forward(self, state):
        """Build a network that maps state -> action values."""
        # activation after 1st hidden layer
        x = F.relu(self.fc1(state))
        # activation after 2nd hidden layer
        x = F.relu(self.fc2(x))
        # dropout
        x = self.fc2_drop(x)
        # return after 3rd layer w/o activation func
        return self.fc3(x)
