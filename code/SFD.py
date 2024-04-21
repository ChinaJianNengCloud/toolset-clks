import os
import warnings


def validate_input(func):
    def wrapper(self, file_list, *suffixes):
        if not isinstance(file_list, list):
            raise TypeError("file_list must be a list of filenames.")
        collected_suffixes = SuperFileDeal.collect_suffixes(*suffixes)
        if not collected_suffixes:
            raise ValueError("At least one suffix must be provided.")
        return func(self, file_list, collected_suffixes)

    return wrapper


class SuperFileDeal:

    def get_filenames(self, directory, recursive=True, only_filenames=False, min_size=0, max_size=None):
        """
        获取指定目录下的所有文件名，可选择基于文件大小进行筛选（单位为KB）。可选地遍历所有子目录。

        :param directory: 要遍历的目录的路径
        :param recursive: 布尔值，指示是否递归遍历子目录
        :param only_filenames: 布尔值，控制是否要输出完整目录，还是仅仅文件名
        :param min_size: 整数，文件大小的最小值（以KB为单位），只有大于等于这个大小的文件会被包含在返回的列表中
        :param max_size: 整数或 None，文件大小的最大值（以KB为单位），只有小于等于这个大小的文件会被包含在返回的列表中
        :return: 一个列表，根据 only_filenames 参数，包含文件的完整路径或仅文件名
        """
        file_list = []
        min_size_bytes = min_size * 1024  # 将KB转换为字节
        max_size_bytes = max_size * 1024 if max_size is not None else None  # 将KB转换为字节

        if recursive:
            for root, _, files in os.walk(directory):
                for file in files:
                    full_path = os.path.join(root, file)
                    file_size = os.path.getsize(full_path)
                    if file_size >= min_size_bytes and (max_size_bytes is None or file_size <= max_size_bytes):
                        if only_filenames:
                            file_list.append(file)
                        else:
                            file_list.append(full_path)
        else:
            for file in os.listdir(directory):
                full_path = os.path.join(directory, file)
                if os.path.isfile(full_path):
                    file_size = os.path.getsize(full_path)
                    if file_size >= min_size_bytes and (max_size_bytes is None or file_size <= max_size_bytes):
                        if only_filenames:
                            file_list.append(os.path.basename(file))
                        else:
                            file_list.append(full_path)

        # 检查文件列表是否为空
        if not file_list:
            warnings.warn("目标文件夹是空的，对吗？对吗？对吗？", UserWarning)

        return file_list

    @staticmethod
    def collect_suffixes(*suffixes):
        """将多种形式的后缀参数统一收集成一个元组,如果只有一个就直接返回字符串了"""
        collected_suffixes = []
        for item in suffixes:
            if isinstance(item, (list, tuple)):
                if not all(isinstance(suffix, str) for suffix in item):
                    raise ValueError("All items in list/tuple must be strings.")
                collected_suffixes.extend(item)
            elif isinstance(item, str):
                collected_suffixes.append(item)
            else:
                raise ValueError("All suffixes must be strings, or lists/tuples of strings.")

        # 如果只收集到一个后缀，直接返回该后缀而不是元组
        if len(collected_suffixes) == 1:
            return collected_suffixes[0]
        return tuple(collected_suffixes)

    @validate_input
    def list_remain_suffix(self, file_list, suffixes):
        """仅保留具有指定后缀的文件名，记得要加点！"""
        return [filename for filename in file_list if filename.endswith(suffixes)]

    @validate_input
    def list_exclude_suffix(self, file_list, suffixes):
        """排除具有指定后缀的文件名，记得要加点！"""
        return [filename for filename in file_list if not filename.endswith(suffixes)]


if __name__ == '__main__':
    # 使用示例
    f = SuperFileDeal()
    file = ['example.txt', 'notebook.ipynb', 'image.png', 'report.pdf', 'summary.txt', 'my.jpg']
    print(f.list_remain_suffix(file, '.txt', '.pdf', ('.png', '.ipynb')))
    print(f.list_exclude_suffix(file, '.txt', '.pdf', ['.txt']))
    print(f.collect_suffixes('tex'))
    print(f.get_filenames(r"D:\科研\浙大课题\20240119reduce background\tumor", recursive=True, only_filenames=True, min_size=1, max_size=3*1024)
)
