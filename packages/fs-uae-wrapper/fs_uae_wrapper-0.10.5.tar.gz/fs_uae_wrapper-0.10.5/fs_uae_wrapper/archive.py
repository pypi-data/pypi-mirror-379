"""
Run fs-uae with archived filesystem/adf files

It will use compressed directories, and optionally replace source archive with
the temporary one.
"""
import os
import shutil

from fs_uae_wrapper import base, utils


class Wrapper(base.ArchiveBase):
    """
    Class for performing extracting archive, copying emulator files, and
    cleaning it back again
    """
    def __init__(self, conf_file, fsuae_options, configuration):
        super(Wrapper, self).__init__(conf_file, fsuae_options, configuration)
        self.archive_type = None

    def run(self):
        """
        Main function which accepts configuration file for FS-UAE
        It will do as follows:
            - extract archive file
            - copy configuration
            - run the emulation
            - optionally make archive save state
        """
        if not super(Wrapper, self).run():
            return False

        if not self._extract():
            return False

        self._load_save()

        if not self._copy_conf():
            return False

        if not self._run_emulator():
            return False

        if self._get_saves_dir():
            if not self._save_save():
                return False

        return self._make_archive()

    def _make_archive(self):
        """
        Produce archive and save it back. Than remove old one.
        """
        if self.all_options.get('wrapper_persist_data', '0') != '1':
            return True

        curdir = os.path.abspath('.')
        os.chdir(self.dir)

        saves = self._get_saves_dir()
        if saves:
            shutil.rmtree(saves)
        os.unlink('Config.fs-uae')

        title = self._get_title()

        arch = os.path.basename(self.arch_filepath)
        if not utils.create_archive(arch, title):
            return False

        shutil.move(arch, self.arch_filepath)
        os.chdir(curdir)
        return True
