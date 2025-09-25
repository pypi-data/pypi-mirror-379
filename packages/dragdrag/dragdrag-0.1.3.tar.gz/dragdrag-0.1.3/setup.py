from setuptools import setup, find_packages

setup(
    name='dragdrag',
    version='0.1.3',
    description='局域网文件拖拽上传/下载/删除的Web应用',
    author='linmy',
    author_email='657894692@qq.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Werkzeug'
    ],
    entry_points={
        'console_scripts': [
            'dragdrag=dragdrag.app:main'
        ]
    },
    package_data={
        'dragdrag': ['templates/*.html'],
    },
    python_requires='>=3.6',
) 