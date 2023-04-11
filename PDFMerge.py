import PyPDF2
import sys

# コマンドライン引数受け取り
args = sys.argv

file1 = args[1]
file2 = args[2]
file3 = args[3]

# PDFマージに使用するクラス
marger = PyPDF2.PdfMerger()


marger.append(file1)
marger.append(file2)

marger.write(file3)
marger.close()
