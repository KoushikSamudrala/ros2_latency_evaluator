from setuptools import find_packages, setup

package_name = 'latency_evaluator'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='koushik',
    maintainer_email='koushik@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
    'console_scripts': [
        'ping_node = latency_evaluator.ping_node:main',
        'pong_node = latency_evaluator.pong_node:main',
    ],
},
)
