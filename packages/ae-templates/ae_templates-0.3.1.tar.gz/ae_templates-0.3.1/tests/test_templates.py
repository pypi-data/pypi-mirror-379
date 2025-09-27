""" ae.templates unit tests """
import os
import sys
import textwrap

import pytest
from tests.conftest import skip_gitlab_ci

from ae.base import (
    DEF_PROJECT_PARENT_FOLDER, PY_EXT, TEMPLATES_FOLDER,
    norm_name, norm_path, os_path_basename, os_path_isdir, os_path_isfile, os_path_join, read_file, write_file)
from ae.shell import (
    GIT_CLONE_CACHE_CONTEXT, GIT_VERSION_TAG_PREFIX, PROJECT_VERSION_SEP,
    get_main_app, project_name_version, temp_context_cleanup, temp_context_folders)
try:
    from ae.dev_ops import MODULE_PRJ, ROOT_PRJ  # no circular imports, although ae.dev_ops import from ae.templates
except ModuleNotFoundError:
    MODULE_PRJ = 'module'
    ROOT_PRJ = 'namespace-root'

from ae.templates import (
    LOCK_EXT, OUTSOURCED_FILE_NAME_PREFIX, OUTSOURCED_MARKER, CACHED_TPL_PROJECTS, SKIP_IF_PORTION_DST_NAME_PREFIX,
    SKIP_PRJ_TYPE_FILE_NAME_PREFIX, TPL_FILE_NAME_PREFIX, TPL_PATH_OPTION_SUFFIX, TPL_STOP_CNV_PREFIX,
    TPL_VERSION_OPTION_SUFFIX, TEMPLATE_PLACEHOLDER_ID_PREFIX, TEMPLATE_PLACEHOLDER_ID_SUFFIX,
    TEMPLATE_PLACEHOLDER_ARGS_SUFFIX, TEMPLATE_INCLUDE_FILE_PLACEHOLDER_ID,
    clone_template_project, deploy_destination_file_creator, deploy_template, patch_outsourced, patch_string,
    project_templates, register_template, replace_with_file_content_or_default, replace_with_template_args,
    setup_kwargs_literal, template_path_option, template_version_option, TPL_IMPORT_NAME_SUFFIX)


def teardown_module():
    """ pytest test module teardown to clear registered template projects and to check if MockedMainApp gets used. """
    print(f"##### {os_path_basename(__file__)} teardown_module BEG - {CACHED_TPL_PROJECTS=} {get_main_app()=}")

    CACHED_TPL_PROJECTS.clear()         # remove registered template projects from ae.templates module
    temp_context_cleanup()
    temp_context_cleanup(GIT_CLONE_CACHE_CONTEXT)

    print(f"##### {os_path_basename(__file__)} teardown_module END - {CACHED_TPL_PROJECTS=} {get_main_app()=}")


@pytest.fixture
def clean_temp_dirs():
    assert not temp_context_folders(GIT_CLONE_CACHE_CONTEXT)
    yield
    temp_context_cleanup(GIT_CLONE_CACHE_CONTEXT)


def test_declaration_of_template_vars():
    assert isinstance(OUTSOURCED_FILE_NAME_PREFIX, str)
    assert isinstance(OUTSOURCED_MARKER, str)
    assert isinstance(TPL_FILE_NAME_PREFIX, str)
    assert isinstance(TEMPLATE_PLACEHOLDER_ID_PREFIX, str)
    assert isinstance(TEMPLATE_PLACEHOLDER_ID_SUFFIX, str)
    assert isinstance(TEMPLATE_PLACEHOLDER_ARGS_SUFFIX, str)
    assert isinstance(TEMPLATE_INCLUDE_FILE_PLACEHOLDER_ID, str)


