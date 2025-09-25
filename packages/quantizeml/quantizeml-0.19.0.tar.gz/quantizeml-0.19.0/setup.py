from os import path
from setuptools import setup, find_packages
from platform import platform


# Read the contents of the README file
directory = path.abspath(path.dirname(__file__))
with open(path.join(directory, 'README'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='quantizeml',
      version='0.19.0',
      description='Base layers and quantization tools',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Kevin Tsiknos',
      author_email='ktsiknos@brainchip.com',
      maintainer='Kevin Tsiknos',
      maintainer_email='ktsiknos@brainchip.com',
      url='https://doc.brainchipinc.com',
      license='Apache 2.0',
      license_files=['LICENSE'],
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'quantizeml = quantizeml.cli:main',
        ]
      },
      install_requires=['tensorflow>=2.15.0, <2.16.0', 'keras>=2.15.0, <2.16.0',
                        'onnx==1.16.1', 'onnxruntime~=1.19.0', 'onnxscript==0.2.5',
                        'matplotlib<3.9', 'tensorboardX<2.6.1', 'onnxruntime_extensions<0.14.0',
                        'scipy'],
       extras_require={
          'test': ['pytest', 'pytest-rerunfailures', 'pytest-console-scripts'],
      },
      python_requires='>=3.9')
