from gooey import Gooey, GooeyParser


@Gooey(program_name="简单的实例")
def main():
    parser = GooeyParser(description="第一个示例!")
    parser.add_argument('文件路径', widget="FileChooser")      # 文件选择框
    parser.add_argument('日期', widget="DateChooser")          # 日期选择框
    args = parser.parse_args()                                 # 接收界面传递的参数
    print(args)


if __name__ == '__main__':
    main()
