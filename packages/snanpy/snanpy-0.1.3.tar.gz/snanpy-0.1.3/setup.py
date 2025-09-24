from distutils.core import setup
setup(
  name = 'snanpy',
  packages = ['snanpy'],
  version = '0.1.3', 
  license='MIT',
  description = 'Ein privates Package mit einigen Quality of Life Funktionen, die ich über die Zeit schreibe',   # Give a short description about your library
  author = 'Antonius Tilgner',                   # Type in your name
  author_email = 'antonius.tilgner@proton.me',      # Type in your E-Mail
  url = 'https://github.com/snantilg/snanpy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/snantilg/snanpy/archive/refs/tags/v0.1.2.tar.gz',    # I explain this later on
  keywords = ['private'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'matplotlib',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
