################################################################################
# Excel ファイルを扱うテストです。
################################################################################

require "win32ole"

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# Excel ワークブックやワークシートを PDF ファイルに変換する
def convert_excel_to_pdf(obj)
  # PDF ファイルを生成
  obj.PrintOut(
    :ActivePrinter => "Adobe PDF",
  )
end

# Excel アプリケーションを開始
excel = WIN32OLE.new("Excel.Application")

# centimeter -> inch 変換
puts excel.Application.CentimetersToPoints(1)

begin
  # 作業ディレクトリと同階層にあるすべての xlsx ファイルに対して処理を行う
  Dir.glob("#{WORKING_DIRECTORY_PATH}/[^~]*.xlsx").each do |xlsx|
    # xlsx ファイルを開く
    book = excel.Workbooks.Open(xlsx)
    puts "#{xlsx} was opened."

    # シートを取得
    sheet = book.sheets[1]
    # sheet = book.sheets["Sheet1"]

    # 上の余白
    puts sheet.PageSetup.TopMargin

    # 印刷範囲
    puts sheet.PageSetup.PrintArea

    # 特定のセルの値
    puts sheet.Cells(1, 1).Value

    # セル全体の各行に対して処理を行う
    sheet.UsedRange.Rows.each do |row|
      # 行の幅
      # puts row.RowHeight

      # すべてのセルに対して処理を行う
      row.Columns.each do |cell|
        # セルの数式
        puts "#{cell.Address} ... #{cell.Formula}"
      end
    end

    # convert_excel_to_pdf(sheet)

    # xlsx ファイルを上書き保存
    # book.Save

    # xlsx ファイルを閉じる
    book.Close
    puts "#{xlsx} was closed."
  end
rescue
  puts "Exception:"
  puts $!
  puts "Backtrace:"
  puts $@
ensure
  # Excel アプリケーションを終了
  excel.Quit
end
