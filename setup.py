from setuptools import setup, find_packages

setup(
    name="libpyfoscamcgi",  
    version="0.0.9",  
    author="Foscam-wangzhengyu",  
    author_email="wangzhengyu@foscam.com",
    url='https://github.com/Foscam-wangzhengyu/libfoscamcgi',
    description="foscam camera cgi", 
    install_requires=["defusedxml"],
    include_package_data=True,
    license='LGPLv3+'    
)
