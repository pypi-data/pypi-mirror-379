from setuptools import setup, find_packages
setup(
    name="Hafsa",
    version="1.0.5",
    author="Syeda Hafsa Tariq",
    author_email="hafsatariq987123@gmail.com",
    description="simple package",
    pakages=find_packages(),
    python_requires=">=3.6",
    entry_point={
        "console_scripts" : [
            "Hafsa=Hafsa.Hafsa:main"
        ],
    },
)
