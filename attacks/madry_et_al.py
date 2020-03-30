"""
The MadryEtAl attack
"""

from cleverhansl2l.attacks.projected_gradient_descent import ProjectedGradientDescent


class MadryEtAl(ProjectedGradientDescent):
  def __init__(self, model, sess=None, dtypestr='float32', **kwargs):
    super(MadryEtAl, self).__init__(model, sess=sess,
                                    dtypestr=dtypestr,
                                    default_rand_init=True,
                                    **kwargs)
