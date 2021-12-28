import SOC
import torch
def Pooling(x):
    x=SOC.Covpool.forward(x)
    x=SOC.Sqrtm.forward(x,3)
    x=SOC.MeanPooling.forward(x)
    return x
if __name__ == '__main__':
    tensor = torch.randn(10,2048, 14, 14)
    result=torch.unsqueeze(torch.unsqueeze(Pooling(tensor),dim=2),dim=3)
    print(result.shape)