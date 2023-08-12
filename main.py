from gui import choose_file
from converter import Converter
from data import pack_formats

def main():
    file_path = choose_file()
    converter = Converter(file_path)

    old_pack = converter.get_format()

    old_to_new = None
    # while old_to_new is None:
    #     inp = input("Do you want to convert from format '3' to '4' or '4' to '3'? (y / n): ").strip()
    #     if inp == 'y':
    #         old_to_new = True
    #     elif inp == 'n':
    #         old_to_new = False
    #     else:
    #         print('Undefined answer.')

    if old_pack['pack']['pack_format'] < 4:
        old_to_new = True
        print('Detected old version pack_format, converting to new...')
    elif old_pack['pack']['pack_format'] >= 4:
        old_to_new = False
        print('Detected new version pack_format, converting to old...')

    converter.convert(old_to_new=old_to_new)

    new_format = None
    formats_text = '\n'.join(f'{k} == ({v})' for k, v in pack_formats.items())
    print(formats_text)
    while new_format is None:
        inp = int(input(f'Format type: {old_pack["pack"]["pack_format"]} --> '))
        new_format = inp

    converter.change_format(old_pack, new_format)


if __name__ == '__main__':
    main()
