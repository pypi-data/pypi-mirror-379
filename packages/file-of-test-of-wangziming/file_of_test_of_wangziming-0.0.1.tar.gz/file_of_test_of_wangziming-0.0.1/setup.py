import setuptools

setuptools.setup(
    name="file_of_test_of_wangziming",
    version="0.0.1",
    author="王梓明",
    author_email="1272660211@qq.com",
    description="这是一个测试项目，测试成功。",
    long_description="这是一个测试项目，测试成功。",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    #package_data={'': ['*.yaml']} # 包含MANIFEST.in里的文件
    package_data={'': []},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
)