from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your dependencies here, e.g.
        'flask',
        # Add other libraries your app uses
    ],
    entry_points={
        'console_scripts': [
            'emotiondetection=app:main',  
        ],
    },
    author='Your Name',
    description='Emotion Detection AI Application',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
    ],
)