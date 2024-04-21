## SuffixFileFilter 类

### 描述
`SuffixFileFilter` 类提供了基于文件后缀过滤文件列表的方法，允许根据文件扩展名包含或排除文件。

`list_remain_suffix`该方法仅保留指定后缀的文件名。

`list_exclude_suffix`该方法排斥指定后缀的文件名。

### 方法

#### collect_suffixes(*suffixes)
- **描述**：将各种形式的后缀参数统一收集成一个元组。如果只提供一个后缀，它将直接返回字符串而不是元组。
- **参数**：
  - `*suffixes` (str, list, tuple)：可变数量的后缀参数，每个可以是字符串或一组字符串（列表/元组）。
- **返回值**：
  - tuple 或 str：一个包含所有收集的后缀的元组，或者如果只提供一个后缀，就返回一个字符串。
- **异常**：
  - `ValueError`：如果任何后缀不是字符串或任何列表/元组中包含非字符串元素时抛出错误。

#### list_remain_suffix(file_list, suffixes)
- **描述**：过滤文件名列表，仅保留具有指定后缀的文件。确保后缀前有点（例如，'.txt'）,该函数使用装饰器`validate_input`来验证输入的文件列表和后缀格式。
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

#### list_exclude_suffix(file_list, suffixes)
- **描述**:过滤文件名列表，排除具有指定后缀的文件。使用此函数时，确保后缀参数前包含点（如`.txt`）,该函数使用装饰器`validate_input`来验证输入的文件列表和后缀格式。。

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
