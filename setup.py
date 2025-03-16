from setuptools import setup, find_packages

setup(
        name="POO",
    version="0.0.1",
    author="JUAN MAURICIO OSPINA",
    author_email="Juan.ospina68@est.iudigital.edu.co",
    description="buenas practicas de la PAD",
    py_modules=["actividad_1"],
    install_requires=
    [
        "kagglehub[pandas-datasets]>=0.3.8",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "scipy",
        "pandas",
        "numpy",
        "openpyxl",
        "requests"
    ]
)