import codecs


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    """
    Функція читає HTML файл, видаляє HTML теги та після чого записує очищений текст у текстовий файл

    Args:
        html_file: файл draft.html
        result_file: 'cleaned.txt' -> файл, в який буде записуватись очищений текст
    """
    try:
        with codecs.open(html_file, 'r', 'utf-8') as infile, codecs.open(result_file, 'w', 'utf-8') as outfile:
            in_tag: bool = False
            for line in infile:
                cleaned_line: str = ""
                for char in line:
                    if char == '<':
                        in_tag = True
                    elif char == '>':
                        in_tag = False
                    elif not in_tag:
                        cleaned_line += char
                if cleaned_line.strip():
                    outfile.write(cleaned_line)
        print(f"Файл '{html_file}' очищено та збережено у '{result_file}'")
    except FileNotFoundError:
        print(f"Помилка! Файл '{html_file}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")


delete_html_tags('draft.html')
