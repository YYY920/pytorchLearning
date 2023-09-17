from torch.utils.data import Dataset
from PIL import Image
import matplotlib.pyplot as plt
import os


class MyData(Dataset):
    def __init__(self, root_dir, label_dir):

    def __getitem__(self, id):

    def __len__(self):


root_dir = " "
bees_label_dir = ""
bees_dataset = MyData(root_dir, bees_label_dir)
img, label = bees_dataset[0]
plt.imshow(img)
plt.show()
