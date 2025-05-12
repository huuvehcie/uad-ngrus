# Universal Android Debloater Next Generation (ресурсы на русском языке)

> [!warning]
> **ПРЕДУПРЕЖДЕНИЕ**: Используйте на свой страх и риск. Мы не несем ответственности за возможные проблемы с вашими устройствами.

<img src="/uad-ng.png" width="850" alt="uad_screenshot">

**Ознакомьтесь с проблемами, и [присоединяйтесь к разработке!](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/wiki/How-to-contribute )**. Нам **очень нужны** [разработчики Rust](https://www.rust-lang.org ) для исправления критических ошибок, подробнее в [этом объявлении](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/discussions/731 ).

**Для оперативного общения присоединяйтесь к нашему серверу Discord:**

<a href="https://discord.gg/CzwbMCPEZa ">
  <img src="./resources/images/icon_clyde_blurple_RGB.png" alt="Иконка" width="75">
</a>

**Если вы предпочитаете использовать Matrix (через мост к Discord):**

[<img src="https://matrix.org/images/matrix-logo.svg ">](https://matrix.to/ #/uad-ng:matrix.org)

## Кратко

Это отдельный форк [проекта UAD](https://github.com/0x192/universal-android-debloater ), цель которого — улучшить приватность и автономность устройства путём удаления ненужных и малопонятных системных приложений.
Это также может повысить безопасность за счёт уменьшения (но не полного устранения) [атакуемой поверхности](https://en.wikipedia.org/wiki/Attack_surface ). Подробнее о начале работы можно узнать в [нашей Вики](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/wiki ). Хотя UAD-ng может удалять системные приложения, он не способен обнаруживать или удалять потенциально вредоносные системные службы или драйверы, прошитые в прошивку вашего устройства различными производителями; некоторые специфичные для поставщиков приложения являются лишь интерфейсом для системных служб, предоставляемых самим поставщиком, поэтому их отключение или удаление не остановит работу службы. Дополнительную информацию вы можете найти в описаниях пакетов внутри приложения Universal Android Debloater Next Generation.

## Документация

Для получения документации по использованию UAD-ng, часто задаваемым вопросам (FAQ), сборке из исходников и извлечению APK-файлов см. [нашу Вики](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation/wiki ).

## Особая благодарность

- [@0x192](https://github.com/0x192 ) за создание оригинального проекта UAD.
- [@mawilms](https://github.com/mawilms ) за его менеджер плагинов LotRO ([Lembas](https://github.com/mawilms/lembas )), который помог понять, как использовать библиотеку GUI [Iced](https://github.com/hecrj/iced ).
- [@casperstorm](https://github.com/casperstorm ) за вдохновение в дизайне интерфейса.

# Инструкция по русификации и сборке

``` bash

# Склонировать изначальную репу и перейти в неё

  git clone https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation

  cd universal-android-debloater-next-generation

# Установить инструменты разработчика

  paru -S rust clang mold

# Поменять в Cargo.toml зависимость ureq на версию 2.7, а то не соберется

# Подменить uad_lists.json из этого репозитория в склонированный в universal-android-debloater-next-generation/resources/assets

# Сборка утилиты

cargo build --release

# Установка утилиты в  ~/.cargo/bin/

cargo install --path . --config 'build.rustflags="-C target-cpu=native"'

```

## Дополнительные файлы

**Файлы:**
1. json2txt.py - извлечение из файла ресурсов описания
2. txt2json.py - загрузка в JSON описаний
3. uad_lists.json - переведенный на русский язык файл ресурсов

**Путь до файла ресурса:** 
