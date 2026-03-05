# ============================================================
# Configuration file for the FireForest smoke detection project
# U-Net / ResNet architecture for binary image segmentation
# ============================================================

# Root directory containing the full dataset (origins + masks subdirectories)
DATA_PATH = '/home/adrien/Desktop/project/images3/images_day'

# Path to the original RGB images (input to the model)
ORIGIN_PATH = '/home/adrien/Desktop/project/images3/images_day/origins'

# Path to the binary mask images (ground truth segmentation labels)
MASK_PATH = '/home/adrien/Desktop/project/images3/images_day/masks'

# Images are resized to IMG_SIZE x IMG_SIZE pixels before being fed to the model.
# 256 strikes a balance between spatial resolution and GPU memory usage.
IMG_SIZE = 256

# Number of samples loaded manually (outside Keras generators) for quick tests
TRAIN_SIZE = 8

# Number of images used for inference visualisation / manual testing
INFERENCE_SIZE = 3

# Number of images per mini-batch during training
BATCH_SIZE = 8

# Number of images per mini-batch during validation
VAL_SIZE = 8
