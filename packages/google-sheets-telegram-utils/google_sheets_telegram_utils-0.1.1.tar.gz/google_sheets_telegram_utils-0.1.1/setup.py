from setuptools import setup, find_packages

setup(
    name='google-sheets-telegram-utils',
    version='0.1.1',
    description='A package with utils to work with google spreadsheet and telegram bots',
    url='https://github.com/alexVarkalov/google_sheets_telegram_utils',
    author='Alexander Varkalov',
    author_email='alex.varkalov@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot==22.4',
        'python-dotenv==1.1.1',
        'google-api-python-client==2.183.0',
        'google-auth-oauthlib==1.2.2',
        'gspread==6.2.1',
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Other Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
    ],
)
