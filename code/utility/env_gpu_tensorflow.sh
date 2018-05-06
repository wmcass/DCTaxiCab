#!/bin/bash

module purge

module load Anaconda3/5.0.1
module load cuda/8.0
module load ImageMagick
module load graphviz

which python
which nvcc
which display
which dot

source activate tensorflow

export MKL_THREADING_LAYER=GNU
export THEANO_FLAGS='device=cuda,floatX=float32,force_device=True'
