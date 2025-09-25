from setuptools import setup, find_packages

setup(
    name="students_management",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="A simple student management system",
    author="Shakhnazar Sailaukan",
    author_email="shakhnazar.sailaukan@gmail.com",
    python_requires=">=3.6",
)
