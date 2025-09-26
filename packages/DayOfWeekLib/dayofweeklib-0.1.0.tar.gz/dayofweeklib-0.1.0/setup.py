from setuptools import setup, find_packages

setup(
    name="DayOfWeekLib",
    version="0.1.0",
    description="Get day of the week from a date",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Nesma Mohamad  Al-Btry",
    author_email="nasmhalbtri23@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    entry_points={"console_scripts": ["dayofweeklib=day_of_week_lib.main:main"]},
)
