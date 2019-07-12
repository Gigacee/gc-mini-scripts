# encoding: utf-8
################################################################################
# この階層以下に存在するファイルの名前が NFC で Unicode 正規化されているか調べます。
################################################################################

require "fileutils"

# 作業ディレクトリのパスを取得
WORKING_DIRECTORY_PATH = __dir__.encode("UTF-8").freeze

exists_unnormalized_file = false

Dir.glob("#{WORKING_DIRECTORY_PATH}/**/*").each do |path|
  if !path.unicode_normalized?
    exists_unnormalized_file = true
    puts "「" + path + "」は NFC で Unicode 正規化されていません。"
    # FileUtils.mv(path, path.unicode_normalize)
  end
end

if !exists_unnormalized_file
  puts "すべてのファイルが NFC で Unicode 正規化されています。"
end
