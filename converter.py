import json
import os
from distutils.dir_util import copy_tree
from data import blocks_items


class Converter:
    def __init__(self, directory_path, adding: str = '_Converted', final_format=None, initial_format=None):
        self.directory_path = directory_path
        self.new_directory_path = self.directory_path + adding
        copy_tree(self.directory_path, self.new_directory_path)
        os.chdir(self.new_directory_path + '/assets/minecraft/textures/')

    def get_format(self):
        with open(self.directory_path + '/pack.mcmeta', 'r') as f:
            pack = json.load(f)

        return pack

    def change_format(self, initial_pack: dict, final_pack_format: int):
        print('Changing format type...')
        final_pack = initial_pack
        final_pack['pack']['pack_format'] = final_pack_format

        with open(self.new_directory_path + '/pack.mcmeta', 'w') as f:
            json.dump(final_pack, f)

        return final_pack

    def convert(self, old_to_new: bool = True):
        # changing folder names
        print('Changing folder names...')

        if old_to_new:
            folder_names = fn = [['blocks', 'block'], ['items', 'item']]
        else:
            folder_names = fn = [['block', 'blocks'], ['item', 'items']]

        blocks_path = os.getcwd() + f'/{fn[0][1]}'
        items_path = os.getcwd() + f'/{fn[1][1]}'

        try:
            os.replace(f'{fn[0][0]}', f'{fn[0][1]}')
            os.replace(f'{fn[1][0]}', f'{fn[1][1]}')
        except FileNotFoundError:
            pass

        # changing file names in blocks folder
        print(f'Changing file names in {fn[0][1]} folder...')
        for block in blocks_items['blocks']:
            if old_to_new:
                old = block[0]
                new = block[1]
            else:
                old = block[1]
                new = block[0]

            try:
                os.replace(f'{blocks_path}/{old}.png', f'{blocks_path}/{fn[0][1]}/{new}.png')
            except FileNotFoundError:
                pass
        # Changing file names in items folder
        print(f'Changing file names in {fn[1][1]} folder...')
        for item in blocks_items['items']:
            if old_to_new:
                old = item[0]
                new = item[1]
            else:
                old = item[1]
                new = item[0]

            try:
                os.replace(f'{items_path}/{old}.png', f'{items_path}/{new}.png')
            except FileNotFoundError:
                pass

        return os.getcwd()