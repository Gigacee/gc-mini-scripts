################################################################################
# Excel ファイルに画像を挿入します。
################################################################################

require "win32ole"

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

# 挿入する画像
image = "#{WORKING_DIRECTORY_PATH}/image.png"

# Excel アプリケーションを開始
excel = WIN32OLE.new("Excel.Application")

begin
  # 作業ディレクトリと同階層にあるすべての xlsx ファイルに対して処理を行う
  Dir.glob("#{WORKING_DIRECTORY_PATH}/[^~]*.xlsx").each do |xlsx|
    # xlsx ファイルを開く
    book = excel.Workbooks.Open(xlsx)
    puts "#{xlsx} opened."

    # シートを取得
    sheet = book.sheets[1]

    # 画像を挿入
    shape = sheet.Shapes.AddPicture(
      :Filename => image.gsub!("/", "\\"),
      :LinkToFile => false,
      :SaveWithDocument => true,
      :Left => 0,
      :Top => 0,
      :Width => 0,
      :Height => 0,
    )

    # 画像のサイズを等倍にする
    shape.ScaleHeight(1, true)
    shape.ScaleWidth(1, true)

    # xlsx ファイルを上書き保存
    book.Save

    # xlsx ファイルを閉じる
    book.Close
    puts "#{xlsx} closed."
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
