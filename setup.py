# -------------------------------------------------------------------
# - NAME:        setup.py
# - AUTHOR:      Reto Stauffer
# - DATE:        2017-02-05
# - LICENSE: GPL-2, Reto Stauffer, copyright 2014
# -------------------------------------------------------------------
# - DESCRIPTION: The python-colorpsace package.
# -------------------------------------------------------------------
# - EDITORIAL:   2017-02-05, RS: Created file on thinkreto.
# -------------------------------------------------------------------
# - L@ST MODIFIED: 2018-09-17 15:53 on marvin
# -------------------------------------------------------------------


##from distutils.command.build import build
from setuptools import setup

setup(name="colorspace",     # This is the package name
      version = "0.1.0",            # Current package version, what else
      description = "Color space package for python",
      long_description = "Provides a set of color transformation functions and an interface to chose efficient color maps based on the HCL color space. This package is inspired and based on the R package 'colorspace'.",
      classifiers = [
        "Development Status :: 3 - Alpha",
        #"Development Status :: 4 - Beta",
        "GNU Lesser General Public License v2 (GPL-2)",
        "Programming Language :: Python :: 2.7",
      ],
      keywords = "colors HCL",
      url = "https://github.com/retostauffer/python-colorspace",
      maintainer = "Reto Stauffer",
      maintainer_email = "reto.stauffer@uibk.ac.at",
      author = "Reto Stauffer [aut,cre], Ross Ihaka [ctb], Paul Murrell [ctb], Kurt Hornik [ctb], Jason C. Fisher [ctb], Claus O. Wilke [ctb], Claire D. Mc White [ctb], Achim Zeileis [ctb]",
      license = "GPL-2",
      install_requires = ["numpy"],

      packages = ["colorspace"],
      include_package_data = True,
      czip_save = False)

