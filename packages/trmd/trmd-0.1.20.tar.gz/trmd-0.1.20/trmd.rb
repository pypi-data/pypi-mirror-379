class Trmd < Formula
  include Language::Python::Virtualenv

  desc "Translate Markdown using OpenAI"
  homepage "https://github.com/rioriost/homebrew-trmd/"
  url "https://files.pythonhosted.org/packages/59/00/ab38f5cfe12cded2123af2f49fe69f2404ea1a2296e0b1fa4976a0535d8d/trmd-0.1.19.tar.gz"
  sha256 "f2cef61b01f6d97f89a2853c5b7a6a6948e557bc0ade40c86dd10c5381e7e37a"
  license "MIT"

  depends_on "python@3.13"

  def install
    virtualenv_install_with_resources
    system libexec/"bin/python", "-m", "pip", "install", "openai"
  end

  test do
    system "#{bin}/trmd", "--help"
  end
end
