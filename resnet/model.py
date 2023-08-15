from torchvision.models import resnet18, ResNet18_Weights

def get_resnet():
    net = resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
    transform = ResNet18_Weights.IMAGENET1K_V1.transforms()

    return net, transform
