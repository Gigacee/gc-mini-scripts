################################################################################
# 同階層にあるディレクトリの一覧を CSV へ出力します。
################################################################################

# 作業ディレクトリのパスを取得
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

File.open("#{WORKING_DIRECTORY_PATH}/dir_list.csv", "w") do |csv|
  Dir.glob("#{WORKING_DIRECTORY_PATH}/*/").each do |dir|
    # 末尾の "/" を削除して CSV へ出力
    csv.puts dir.chop
  end
end
