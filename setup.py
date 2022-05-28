from setuptools import setup, find_packages

setup(
    name="cgroups-exporter",
    version="0.4.6",
    include_package_data=True,
    license="Apache Software License",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Dmitry Orlov",
    author_email="me@mosquito.su",
    url="https://github.com/mosquito/cgroups-exporter",
    project_urls={
        "Source": "https://github.com/mosquito/cgroups-exporter/",
        "Tracker": "https://github.com/mosquito/cgroups-exporter/issues",
        "Say Thanks!": "https://saythanks.io/to/me%40mosquito.su",
    },
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.8.*, <4",
    install_requires=[
        "ConfigArgParse~=1.4",
        "aiochannel~=1.0",
        "aiohttp~=3.7.4",
        "aiomisc~=16.0",
        "async-timeout~=3.0",
        "attrs~=21.2",
        "chardet~=4.0",
        "colorlog~=5.0",
        "idna~=3.2",
        "multidict~=5.1",
        "prometheus-client~=0.10",
        "typing-extensions==3.10.0.0",
        "yarl~=1.6",
    ],
    entry_points={
        "console_scripts": ["cgroups-exporter = cgroups_exporter.__main__:main"]
    },
)
