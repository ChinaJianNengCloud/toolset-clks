def validate_input(func):
    def wrapper(self, file_list, *suffixes):
        if not isinstance(file_list, list):
            raise TypeError("file_list must be a list of filenames.")
        collected_suffixes = SuffixFileFilter.collect_suffixes(*suffixes)
        if not collected_suffixes:
            raise ValueError("At least one suffix must be provided.")
        return func(self, file_list, collected_suffixes)

    return wrapper


class SuffixFileFilter:
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
    f = SuffixFileFilter()
    file = ['example.txt', 'notebook.ipynb', 'image.png', 'report.pdf', 'summary.txt', 'my.jpg']
    print(f.list_remain_suffix(file, '.txt', '.pdf', ('.png', '.ipynb')))
    print(f.list_exclude_suffix(file, '.txt', '.pdf', ['.txt']))
    print(f.collect_suffixes('tex'))
