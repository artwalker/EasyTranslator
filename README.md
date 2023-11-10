<p align="center">
  <img width="180" src="./assets/logo.png" alt="EasyTranslator">
  <h1 align="center">&nbsp;&nbsp;&nbsp;&nbsp;Easy Translator</h1>
  <p align="center">&nbsp;&nbsp;&nbsp;Your Companion for Multilingual Reading</p>
</p>

<div align="center">

[![English badge](https://img.shields.io/badge/English-blue)](./README.md)[![简体中文 badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-red)](./README_ZH-CN.md)[![x badge](https://img.shields.io/badge/Follow-EthanWang-purple?logo=x&labelColor=black)](https://twitter.com/EthanWang999)[![youtube badge](https://img.shields.io/badge/Follow-EthanWang999-green?logo=Youtube&logoColor=red&labelColor=black)](https://www.youtube.com/@EthanWang999)[![bilibili badge](https://img.shields.io/badge/Follow-%E6%96%B9%E7%A8%8B%E6%98%9F-brown?logo=bilibili&logoColor=pink&labelColor=black)](https://space.bilibili.com/29185421)

<a href="https://www.buymeacoffee.com/ethanwang" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 40px !important;width: 145px !important;" ></a>
</div>

---

## :bookmark_tabs: Introduction

A command-line tool crafted with the OpenAI API, supporting translation for various file formats, including .txt, .pdf, .docx, .mobi, and .epub.  
Effortlessly translate your text files, eliminating language barriers with ease.

## :bell: Prerequisites

###### :snake: Code Section

```bash
pip install -r preconditions.txt
```

```bash
git clone https://github.com/artwalker/EasyTranslator.git
```

###### :scroll: Configuration Files

- .env
  - `OPENAI_API_KEY`: Specify the OpenAI API Key, can use multiple keys, format like "sk-xxxxxxx, sk-xxxxxxx"

  - `GPT_MODEL`: Specify the model to be used, for example, "gpt-3.5-turbo"

  - `GPT_TEMPERATURE`: Specify the randomness of the model's responses, it's advisable to set it to 0 for text translation.

  - If using OpenAI API provided by Azure, the following parameters need to be set:

  - `ENGINE_AZURE`: Deployment name on Azure

  - `OPENAI_API_KEY_AZURE`: Specify the key for Azure OpenAI API

  - `OPENAI_API_BASE_AZURE`: API address associated with the deployment name

  - `OPENAI_API_TYPE_AZURE`: Type of the API

  - `OPENAI_API_VERSION_AZURE`: Version of the API

- settings.cfg:
  - `openai-proxy`: Proxy for OpenAI

  - `language`: Language for translation

  - `prompt`: Input prompt for specified model translation

  - `bilingual-output`: Whether to save as bilingual text

  - `langcode`: Language code for generated epub files

  - `startpage`: Starting page for specified pdf file

  - `endpage`: Ending page for specified pdf file

  - `transliteration-list`: Transliteration list file name

  - `transliteration-word-capi-low`: Whether the transliteration list is case-sensitive

## :running: Usage

```bash
python easy_translator.py filename [--show] [--tlist] [--azure] [--test]
```

###### :clap: Explanation

- `filename`: Specify the name of the file to be translated, supports txt, pdf, docx, epub, mobi formats

- `--show`: Display the translation process of the text

- `--tlist`: Use a transliteration list

- `--azure`: Use Azure to call the OpenAI API

- `--test`: Used to test the translation effect, translates three paragraphs of text, typically used for debugging

###### :pushpin: Example

```bash
python easy_translator.py ./book/profile.txt
```

```bash
python easy_translator.py ./book/profile.txt --show
```

```bash
python easy_translator.py ./book/profile.txt --azure
```

```bash
python easy_translator.py ./book/profile.txt --azure --show
```

```bash
python easy_translator.py ./book/profile.txt --show --tlist
```

```bash
python easy_translator.py ./book/profile.txt --show --tlist --azure
```

```bash
python easy_translator.py ./book/profile.txt --show --tlist --azure --test
```

## :gift_heart: Reward

<p align="left">
If you feel that this program has awakened your soul like a cup of hot coffee or solved your problems like a Swiss army knife, you might consider showing your appreciation with a reward;</p>  
<p align="left"> Just like tipping a barista, your contribution will fuel my motivation to improve this program and create new code, making the world a better place;</p>  
<p align="left">Regardless of the amount you choose to reward, I will be delighted, as if receiving a gift;</p>  
<p align="left">Thank you for your generous support!</p>  

<div align="center">

| <img width="215" src="./assets/alipay.jpg"> | <img width="200" src="./assets/wechat_pay.jpg"> |
|:---:|:---:
| Alipay | WeChat  |

</div>

---

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=artwalker/EasyTranslator.git&type=Timeline)](https://star-history.com/#artwalker/EasyTranslator.git&Timeline)

</div>
