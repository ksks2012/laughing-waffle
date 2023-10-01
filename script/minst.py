import torch
import numpy as np
import torchvision as TV
import matplotlib.pyplot as plt

from typing import Any
from torch import nn

PATH = "./ai_model/model_minst"


class CNN(torch.nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, kernel_size=(3, 3))
        self.conv2 = nn.Conv2d(16, 32, kernel_size=(3, 3))
        self.maxpool = nn.MaxPool2d(kernel_size=(2, 2))
        self.lin1 = nn.Linear(800, 128)
        self.out = nn.Linear(128, 10)  # flatten output of CNN

    def forward(self, x):
        x = self.conv1(x)
        x = nn.functional.relu(x)  # use ReLU
        x = self.maxpool(x)
        x = self.conv2(x)
        x = nn.functional.relu(x)
        x = self.maxpool(x)
        x = x.flatten(start_dim=1)  # flatten
        x = self.lin1(x)
        x = nn.functional.relu(x)
        x = self.out(x)
        x = nn.functional.log_softmax(x, dim=1)
        return x


class MINSTModel:
    def __init__(self) -> None:
        self.download_dataset()

    def download_dataset(self):
        self.train_data = TV.datasets.MNIST(
            "MNIST/", train=True, transform=None, target_transform=None, download=True
        )
        self.test_data = TV.datasets.MNIST(
            "MNIST/", train=False, transform=None, target_transform=None, download=True
        )

        print("Number of samples in train_data is: ", len(self.train_data))
        print("Number of samples in test_data is: ", len(self.test_data))

    def prepare_images(self, xt):  # preprocess
        out = torch.zeros(xt.shape)
        for i in range(xt.shape[0]):
            img = xt[i].unsqueeze(dim=0)
            out[i] = img
        return out

    def train_model(self):
        self.model = CNN()
        epochs = 100
        batch_size = 500
        lr = 1e-3
        opt = torch.optim.Adam(params=self.model.parameters(), lr=lr)
        lossfn = nn.NLLLoss()

        self.losses = []
        self.acc_CNN = []

        for i in range(epochs):
            print("Current training epoch: ", i)
            opt.zero_grad()
            batch_ids_CNN = np.random.randint(0, 60000, size=batch_size)
            xt = self.train_data.data[batch_ids_CNN].detach()
            xt = self.prepare_images(xt).unsqueeze(dim=1)
            yt = self.train_data.train_labels[batch_ids_CNN].detach()
            pred = self.model(xt)
            pred_labels = torch.argmax(pred, dim=1)
            acc_ = 100.0 * (pred_labels == yt).sum() / batch_size
            print("Current training accuracy: ", acc_.item())
            self.acc_CNN.append(acc_)
            loss = lossfn(pred, yt)
            print("Current training loss: ", loss.item())
            self.losses.append(loss)
            loss.backward()
            opt.step()

    def test_model(self):
        test_id = np.random.randint(0, 10000, size=10)

        xt = self.test_data.data[test_id].detach()
        print(type(self.test_data.data[test_id]), type(xt))
        xt = self.prepare_images(xt).unsqueeze(dim=1)
        preds = self.model(xt)
        pred_ind = torch.argmax(preds.detach(), dim=1)
        pred_ind = pred_ind.numpy()

        for i in range(10):
            x = self.test_data.data[test_id[i]]
            plt.imshow(x)
            print("\nThe number below is", pred_ind[i])
            plt.pause(0.05)

    def save_model(self):
        torch.save(self.model.state_dict(), PATH)

    def load_model(self):
        self.model = CNN()
        self.model.load_state_dict(torch.load(PATH))
        self.model.eval()

    def recognize_number(self, image):
        height, width = image.shape

        dst = np.zeros((height, width), np.uint8)
        for i in range(height):
            for j in range(width):
                dst[i, j] = 255 - image[i, j]
        image = dst

        import cv2

        cv2.imwrite("./TRAINING_POWER_minst.png", image)

        image = np.array(image).astype(np.float32)
        image = np.expand_dims(image, 0)
        image = np.expand_dims(image, 0)  # extend to [1，1，28，28]
        image = torch.from_numpy(image)
        # input = torch.from_numpy(image)
        # input = self.prepare_images(input).unsqueeze(dim=1)
        # print(type(input))
        preds = self.model(image)
        pred_ind = torch.argmax(preds.detach(), dim=1)
        pred_ind = pred_ind.numpy()
        print("\nThe number below is", pred_ind[0])


if __name__ == "__main__":
    num_model = MINSTModel()
    num_model.train_model()
    num_model.test_model()
    num_model.save_model()
    # num_model.load_model()
