import sys

import pypdf


def PDFExtractPage(PDFFilePath: str, OutputFilePath: str, PageFrom: int, PageTo: int):
    """
    PDFファイルをから、指定したページを抽出する関数
    :param PDFFilePath: 抽出元のPDFファイルのパス
    :param OutputFilePath: 出力するPDFファイルのパス
    """
    merger = pypdf.PdfWriter()

    merger.append(PDFFilePath, pages=(PageFrom - 1, PageTo))

    merger.write(OutputFilePath)
    merger.close()


if __name__ == "__main__":
    print("Extract PDF Page")

    # コマンドライン引数受け取り
    args = sys.argv
    if len(args) < 4:
        raise ValueError("引数が足りません")

    PDFExtractPage(args[1], args[2], int(args[3]), int(args[4]))
