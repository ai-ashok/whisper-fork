from setuptools import setup, find_packages


setup(
    name="whisper",
    py_modules=["whisper"],
    version="1.0",
    description="Robust Speech Recognition via Large-Scale Weak Supervision",
    readme="README.md",
    python_requires=">=3.7",
    author="OpenAI",
    url="https://github.com/openai/whisper",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        "console_scripts": ["whisper=whisper.transcribe:cli"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