class TestHelpers:
    def test_clone_template_project(self, clean_temp_dirs):
        tpl_path = clone_template_project('aedev.project_tpls', GIT_VERSION_TAG_PREFIX + '0.3.36')
        assert tpl_path
        assert os_path_isdir(tpl_path)
        assert os_path_basename(tpl_path) == TEMPLATES_FOLDER

    def test_clone_template_project_for_apps(self, clean_temp_dirs):
        tpl_path = clone_template_project('aedev.app_tpls', GIT_VERSION_TAG_PREFIX + '0.3.16')
        assert tpl_path
        assert os_path_isdir(tpl_path)
        assert os_path_basename(tpl_path) == TEMPLATES_FOLDER

    def test_deploy_destination_file_creator_bytes_content(self, tmp_path):
        file_path = os_path_join(str(tmp_path),  'tst file name.bin')

        deploy_destination_file_creator(file_path, b"bytes content", extra_mode='b')

        assert os_path_isfile(file_path)
        assert read_file(file_path, extra_mode='b') == b"bytes content"

    def test_deploy_destination_file_creator_string_content(self, tmp_path):
        file_path = os_path_join(str(tmp_path), 'subdir1', 'subdir2', 'sub dir 3', 'tst file name')

        deploy_destination_file_creator(file_path, "string content", "")

        assert os_path_isfile(file_path)
        assert read_file(file_path) == "string content"

    def test_deploy_template_dst_files_not_passed(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        src_dir = os_path_join(parent_dir, 'tpl_src_prj_dir')
        tpl_dir = os_path_join(src_dir, TEMPLATES_FOLDER)
        file_name = 'template.extension'
        src_file = os_path_join(tpl_dir, file_name)
        content = "template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)

        deploy_template(src_file, "", "", new_pdv)

        dst_file = os_path_join(dst_dir, file_name)
        assert os_path_isfile(dst_file)
        assert read_file(dst_file) == content

    def test_deploy_template_logged_state(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        src_dir = os_path_join(parent_dir, 'tpl_src_prj_dir')
        tpl_dir = os_path_join(src_dir, TEMPLATES_FOLDER)
        content = "logged template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        log_prefix = "    - "
        os.makedirs(tpl_dir)
        os.makedirs(dst_dir)
        logged = []

        file_name = "template_state_log.ext"
        src_file = os_path_join(tpl_dir, file_name)
        write_file(src_file, content)

        deploy_template(src_file, "", "", new_pdv, logger=lambda *_: logged.extend(arg for arg in _))
        assert logged[-1].startswith(log_prefix + "refresh")

        deploy_template(src_file, "", "", new_pdv, logger=lambda *_: logged.extend(arg for arg in _))
        assert logged[-1].startswith(log_prefix + "binary-exists-skip")

        lock_file = os_path_join(dst_dir, file_name + LOCK_EXT)
        write_file(lock_file, "")
        deploy_template(src_file, "", "", new_pdv, logger=lambda *_: logged.extend(arg for arg in _))
        assert logged[-1].startswith(log_prefix + "lock-extension-skip")
        os.remove(lock_file)

        src_file = os_path_join(tpl_dir, TPL_FILE_NAME_PREFIX + "template_state_log.ext")
        write_file(src_file, content)

        deploy_template(src_file, "", "", new_pdv, logger=lambda *_: logged.extend(arg for arg in _))
        assert logged[-1].startswith(log_prefix + "unchanged-skip")

        src_file = os_path_join(tpl_dir, TPL_FILE_NAME_PREFIX + "template_state_log.ext")
        write_file(src_file, content + " extended")

        deploy_template(src_file, "", "", new_pdv, logger=lambda *_: logged.extend(arg for arg in _))
        assert logged[-1].startswith(log_prefix + "missing-outsourced-marker-skip")

    def test_deploy_template_otf_in_sub_dir(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'prj_with_otf_tpl')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        sub_dir_folder = 'sub_dir'
        tpl_sub_dir = os_path_join(tpl_dir, sub_dir_folder)
        file_name = OUTSOURCED_FILE_NAME_PREFIX + 'changed_template' + PY_EXT
        src_file = os_path_join(tpl_sub_dir, file_name)
        content = "# template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        patcher = "patching package id to be added to patched destination file"
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)

        deploy_template(src_file, sub_dir_folder, patcher, new_pdv, dst_files=dst_files)

        dst_file = os_path_join(dst_dir, sub_dir_folder, file_name[len(OUTSOURCED_FILE_NAME_PREFIX):])
        assert os_path_isfile(dst_file)
        assert OUTSOURCED_MARKER in read_file(dst_file)
        assert patcher in read_file(dst_file)
        assert read_file(dst_file).endswith(content)
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_otf_tpl_in_sub_dir(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'prj_root_dir')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        sub_dir_folder = 'sub_dir'
        tpl_sub_dir = os_path_join(tpl_dir, sub_dir_folder)
        file_name = OUTSOURCED_FILE_NAME_PREFIX + TPL_FILE_NAME_PREFIX + 'changed_template' + PY_EXT
        src_file = os_path_join(tpl_sub_dir, file_name)
        content = "# template file content created in {project_path}"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        patcher = "patching project name to be added to destination file"
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)

        deploy_template(src_file, sub_dir_folder, patcher, new_pdv, dst_files=dst_files)

        dst_file = os_path_join(dst_dir, sub_dir_folder,
                                file_name[len(OUTSOURCED_FILE_NAME_PREFIX) + len(TPL_FILE_NAME_PREFIX):])
        assert os_path_isfile(dst_file)
        assert OUTSOURCED_MARKER in read_file(dst_file)
        assert patcher in read_file(dst_file)
        assert read_file(dst_file).endswith(content.format(project_path=dst_dir))
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_otf_stop_tpl(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'prj_root_dir')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        sub_dir_folder = TEMPLATES_FOLDER
        tpl_sub_dir = os_path_join(tpl_dir, sub_dir_folder)
        file_name = OUTSOURCED_FILE_NAME_PREFIX + TPL_STOP_CNV_PREFIX + TPL_FILE_NAME_PREFIX + 'chg_template' + PY_EXT
        src_file = os_path_join(tpl_sub_dir, file_name)
        content = "# template file content created in {project_path}"
        dst_dir = os_path_join(parent_dir, 'dst', TEMPLATES_FOLDER)
        new_pdv = {'project_path': dst_dir}
        patcher = "patcher"
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)

        deploy_template(src_file, sub_dir_folder, patcher, new_pdv, dst_files=dst_files)

        dst_file = os_path_join(dst_dir, sub_dir_folder,
                                file_name[len(OUTSOURCED_FILE_NAME_PREFIX) + len(TPL_STOP_CNV_PREFIX):])
        assert os_path_isfile(dst_file)
        assert OUTSOURCED_MARKER in read_file(dst_file)
        assert patcher in read_file(dst_file)
        assert read_file(dst_file).endswith(content)
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_otf_existing_unlocked_because_marker(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'project_dir')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        file_name = OUTSOURCED_FILE_NAME_PREFIX + 'unlocked_template' + PY_EXT
        src_file = os_path_join(tpl_dir, file_name)
        content = f"# template file extra content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        patcher = "patching package id to be added to destination file"
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        dst_file = os_path_join(dst_dir, file_name[len(OUTSOURCED_FILE_NAME_PREFIX):])
        write_file(dst_file, OUTSOURCED_MARKER, make_dirs=True)

        deploy_template(src_file, "", patcher, new_pdv, dst_files=dst_files)

        assert os_path_isfile(dst_file)
        assert OUTSOURCED_MARKER in read_file(dst_file)
        assert content in read_file(dst_file)
        assert patcher in read_file(dst_file)
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_otf_existing_locked_without_marker(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'prj_root')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        file_name = OUTSOURCED_FILE_NAME_PREFIX + 'locked_template' + PY_EXT
        src_file = os_path_join(tpl_dir, file_name)
        content = "# template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        patcher = "patcher id or package name"
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        dst_file = os_path_join(dst_dir, file_name[len(OUTSOURCED_FILE_NAME_PREFIX):])
        dst_content = "locked because not contains marker"
        write_file(dst_file, dst_content, make_dirs=True)

        deploy_template(src_file, "", patcher, new_pdv, dst_files=dst_files)

        assert os_path_isfile(dst_file)
        assert OUTSOURCED_MARKER not in read_file(dst_file)
        assert read_file(dst_file) == dst_content
        assert patcher not in read_file(dst_file)
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_otf_locked_by_file(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'prj_dir')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        file_name = OUTSOURCED_FILE_NAME_PREFIX + 'locked_template' + PY_EXT
        src_file = os_path_join(tpl_dir, file_name)
        content = "# template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        dst_file = os_path_join(dst_dir, file_name[len(OUTSOURCED_FILE_NAME_PREFIX):])
        write_file(dst_file + '.locked', "", make_dirs=True)

        deploy_template(src_file, "", "", new_pdv, dst_files=dst_files)

        assert not os_path_isfile(dst_file)
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_sfp_prefix_remove_and_spt_in_sub_dir(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        src_dir = os_path_join(parent_dir, 'tpl_src_prj_dir')
        tpl_dir = os_path_join(src_dir, TEMPLATES_FOLDER)
        sub_dir_folder = 'sub_dir'
        tpl_sub_dir = os_path_join(tpl_dir, sub_dir_folder)
        prefixes = SKIP_IF_PORTION_DST_NAME_PREFIX + SKIP_PRJ_TYPE_FILE_NAME_PREFIX
        file_name = prefixes + ROOT_PRJ + "_template_file_name.xyz"
        src_file = os_path_join(tpl_sub_dir, file_name)
        content = "template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir, 'project_type': ROOT_PRJ}
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)

        assert not deploy_template(src_file, sub_dir_folder, "", new_pdv, dst_files=dst_files)

        assert not dst_files        # skipped deploy

        new_pdv['project_type'] = MODULE_PRJ

        assert deploy_template(src_file, sub_dir_folder, "", new_pdv, dst_files=dst_files)

        assert dst_files            # not skipped deploy
        dst_file = os_path_join(dst_dir, sub_dir_folder, file_name[len(prefixes) + len(ROOT_PRJ) + 1:])
        assert os_path_isfile(dst_file)
        assert read_file(dst_file) == content
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_tpl_in_sub_dir(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'tpl_src_root_dir')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        sub_dir_folder = 'sub_dir'
        tpl_sub_dir = os_path_join(tpl_dir, sub_dir_folder)
        file_name = TPL_FILE_NAME_PREFIX + 'changed_template' + PY_EXT
        src_file = os_path_join(tpl_sub_dir, file_name)
        content = "# template file content created in {project_path}"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        patcher = "patching package id here not added to patched destination file"
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)

        deploy_template(src_file, sub_dir_folder, patcher, new_pdv, dst_files=dst_files)

        dst_file = os_path_join(dst_dir, sub_dir_folder, file_name[len(TPL_FILE_NAME_PREFIX):])
        assert os_path_isfile(dst_file)
        assert OUTSOURCED_MARKER not in read_file(dst_file)
        assert patcher not in read_file(dst_file)
        assert read_file(dst_file).endswith(content.format(project_path=dst_dir))
        assert norm_path(dst_file) in dst_files

    def test_deploy_template_tpl_locked_by_priority(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        prj_dir = os_path_join(parent_dir, 'prj')
        tpl_dir = os_path_join(prj_dir, TEMPLATES_FOLDER)
        file_name = TPL_FILE_NAME_PREFIX + 'template' + PY_EXT
        src_file = os_path_join(tpl_dir, file_name)
        content = "# template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)
        dst_file = os_path_join(dst_dir, file_name[len(TPL_FILE_NAME_PREFIX):])

        deploy_template(src_file, "", "", new_pdv, dst_files=dst_files)

        assert os_path_isfile(dst_file)
        assert read_file(dst_file) == content
        assert norm_path(dst_file) in dst_files

        dst_files_len = len(dst_files)
        write_file(src_file, 'any OTHER content')

        # second deploy try from tpl prj with lower priority
        deploy_template(src_file, "", "", new_pdv, dst_files=dst_files)

        assert os_path_isfile(dst_file)
        assert read_file(dst_file) == content
        assert dst_files_len == len(dst_files)

    def test_deploy_template_unchanged_in_sub_dir(self, tmp_path):
        parent_dir = os_path_join(str(tmp_path), DEF_PROJECT_PARENT_FOLDER)
        src_dir = os_path_join(parent_dir, 'tpl_src_prj_dir')
        tpl_dir = os_path_join(src_dir, TEMPLATES_FOLDER)
        sub_dir_folder = 'sub_dir'
        tpl_sub_dir = os_path_join(tpl_dir, sub_dir_folder)
        file_name = 'unchanged_template.ext'
        src_file = os_path_join(tpl_sub_dir, file_name)
        content = "template file content"
        dst_dir = os_path_join(parent_dir, 'dst')
        new_pdv = {'project_path': dst_dir}
        dst_files = set()
        write_file(src_file, content, make_dirs=True)
        os.makedirs(dst_dir)

        deploy_template(src_file, sub_dir_folder, "", new_pdv, dst_files=dst_files)

        dst_file = os_path_join(dst_dir, sub_dir_folder, file_name)
        assert os_path_isfile(dst_file)
        assert read_file(dst_file) == content
        assert norm_path(dst_file) in dst_files

    def test_patch_outsourced_md(self):
        content = "content"
        patcher = "patcher"
        patched_content = patch_outsourced("any.md", content, patcher)
        assert patched_content.endswith(content)
        assert patched_content.startswith(f"<!-- {OUTSOURCED_MARKER}")
        assert patcher in patched_content

    def test_patch_outsourced_rst(self):
        content = "content"
        patcher = "patcher"
        sep = os.linesep
        patched_content = patch_outsourced("any.rst", content, patcher)
        assert patched_content.endswith(content)
        assert patched_content.startswith(f"{sep}..{sep}    {OUTSOURCED_MARKER}")
        assert patcher in patched_content

    def test_patch_outsourced_txt(self):
        content = "content"
        patcher = "patcher"
        patched_content = patch_outsourced("any.txt", content, patcher)
        assert patched_content.endswith(content)
        assert patched_content.startswith(f"# {OUTSOURCED_MARKER}")
        assert patcher in patched_content

    def test_patch_string_empty_args(self):
        assert patch_string("", {}, invalid_place_holder_id=lambda s: "") == ""

    def test_patch_string_replace_without_empty_lines(self):
        if sys.version_info < (3, 12):
            return  # backslash in f-strings is not supported before Python 3.12

        # code editor does allow comments with backslash at the end \
        tpl_content = textwrap.dedent('''\
        # ReplaceWith#({'1st line  
        # with comment\\n' if tpl_var else ''})## ReplaceWith#({'2nd line\\n' if tpl_var else ''})#''')

        patched = patch_string(tpl_content, {'tpl_var': True})

        assert patched == "1st line  # with comment\n2nd line\n"
        assert patched == textwrap.dedent('''\
        1st line  # with comment
        2nd line
        ''')

        patched = patch_string(tpl_content, {'tpl_var': False})

        assert patched == ""

    def test_patch_string_setup_template(self):
        setup_tpl = textwrap.dedent('''\
        """ setup of {project_desc}. """
        # ReplaceWith#({'import sys' if bool_var else ''})#
        # ReplaceWith#({'print(f"SetUp {__name__=} {sys.executable=} {sys.argv=} {sys.path=}")' if bool_var else ''})#
        # ReplaceWith#(setup_kwargs = {setup_kwargs_literal(setup_kwargs)})#
        # ReplaceWith#(setuptools.setup(**setup_kwargs))#
        ''')

        glo_vars = {'project_desc': 'ProjectDesc',
                    'bool_var': False,
                    'setup_kwargs_literal': setup_kwargs_literal,
                    'setup_kwargs': {'key1': "SetupKwargs_Key1_Value",
                                     'key2': ["list", "of", "test", "strings"],
                                     }
                    }

        patched = patch_string(setup_tpl, glo_vars)

        assert patched == textwrap.dedent('''\
        """ setup of ProjectDesc. """


        setup_kwargs = {
            'key1': 'SetupKwargs_Key1_Value',
            'key2': ['list', 'of', 'test', 'strings'],
        }
        setuptools.setup(**setup_kwargs)
        ''')

        glo_vars['bool_var'] = True

        patched = patch_string(setup_tpl, glo_vars)

        assert patched == textwrap.dedent('''\
        """ setup of ProjectDesc. """
        import sys
        print(f"SetUp {__name__=} {sys.executable=} {sys.argv=} {sys.path=}")
        setup_kwargs = {
            'key1': 'SetupKwargs_Key1_Value',
            'key2': ['list', 'of', 'test', 'strings'],
        }
        setuptools.setup(**setup_kwargs)
        ''')

    def test_patch_string_with_globals(self):
        content = (
            "\nif {os.environ}:"                                    # patch_string is adding 'os' module to globals
            "\n    var_name = {tst_dict}"
        )
        key1 = 'key'
        val1 = "test dict key value"
        key2 = 'sub-dict'
        val2_key1 = 'sub_dict_key1'
        val2_key11 = 'sub_dict_key1'
        val2_val111 = "list item 1"
        val2_val112 = "list item 2"
        val2_key2 = 'str_val'
        val2_val2 = "string val"
        val2 = {val2_key1: {val2_key11: [val2_val111, val2_val112], val2_key2: val2_val2}}
        key3 = 'z quite long test dict key name, with z as first char to show on last line'
        val3 = "test dict value of long key name"

        patched = patch_string(content, {'tst_dict': {key1: val1, key2: val2, key3: val3}})

        assert key1 in patched
        assert val1 in patched
        assert key2 in patched
        assert val2_key1 in patched
        assert val2_key11 in patched
        assert val2_val111 in patched
        assert val2_val112 in patched
        assert val2_key2 in patched
        assert val2_val2 in patched
        assert key2 in patched
        assert val3 in patched

        assert 'os.environ' not in patched
        assert 'pprint.' not in patched
        assert 'sys.' not in patched

    def test_project_templates_new_dev_req(self, clean_temp_dirs):
        assert not CACHED_TPL_PROJECTS      # first reference to this cache in this test module - should be empty
        root_prj_imp_name = 'ae.ae'
        reg_tpls = CACHED_TPL_PROJECTS.copy()
        dev_reqs = []

        prj_tpls = project_templates(MODULE_PRJ, 'ae', {}, reg_tpls, dev_reqs)

        assert root_prj_imp_name + PROJECT_VERSION_SEP + prj_tpls[0]['version'] in reg_tpls
        assert 'aedev.module_tpls' + PROJECT_VERSION_SEP + "" in reg_tpls
        assert 'aedev.project_tpls' + PROJECT_VERSION_SEP + prj_tpls[1]['version'] in reg_tpls

        assert len(prj_tpls) == 2   # ae namespace root and tpl_project
        assert prj_tpls[0]['import_name'] == root_prj_imp_name
        assert prj_tpls[0]['version'] != ""   # latest PyPI version
        assert prj_tpls[0] == reg_tpls[root_prj_imp_name + PROJECT_VERSION_SEP + prj_tpls[0]['version']]
        assert prj_tpls[1]['import_name'] == 'aedev.project_tpls'
        assert prj_tpls[1]['version'] != ""   # latest PyPI version
        assert prj_tpls[1] == reg_tpls['aedev.project_tpls' + PROJECT_VERSION_SEP + prj_tpls[1]['version']]

        assert len(reg_tpls) == 3
        reg_tpl = reg_tpls[root_prj_imp_name + PROJECT_VERSION_SEP + prj_tpls[0]['version']]
        assert reg_tpl['import_name'] == root_prj_imp_name
        assert reg_tpl['version'] == prj_tpls[0]['version']
        assert reg_tpl['tpl_path'].endswith(TEMPLATES_FOLDER)
        assert reg_tpl['register_message'] != ""
        reg_tpl = reg_tpls['aedev.module_tpls' + PROJECT_VERSION_SEP + ""]
        assert reg_tpl['import_name'] == 'aedev.module_tpls'
        assert reg_tpl['version'] == ""
        assert reg_tpl['tpl_path'] == ""
        assert reg_tpl['register_message'] != ""
        reg_tpl = reg_tpls['aedev.project_tpls' + PROJECT_VERSION_SEP + prj_tpls[1]['version']]
        assert reg_tpl['import_name'] == 'aedev.project_tpls'
        assert reg_tpl['version'] == prj_tpls[1]['version']
        assert reg_tpl['tpl_path'].endswith(TEMPLATES_FOLDER)
        assert reg_tpl['register_message'] != ""

        assert len(dev_reqs) == 2
        assert norm_name(root_prj_imp_name) + PROJECT_VERSION_SEP + prj_tpls[0]['version'] in dev_reqs
        assert norm_name('aedev.project_tpls') + PROJECT_VERSION_SEP + prj_tpls[1]['version'] in dev_reqs

        assert not CACHED_TPL_PROJECTS

    def test_project_templates_dev_req_lock(self, clean_temp_dirs):
        dev_reqs = ('any_non_tpl_prj', )
        req_copy = tuple(dev_reqs)
        reg_tpls = CACHED_TPL_PROJECTS.copy()

        prj_tpls = project_templates(MODULE_PRJ, 'ae', {}, reg_tpls, dev_reqs)

        assert len(prj_tpls) == 2
        assert dev_reqs == req_copy
        assert len(reg_tpls) == len(CACHED_TPL_PROJECTS) + 3  # ae namespace root, module_tpls and project_tpls
        assert not CACHED_TPL_PROJECTS

    def test_project_templates_dev_req_extendable(self, clean_temp_dirs):
        dev_reqs = ['any_non_tpl_prj']
        req_copy = dev_reqs.copy()
        reg_tpls = CACHED_TPL_PROJECTS.copy()
        assert not reg_tpls and not CACHED_TPL_PROJECTS

        prj_tpls = project_templates(MODULE_PRJ, 'aedev', {}, reg_tpls, dev_reqs)

        assert len(prj_tpls) == 2
        assert len(dev_reqs) == len(req_copy) + 2                   # added aedev and project_tpls
        assert len(reg_tpls) == len(CACHED_TPL_PROJECTS) + 3    # .. and module_tpls without version
        assert not CACHED_TPL_PROJECTS

        try:
            # cleanup because git_clone would fail because of non-empty temp destination dir/folder
            temp_context_cleanup(GIT_CLONE_CACHE_CONTEXT)
            prj_tpls = project_templates(MODULE_PRJ, 'aedev', {}, CACHED_TPL_PROJECTS, dev_reqs)

            assert len(prj_tpls) == 2
            assert len(reg_tpls) == len(CACHED_TPL_PROJECTS)
            assert reg_tpls != CACHED_TPL_PROJECTS  # only temp dir paths are new/changed
            assert len(dev_reqs) == len(req_copy) + 2
        finally:
            CACHED_TPL_PROJECTS.clear()

    def test_register_template_aedev_root(self, clean_temp_dirs):
        nsn = "aedev"
        tpl_imp_name = nsn + "." + nsn
        pkg_name = norm_name(tpl_imp_name)
        tpl_path = os_path_join(pkg_name, nsn, nsn, TEMPLATES_FOLDER)
        dev_requires = []
        prj_tpls = []
        reg_tpls = CACHED_TPL_PROJECTS.copy()

        register_template(tpl_imp_name, {}, reg_tpls, dev_requires, prj_tpls)

        assert dev_requires
        assert dev_requires[0].startswith(pkg_name + PROJECT_VERSION_SEP)
        assert dev_requires[0].split(PROJECT_VERSION_SEP)[1]

        assert prj_tpls
        assert prj_tpls[0]['import_name'] == tpl_imp_name
        assert prj_tpls[0]['tpl_path'] != ""  # temporary dir path
        assert prj_tpls[0]['tpl_path'].endswith(tpl_path)
        assert prj_tpls[0]['version'] != ""   # latest PyPI version
        assert prj_tpls[0]['register_message'] != ""

        pkg_name, version = project_name_version(tpl_imp_name, list(reg_tpls.keys()))
        assert tpl_imp_name + PROJECT_VERSION_SEP + version in reg_tpls
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['import_name'] == tpl_imp_name
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['tpl_path'] != ""
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['tpl_path'].endswith(tpl_path)
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['version'] == version
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['register_message'] != ""
        assert version in reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['register_message']

        assert not CACHED_TPL_PROJECTS

    @skip_gitlab_ci
    def test_register_template_aedev_root_local(self, clean_temp_dirs):
        nsn = "aedev"
        tpl_imp_name = nsn + "." + nsn
        pkg_name = norm_name(tpl_imp_name)
        pkg_path = "../" + pkg_name
        tpl_subdir = os_path_join(nsn, nsn, TEMPLATES_FOLDER)
        pkg_tpl_path = norm_path(os_path_join(pkg_path, tpl_subdir))
        dev_requires = []
        prj_tpls = []
        reg_tpls = CACHED_TPL_PROJECTS.copy()
        req_options = {template_path_option(tpl_imp_name): pkg_path}

        register_template(tpl_imp_name, req_options, reg_tpls, dev_requires, prj_tpls)

        assert not dev_requires     # local templates get never added to dev_requirements

        assert prj_tpls
        assert prj_tpls[0]['import_name'] == tpl_imp_name
        assert prj_tpls[0]['tpl_path'] == pkg_tpl_path
        assert prj_tpls[0]['tpl_path'].endswith(tpl_subdir)
        assert prj_tpls[0]['version'] == 'local'
        assert prj_tpls[0]['register_message'] != ""

        pkg_name, version = project_name_version(tpl_imp_name, list(reg_tpls.keys()))
        assert tpl_imp_name + PROJECT_VERSION_SEP + version in reg_tpls
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['import_name'] == tpl_imp_name
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['tpl_path'].endswith(tpl_subdir)
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['tpl_path'] == pkg_tpl_path
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['version'] == version
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['register_message'] != ""
        assert version in reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['register_message']

    def test_register_template_aedev_root_version(self, clean_temp_dirs):
        nsn = "aedev"
        version = "0.3.24"
        tpl_imp_name = nsn + "." + nsn
        pkg_name = norm_name(tpl_imp_name)
        tpl_path = os_path_join(pkg_name, nsn, nsn, TEMPLATES_FOLDER)
        dev_requires = []
        prj_tpls = []
        reg_tpls = CACHED_TPL_PROJECTS.copy()
        req_options = {template_version_option(tpl_imp_name): version}

        register_template(tpl_imp_name, req_options, reg_tpls, dev_requires, prj_tpls)

        assert dev_requires
        assert dev_requires[0].startswith(pkg_name + PROJECT_VERSION_SEP)
        assert dev_requires[0].split(PROJECT_VERSION_SEP)[1]

        assert prj_tpls
        assert prj_tpls[0]['import_name'] == tpl_imp_name
        assert prj_tpls[0]['tpl_path'] != ""
        assert prj_tpls[0]['tpl_path'].endswith(tpl_path)
        assert prj_tpls[0]['version'] == version
        assert prj_tpls[0]['register_message'] != ""

        pkg_name, version = project_name_version(tpl_imp_name, list(reg_tpls.keys()))
        assert tpl_imp_name + PROJECT_VERSION_SEP + version in reg_tpls
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['import_name'] == tpl_imp_name
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['tpl_path'] != ""
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['tpl_path'].endswith(tpl_path)
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['version'] == version
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['register_message'] != ""
        assert version in reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP + version]['register_message']

    def test_register_template_not_existing(self, clean_temp_dirs):
        tpl_imp_name = "not.existing_package_tpls_imp_name"
        dev_requires = []
        prj_tpls = []
        reg_tpls = CACHED_TPL_PROJECTS.copy()

        register_template(tpl_imp_name, {}, reg_tpls, dev_requires, prj_tpls)

        assert not dev_requires
        assert not prj_tpls
        assert tpl_imp_name + PROJECT_VERSION_SEP in reg_tpls
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP]['import_name'] == tpl_imp_name
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP]['tpl_path'] == ""
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP]['version'] == ""
        assert reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP]['register_message'] != ""
        assert tpl_imp_name in reg_tpls[tpl_imp_name + PROJECT_VERSION_SEP]['register_message']

    def test_replace_with_file_content_or_default(self, tmp_path):
        assert replace_with_file_content_or_default("") == ""

        def_val = "default_value"
        assert replace_with_file_content_or_default(f"_non_file,{def_val}") == def_val
        assert replace_with_file_content_or_default(f"_non_file,{def_val},{def_val}") == def_val + "," + def_val

        assert replace_with_file_content_or_default(f"_non_file,'{def_val[:3]}' + '{def_val[3:]}'") == def_val
        assert replace_with_file_content_or_default(f"_non_file,369") == 369
        with pytest.raises(ValueError):
            assert replace_with_file_content_or_default(f"_non_file,{'a': 111}")
        with pytest.raises(ValueError):
            assert replace_with_file_content_or_default(f"_non_file,{3: '111'}")
        assert replace_with_file_content_or_default(f"_non_file,{111}") == 111
        assert replace_with_file_content_or_default(f"_non_file,[111]") == [111]
        assert replace_with_file_content_or_default(f"_non_file,(1, 2, 3)") == (1, 2, 3)

        syntax_err = "syntax error ' + 1"
        assert replace_with_file_content_or_default("_non_file," + syntax_err) == syntax_err

        file_name = os_path_join(str(tmp_path), "returned_file.txt")
        content = "file_content_to_be_returned"
        assert replace_with_file_content_or_default(f"{file_name},{def_val}") == def_val
        write_file(file_name, content)
        assert replace_with_file_content_or_default(file_name) == content
        assert replace_with_file_content_or_default(f"{file_name},{def_val}") == content

    def test_replace_with_template_args(self):
        any_arg_str = 'any Arg String'
        assert replace_with_template_args(any_arg_str) == any_arg_str

    def test_setup_kwargs_literal(self):
        kwargs = {'key1': "val1", 'key2': {'a': 1, 'b': "3"}}
        lit = setup_kwargs_literal(kwargs)
        assert lit[0] == "{"
        assert lit[1] == "\n"
        assert lit[2:14] == " " * 4 + "'key1': "
        assert lit[14:21] == "'val1',"
        assert lit[21:40] == "\n" + " " * 4 + "'key2': {'a': "
        assert lit[-5:-2] == "'},"
        assert lit[-2:] == "\n}"

    def test_template_path_option(self):
        nsn_name = 'nsn'
        por_name = 'nsn'
        import_name = nsn_name + "." + por_name

        assert template_path_option(import_name) == 'portions_namespace_root' + TPL_PATH_OPTION_SUFFIX

        por_name = "what_ever" + TPL_IMPORT_NAME_SUFFIX
        import_name = nsn_name + "." + por_name

        assert template_path_option(import_name) == norm_name(por_name) + TPL_PATH_OPTION_SUFFIX

    def test_template_version_option(self):
        import_name = 'xy.nsm.prj_name'

        assert template_version_option(import_name) == 'portions_namespace_root' + TPL_VERSION_OPTION_SUFFIX

        import_name += TPL_IMPORT_NAME_SUFFIX
        por_name = import_name.split('.')[-1]

        assert template_version_option(import_name) == norm_name(por_name) + TPL_VERSION_OPTION_SUFFIX


def test_temp_context_is_correctly_cleaned_up():
    assert not temp_context_folders(GIT_CLONE_CACHE_CONTEXT)
