from abc import ABCMeta
import collections
import warnings
import numpy as np
from six.moves import xrange
import tensorflow as tf

from cleverhansl2l import utils
from cleverhansl2l.attacks.attack import Attack
from cleverhansl2l.attacks.basic_iterative_method import BasicIterativeMethod
from cleverhansl2l.attacks.carlini_wagner_l2 import CarliniWagnerL2
from cleverhansl2l.attacks.deep_fool import DeepFool
from cleverhansl2l.attacks.elastic_net_method import ElasticNetMethod
from cleverhansl2l.attacks.fast_feature_adversaries import FastFeatureAdversaries
from cleverhansl2l.attacks.fast_gradient_method import FastGradientMethod, fgm, optimize_linear
from cleverhansl2l.attacks.lbfgs import LBFGS
from cleverhansl2l.attacks.madry_et_al import MadryEtAl
from cleverhansl2l.attacks.max_confidence import MaxConfidence
from cleverhansl2l.attacks.momentum_iterative_method import MomentumIterativeMethod
from cleverhansl2l.attacks.noise import Noise
from cleverhansl2l.attacks.projected_gradient_descent import ProjectedGradientDescent
from cleverhansl2l.attacks.saliency_map_method import SaliencyMapMethod
from cleverhansl2l.attacks.semantic import Semantic
from cleverhansl2l.attacks.spsa import SPSA, projected_optimization
from cleverhansl2l.attacks.spatial_transformation_method import SpatialTransformationMethod
from cleverhansl2l.attacks.virtual_adversarial_method import VirtualAdversarialMethod, vatm
from cleverhansl2l.model import Model, CallableModelWrapper
from cleverhansl2l.model import wrapper_warning, wrapper_warning_logits
from cleverhansl2l.compat import reduce_sum, reduce_mean
from cleverhansl2l.compat import reduce_max
from cleverhansl2l.compat import softmax_cross_entropy_with_logits
from cleverhansl2l.utils_tf import clip_eta
from cleverhansl2l import utils_tf

_logger = utils.create_logger("cleverhans.attacks")
tf_dtype = tf.as_dtype('float32')
