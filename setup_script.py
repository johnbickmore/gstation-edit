#!/usr/bin/env python

VERSION='0.5'

from distutils.core import setup, Extension

setup(  name='gstation-edit',
        version=VERSION,
        description='GTK replacement for Johnson J-Station J-Edit.',
        author='F Laignel',
        author_email='fengalin@free.fr',
        url='http://sourceforge.net/projects/gstation-edit/',
        license='GNU General Public License version 3.0 (GPLv3)',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: X11 Applications',
            'Intended Audience :: End Users/Desktop',
            'License :: GNU General Public License version 3.0 (GPLv3)',
            'Operating System :: Linux',
            'Programming Language :: Python',
            'Topic :: Multimedia :: Sound/Audio',
            'Translations :: English',
            'User Interface :: GTK+',
            ],
        packages=["gstation_edit", "gstation_edit"],
        package_dir={"gstation_edit": "gstation_edit/"},
        scripts = ['gstation_edit/gstation-edit'],
        data_files=[('share/gstation-edit', ['README.md', 'ChangeLog', 'COPYING',
                     'NEWS', 'AUTHORS',
                     "gstation_edit/resources/gstation-edit-one-window.ui"]),
                    ('share/applications', ['gstation-edit.desktop'])]
  )