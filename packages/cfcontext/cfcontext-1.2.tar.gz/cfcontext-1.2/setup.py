from setuptools import setup

setup(
    name="cfcontext",  # Nom de votre package
    version="1.2",       # Version de votre package
    py_modules=["cfcontext"],  # Nom du fichier (sans extension) contenant votre module
    author="Jimw",
    author_email="jimmy.c@jimw.fr",
    description="`cfcontext` is a lightweight library for managing shared contexts within a Python application. It allows you to create, replace, and handle dynamic contextual objects that are inherited across the call stack frames, ensuring consistency throughout nested function calls and asynchronous tasks.",
    url="https://git.jimw.fr/cfcontext",  # URL du projet (facultatif)
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers"
    ],
    python_requires='>=3.6',
)
