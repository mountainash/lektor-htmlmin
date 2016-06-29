from setuptools import setup

setup(
    name='lektor-htmlmin',
    description='HTML minifier for Lektor. Based on htmlmin.',
     url='https://github.com/vesuvium/lektor-htmlmin',
    version='0.2',
    author=u'Jacopo Cascioli',
    author_email='jacopocascioli@gmail.com',
    license='MIT',
    py_modules=['lektor_htmlmin'],
    entry_points={
        'lektor.plugins': [
            'htmlmin = lektor_htmlmin:HTMLMinPlugin',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['htmlmin', 'chardet']
)
