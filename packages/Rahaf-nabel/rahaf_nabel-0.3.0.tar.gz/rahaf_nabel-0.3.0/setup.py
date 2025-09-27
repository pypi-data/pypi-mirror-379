from setuptools import setup, find_packages

setup(
    name='Rahaf_nabel',  # غيّره لاسم فريد
    version='0.3.0',
    author='Rahaf Nabel',  # غيّره لاسمك
    author_email='your.email@example.com',  # بريدك
    description='باكيج بايثون بسيط يحتوي على دوال ترحيب وجمع ',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mypackage',  # غيّره لرابط مشروعك
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # لازم تحط LICENSE فعلاً
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
