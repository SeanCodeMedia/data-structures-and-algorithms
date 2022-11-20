from setuptools import  setup


setup(
      name="merge sort test",
      version=1,
      entry_points={
        'console_scripts':['merge_sort=merge_sort:main'],
      },

)