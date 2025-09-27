# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.56
""" setup of ae namespace module portion templates: ae.templates. """
# noinspection PyUnresolvedReferences
import sys
print(f"SetUp {__name__=} {sys.executable=} {sys.argv=} {sys.path=}")

# noinspection PyUnresolvedReferences
import setuptools

setup_kwargs = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [       'Development Status :: 3 - Alpha', 'Natural Language :: English', 'Operating System :: OS Independent',
        'Programming Language :: Python', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9', 'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed'],
    'description': 'ae namespace module portion templates: ae.templates',
    'extras_require': {       'dev': [       'aedev_project_tpls', 'ae_ae', 'anybadge', 'coverage-badge', 'aedev_git_repo_manager', 'flake8',
                       'mypy', 'pylint', 'pytest', 'pytest-cov', 'pytest-django', 'typing', 'types-setuptools'],
        'docs': [],
        'tests': [       'anybadge', 'coverage-badge', 'aedev_git_repo_manager', 'flake8', 'mypy', 'pylint', 'pytest',
                         'pytest-cov', 'pytest-django', 'typing', 'types-setuptools']},
    'install_requires': [],
    'keywords': ['configuration', 'development', 'environment', 'productivity'],
    'license': 'GPL-3.0-or-later',
    'long_description': ('<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project ae.ae v0.3.97 -->\n'
 '<!-- THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.namespace_root_tpls v0.3.19 -->\n'
 '# templates 0.3.1\n'
 '\n'
 '[![GitLab develop](https://img.shields.io/gitlab/pipeline/ae-group/ae_templates/develop?logo=python)](\n'
 '    https://gitlab.com/ae-group/ae_templates)\n'
 '[![LatestPyPIrelease](\n'
 '    https://img.shields.io/gitlab/pipeline/ae-group/ae_templates/release0.3.1?logo=python)](\n'
 '    https://gitlab.com/ae-group/ae_templates/-/tree/release0.3.1)\n'
 '[![PyPIVersions](https://img.shields.io/pypi/v/ae_templates)](\n'
 '    https://pypi.org/project/ae-templates/#history)\n'
 '\n'
 '>ae namespace module portion templates: ae.templates.\n'
 '\n'
 '[![Coverage](https://ae-group.gitlab.io/ae_templates/coverage.svg)](\n'
 '    https://ae-group.gitlab.io/ae_templates/coverage/index.html)\n'
 '[![MyPyPrecision](https://ae-group.gitlab.io/ae_templates/mypy.svg)](\n'
 '    https://ae-group.gitlab.io/ae_templates/lineprecision.txt)\n'
 '[![PyLintScore](https://ae-group.gitlab.io/ae_templates/pylint.svg)](\n'
 '    https://ae-group.gitlab.io/ae_templates/pylint.log)\n'
 '\n'
 '[![PyPIImplementation](https://img.shields.io/pypi/implementation/ae_templates)](\n'
 '    https://gitlab.com/ae-group/ae_templates/)\n'
 '[![PyPIPyVersions](https://img.shields.io/pypi/pyversions/ae_templates)](\n'
 '    https://gitlab.com/ae-group/ae_templates/)\n'
 '[![PyPIWheel](https://img.shields.io/pypi/wheel/ae_templates)](\n'
 '    https://gitlab.com/ae-group/ae_templates/)\n'
 '[![PyPIFormat](https://img.shields.io/pypi/format/ae_templates)](\n'
 '    https://pypi.org/project/ae-templates/)\n'
 '[![PyPILicense](https://img.shields.io/pypi/l/ae_templates)](\n'
 '    https://gitlab.com/ae-group/ae_templates/-/blob/develop/LICENSE.md)\n'
 '[![PyPIStatus](https://img.shields.io/pypi/status/ae_templates)](\n'
 '    https://libraries.io/pypi/ae-templates)\n'
 '[![PyPIDownloads](https://img.shields.io/pypi/dm/ae_templates)](\n'
 '    https://pypi.org/project/ae-templates/#files)\n'
 '\n'
 '\n'
 '## installation\n'
 '\n'
 '\n'
 'execute the following command to install the\n'
 'ae.templates module\n'
 'in the currently active virtual environment:\n'
 ' \n'
 '```shell script\n'
 'pip install ae-templates\n'
 '```\n'
 '\n'
 'if you want to contribute to this portion then first fork\n'
 '[the ae_templates repository at GitLab](\n'
 'https://gitlab.com/ae-group/ae_templates "ae.templates code repository").\n'
 'after that pull it to your machine and finally execute the\n'
 'following command in the root folder of this repository\n'
 '(ae_templates):\n'
 '\n'
 '```shell script\n'
 'pip install -e .[dev]\n'
 '```\n'
 '\n'
 'the last command will install this module portion, along with the tools you need\n'
 'to develop and run tests or to extend the portion documentation. to contribute only to the unit tests or to the\n'
 'documentation of this portion, replace the setup extras key `dev` in the above command with `tests` or `docs`\n'
 'respectively.\n'
 '\n'
 'more detailed explanations on how to contribute to this project\n'
 '[are available here](\n'
 'https://gitlab.com/ae-group/ae_templates/-/blob/develop/CONTRIBUTING.rst)\n'
 '\n'
 '\n'
 '## namespace portion documentation\n'
 '\n'
 'information on the features and usage of this portion are available at\n'
 '[ReadTheDocs](\n'
 'https://ae.readthedocs.io/en/latest/_autosummary/ae.templates.html\n'
 '"ae_templates documentation").\n'),
    'long_description_content_type': 'text/markdown',
    'name': 'ae_templates',
    'package_data': {'': []},
    'packages': ['ae'],
    'project_urls': {       'Bug Tracker': 'https://gitlab.com/ae-group/ae_templates/-/issues',
        'Documentation': 'https://ae.readthedocs.io/en/latest/_autosummary/ae.templates.html',
        'Repository': 'https://gitlab.com/ae-group/ae_templates',
        'Source': 'https://ae.readthedocs.io/en/latest/_modules/ae/templates.html'},
    'python_requires': '>=3.9',
    'url': 'https://gitlab.com/ae-group/ae_templates',
    'version': '0.3.1',
    'zip_safe': True,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass
