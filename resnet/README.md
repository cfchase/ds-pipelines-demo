### Training

`python main.py`

### Inference

```
from export import *

run(model_fname, img_fname, transform)
```

where model_fname is the onnx file, img_fname is the png image, transform is the PyTorch image transformation (using the resnet one for now)
