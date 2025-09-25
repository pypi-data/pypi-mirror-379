from setuptools import setup

with open("README.md") as file:
    read_me_description = file.read()

setup(
    name='asynctoolspy',
    version='1.0',
    packages=['asynctoolspy'],
    url='https://gitlab.com/asurnovsurnov/asynctoolspy/',
    author='Aleksei Surnov',
    author_email='asurnovsurnov@gmail.com',
    description='asynctoolspy is a set of simple tools to speed up Python async development. It includes the appoint_limit_async decorator to limit how often an async function can be called by setting max attempts and intervals, useful for APIs with rate limits. The decorator handles errors with retries and pauses to improve reliability. It also features AsyncIterWrapper, an async iterator supporting optional delays and sync/async callbacks for flexible data processing.',
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',

)