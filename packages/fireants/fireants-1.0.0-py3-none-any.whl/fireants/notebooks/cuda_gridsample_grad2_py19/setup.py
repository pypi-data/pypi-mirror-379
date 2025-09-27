from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension, CUDAExtension
setup(
    name='cuda_gridsample_grad2',
    ext_modules=[
        CUDAExtension(
            name='gridsample_grad2',
            sources=['gridsample_cuda.cpp', './gridsample_cuda_mod.cu']),
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)
