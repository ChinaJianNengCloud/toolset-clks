## SuperFileDeal 类 （详细的文件操作API可参考Pathlib模块）

### 描述
`SuperFileDeal` 类提供了基于文件后缀过滤文件列表的方法，允许根据文件扩展名包含或排除文件。

`get_filenames`该方法能够尽可能获得指定目录下的文件名，多个参数控制行为。

`list_remain_suffix`该方法仅保留指定后缀的文件名。

`list_exclude_suffix`该方法排斥指定后缀的文件名。

### 方法
### get_filenames(directory, recursive=True, only_filenames=False, min_size=0, max_size=None)

- **描述**:
  - 获取指定目录下的所有文件名，可选择基于文件大小进行筛选（单位为KB）。此函数可选择性地递归遍历所有子目录，以获取更深层次的文件列表。

- **参数**：
  - **directory** (`str`): 需要遍历的目录的路径。
  - **recursive** (`bool`): 指示是否递归遍历子目录。默认为 `True`，表示递归遍历。
  - **only_filenames** (`bool`): 控制是否只返回文件名，而不包括完整的路径。默认为 `False`，表示返回完整路径。
  - **min_size** (`int`): 文件大小的最小阈值（以KB为单位）。只有大于等于这个大小的文件才会被包含在返回的列表中。默认为 `0`，表示没有最小大小限制。
  - **max_size** (`int` 或 `None`): 文件大小的最大阈值（以KB为单位）。只有小于等于这个大小的文件才会被包含在返回的列表中。如果为 `None`，表示没有最大大小限制。

- **返回值**：
  - 返回一个列表，包含符合条件的文件的完整路径或仅文件名，具体取决于 `only_filenames` 参数的设置。

- **示例**：
  ```python
  # 示例：在指定目录下查找所有大于1KB且小于1MB的文件名
  directory_path = 'path_to_your_directory'
  files = get_filenames(directory_path, recursive=True, only_filenames=True, min_size=1, max_size=1024)
  print(files)

- **补充说明**：
  - 想要手搓文件遍历轮子可参考练习：[590. N 叉树的后序遍历](https://leetcode.cn/problems/n-ary-tree-postorder-traversal/description/)




### collect_suffixes(*suffixes)
- **描述**：
  - 将各种形式的后缀参数统一收集成一个元组。如果只提供一个后缀，它将直接返回字符串而不是元组。
- **参数**：
  - `*suffixes` (str, list, tuple)：可变数量的后缀参数，每个可以是字符串或一组字符串（列表/元组）。
- **返回值**：
  - tuple 或 str：一个包含所有收集的后缀的元组，或者如果只提供一个后缀，就返回一个字符串。
- **异常**：
  - `ValueError`：如果任何后缀不是字符串或任何列表/元组中包含非字符串元素时抛出错误。

### list_remain_suffix(file_list, suffixes)
- **描述**：
  - 过滤文件名列表，仅保留具有指定后缀的文件。确保后缀前有点（例如，'.txt'）,该函数使用装饰器`validate_input`来验证输入的文件列表和后缀格式。
- **参数**：
  - `file_list` (list)：要过滤的文件名列表。
  - `suffixes` (tuple, str)：要保留在文件列表中的后缀。
- **返回值**：
  - list：匹配给定后缀的文件名列表。
- **示例**：
  ```python
  file_list = ['example.txt', 'report.pdf', 'data.csv']
  print(f.list_remain_suffix(file_list, '.txt', '.pdf'))
  # 输出: ['example.txt', 'report.pdf']

### list_exclude_suffix(file_list, suffixes)
- **描述**:
  - 过滤文件名列表，排除具有指定后缀的文件。使用此函数时，确保后缀参数前包含点（如`.txt`）,该函数使用装饰器`validate_input`来验证输入的文件列表和后缀格式。。

- **参数**:
  - `file_list` (list): 要过滤的文件名列表。
  - `suffixes` (tuple, str): 要从文件列表中排除的后缀，可以是单个字符串后缀或一个包含多个字符串后缀的元组。

- **返回值**：
  - (list): 不匹配给定后缀的文件名列表。

- **示例**：
  ```python
  # 示例1: 排除一个后缀
  file_list = ['example.txt', 'report.pdf', 'data.csv']
  excluded_files = f.list_exclude_suffix(file_list, '.txt')
  print(excluded_files)  # 输出: ['report.pdf', 'data.csv']
  
  # 示例2: 排除多个后缀，写法不限
  file_list = ['example.txt', 'notebook.ipynb', 'image.png', 'report.pdf', 'summary.txt', 'my.jpg']
  excluded_files = f.list_exclude_suffix(file_list, ('.txt', '.pdf'),['png'])
  print(excluded_files)  # 输出: ['notebook.ipynb', 'my.jpg']
