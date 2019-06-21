from distutils.core import setup

setup(
    name='pykachu',  # How you named your package folder (MyLib)
    packages=['pykachu'],  # Chose the same as "name"
    version='0.3',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Pikachu interpreter written in Python',  # Give a short description about your library
    author='Dany Lewin',  # Type in your name
    author_email='danyglewin@gmail.com',  # Type in your E-Mail
    url='https://github.com/DanyGLewin/pykachu',  # Provide either the link to your github or to your website
    download_url='https://github.com/DanyGLewin/pykachu/archive/V0.3.tar.gz',  # I explain this later on
    keywords=['Esolang', 'Esoteric', 'Language', 'Pokemon', 'Pikachu', 'Interpreter'],  # Keywords that define your package best
    install_requires=[  # I get to this in a second
        'click',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Interpreters',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 2.7',  # Specify which python versions that you want to support
    ],
)
