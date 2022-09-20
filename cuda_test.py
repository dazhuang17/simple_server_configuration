import torch

# pytorch测试文件

x_ones = torch.ones((2,3)).cuda()
print(f"Ones Tensor: \n {x_ones} \n")
print(torch.cuda.is_available())
print(torch.backends.cudnn.is_available())
print(torch.version.cuda)
print(torch.version.cudnn)


