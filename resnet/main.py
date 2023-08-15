import torch

#should be more careful but importing everything
from model import *
from utils import *
from data import *
from train import *
from export import *

n_outputs = 3 #how many classes to predict
batch_size = 64
n_epochs = 30
print_freq = 1

torch.manual_seed(1234) #fix seed for reproducibility
device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

net, transform = get_resnet()
add_head(net, n_outputs)

criterion, optimizer = get_crit_opt(net)
ds_train, ds_test, dl_train, dl_test = get_ds_dl(transform, batch_size)

net, optimizer = train(n_epochs,
                       net, 
                       dl_train,
                       dl_test,
                       criterion, 
                       optimizer, 
                       print_freq,
                       device)

export_to_onnx(net, ds_train[0][0].unsqueeze(0).shape, device)
