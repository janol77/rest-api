from setuptools import find_packages, setup

setup(name="rest-api",
      version = "0.1",
      description = "flask-rest-api",
      author = "Alejandro Medina",
      platforms = ["any"],
      license = "GPLv3",
      include_package_data=True,
      packages = find_packages(),
      install_requires = ["Flask==0.11.1",
                          "mongoengine==0.10.6",
                          "flask-mongoengine==0.8",
                          "gunicorn==19.6.0"],
      )
