import sys

import pypdf


def PDFMerge(MergeFilePathList: list, OutputFilePath: str):
    """
    PDFファイルをマージする関数
    :param MergeFilePathList: マージするPDFファイルのパスのリスト
    :param OutputFilePath: 出力するPDFファイルのパス
    """

    merger = pypdf.PdfWriter()

    for pdfFile in MergeFilePathList:
        merger.append(pdfFile)

    merger.write(OutputFilePath)
    merger.close()


if __name__ == "__main__":
    print("PDFMerge.py")

    # コマンドライン引数受け取り
    args = sys.argv
    if len(args) < 4:
        raise ValueError("引数が足りません")
    PDFMerge(args[1:-1], args[-1])
