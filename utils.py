import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from sklearn.metrics import accuracy_score

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return torch.tensor(self.X[idx], dtype=torch.float32), torch.tensor(self.y[idx], dtype=torch.float32)

class SingleTaskNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SingleTaskNN, self).__init__()
        self.shared_hidden = nn.Linear(input_dim, hidden_dim)
        self.output = nn.Linear(hidden_dim, output_dim)
    
    def forward(self, x):
        x = F.relu(self.shared_hidden(x))
        return self.output(x)
    def train_model(self, train_loader, criterion, optimizer, epochs=5):
        self.train() 
        for epoch in range(epochs):
            for data, target in train_loader:
                optimizer.zero_grad()  
                output = self(data).squeeze() 
                loss = criterion(output, target) 
                loss.backward()  
                optimizer.step()  
                
            print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')


class MultiTaskNN(nn.Module):
    def __init__(self, shared_hidden, output_heads):
        super(MultiTaskNN, self).__init__()
        self.shared_hidden = shared_hidden
        self.output_heads = nn.ModuleList(output_heads)
    
    def forward(self, x, task_id):
        x = F.relu(self.shared_hidden(x))
        if 0 <task_id <= len(self.output_heads):
            return self.output_heads[task_id-1](x)
        else:
            raise ValueError(f"Invalid task_id: should be between 0 and {len(self.output_heads)-1}")




def test_model(model, dataloader, criterion, task_id=None):
    model.eval()
    total_loss = 0
    predictions, true_values = [], []
    print('Initiating Stats')
    with torch.no_grad():
        for data, target in dataloader:
            if task_id is not None:
                output = model(data, task_id).squeeze()

            else:
                output = model(data).squeeze()
            loss = criterion(output, target)
            total_loss += loss.item()
            predictions.extend(torch.sigmoid(output).numpy())
            true_values.extend(target.numpy())

    avg_loss = total_loss / len(dataloader)
    predictions = (np.array(predictions) > 0.5).astype(int)
    metric = accuracy_score(true_values, predictions)

    return avg_loss, metric




def check_thres(mt_accuracy: float, mt_loss: float, st_accuracy: float, st_loss: float, accuracy_threshold: float, loss_threshold: float) -> bool:

    print('Checking Conditions')

    accuracy_pass = mt_accuracy >= (st_accuracy * accuracy_threshold) and mt_accuracy>=0.82
    loss_pass = mt_loss <= (st_loss * loss_threshold) and mt_loss<=0.5
    return accuracy_pass and loss_pass

def save_model(model, path):

    torch.save(model.state_dict(), path)
    print(f"Model saved at: {path}")


