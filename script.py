#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import ntfsutils.junction
import getpass
import os

def get_my_document_path():
    username = getpass.getuser()
    path_tpl = 'C:\\Users\\{}\\Documents\\'.format(username)
    return path_tpl

MY_DOCUMENT_PATH = get_my_document_path()
SRC_BASE_PATH = os.path.dirname(__file__)


class SaveFilePathInfo(object):
    def __init__(self, src, dst):
        self.src = os.path.join(SRC_BASE_PATH, src)
        self.dst = dst

    def create(self):
        self._create_hard_link(self.src, self.dst)

    def _create_hard_link(self, src, dst):
        return ntfsutils.junction.create(src, dst)


sample_game_name = 'Ricotta_ワルキューレロマンツェ'
sample_path = SaveFilePathInfo(sample_game_name, os.path.join(MY_DOCUMENT_PATH, sample_game_name))

def main():
    sample_path.create()

if __name__ == '__main__':
    main()
