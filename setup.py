import setuptools

data = {
    "name" : "femail",
    "version" : "1.0.0",
    "description" : 'The python (fe)Mail Client',
    "author" : "CodewarsNL",
    "classifiers" : "Development Status :: 3 - Production",
    "platforms": "Posix",
    "packages": setuptools.find_packages(),
    "namespace_packages": [],
    "install_requires": ["requests", "jinja2"],
    "extras_require": {},
    "python_requires": ">=3.6.*",
    "include_package_data": True,
    "zip_safe": False
}

setuptools.setup(**data)