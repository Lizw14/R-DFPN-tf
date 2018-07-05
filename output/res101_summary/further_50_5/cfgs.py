# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import os

"""
Test
3.4w iters 2000 images
12000 2000 nms
R: 0.744025157233
P: 0.775353646276
mAP: 0.5843414523
F: 0.759366416392
3000 300 nms
R: 0.776100628931
P: 0.760150046641
mAP: 0.596233094459
F: 0.768042531939

8w iters 2000 images
12000 2000 nms
R: 0.804402515723
P: 0.811959672345
mAP: 0.657771231522
F: 0.80816342763

3000 300 nms
R: 0.794968553459
P: 0.839605285273
mAP: 0.671949256727
F: 0.816677452305

水平标准：
12000 2000 nms
R: 0.835849056604
P: 0.859430049235
mAP: 0.723505658855
F: 0.847475549479

3000 300 nms
R: 0.825471698113
P: 0.872015924138
mAP: 0.723763655682
F: 0.848105701914
"""

# root path
ROOT_PATH = os.path.abspath(r'/var/lzw/thesis/tf/R-DFPN_FPN_Tensorflow')

# pretrain weights path
TEST_SAVE_PATH = ROOT_PATH + '/tools/test_result'
INFERENCE_IMAGE_PATH = ROOT_PATH + '/tools/inference_image'
INFERENCE_SAVE_PATH = ROOT_PATH + '/tools/inference_result'

NET_NAME = 'resnet_v1_101'
VERSION = 'further_50_5'
CLASS_NUM = 1
BASE_ANCHOR_SIZE_LIST = [50, 150, 250, 350, 500]
LEVEL = ['P2', 'P3', 'P4', 'P5', 'P6']
POOL_STRIDE = [4., 8., 16., 32., 64]
ANCHOR_STRIDE = [4., 8., 16., 32., 64]
ANCHOR_SCALES = [1.]
ANCHOR_RATIOS = [1/5., 5., 1/7., 7., 1/9, 9]
ANCHOR_ANGLES = [-90, -75, -60, -45, -30, -15]
SCALE_FACTORS = [10., 10., 5., 5., 5.]
SHORT_SIDE_LEN = 600
DATASET_NAME = 'ship'  # 'ship', 'spacenet', 'pascal', 'coco'
NUM_RECT_PARAMETERS = 5
IOU_USE_GPU = True
NMS_USE_GPU = True
RPN_TRAIN = False

BATCH_SIZE = 1
WEIGHT_DECAY = {'resnet_v1_50': 0.0001, 'resnet_v1_101': 0.0001}
EPSILON = 1e-5
MOMENTUM = 0.9
MAX_ITERATION = 80000
LR = 0.001
#LR = 0.0001
GPU_GROUP = "3"

# rpn
SHARE_HEAD = False
RPN_NMS_IOU_THRESHOLD = 0.7
MAX_PROPOSAL_NUM = 2000
RPN_IOU_POSITIVE_THRESHOLD = 0.5
RPN_IOU_NEGATIVE_THRESHOLD = 0.2
RPN_MINIBATCH_SIZE = 512
RPN_POSITIVE_RATE = 0.5
IS_FILTER_OUTSIDE_BOXES = False
RPN_TOP_K_NMS = 12000
RPN_ANCHOR_ANGLES_THRESHOLD = 15.0
RPN_NMS_ANGLES_THRESHOLD = 15.0
KERNEL_SIZE = 5
FEATURE_PYRAMID_MODE = 0  # {0: 'feature_pyramid', 1: 'build_dense_feature_pyramid'}
USE_HORIZONTAL_NMS = False
RPN_USE_ANGLE_CONDITION = False

# fast rcnn
ROI_SIZE = 14
ROI_POOL_KERNEL_SIZE = 2
USE_DROPOUT = False
KEEP_PROB = 0.5
FAST_RCNN_NMS_IOU_THRESHOLD = 0.15
FAST_RCNN_NMS_MAX_BOXES_PER_CLASS = 100
FINAL_SCORE_THRESHOLD = 0.8
FAST_RCNN_IOU_POSITIVE_THRESHOLD = 0.4
FAST_RCNN_MINIBATCH_SIZE = 256
FAST_RCNN_POSITIVE_RATE = 0.5
FAST_RCNN_TOP_K_NMS = False
FAST_RCNN_BOXES_ANGLES_THRESHOLD = 15.0
FAST_RCNN_NMS_ANGLES_THRESHOLD = 15.0
NEED_AUXILIARY = False
FAST_RCNN_USE_ANGLE_CONDITION = False
USE_MASK = False
MULTI_SCALE_POOL = False