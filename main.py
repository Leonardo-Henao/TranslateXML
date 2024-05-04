import xml.etree.ElementTree as ET
from translate import Translator
from sys import argv


def show_help():
    print(
        """

        Hi, missing parameters.

        use pyhton main.py [to_language] [from_language] [path_file]

        Example:
        python main.py pt es test.xml_copy

        ---------------------------------------------------------------

        Remember visit me https://leonardohenao.com
        
        Can I count on you for a coffee refill?
        refill here -> https://ko-fi.com/lhenaoll

        Thanks!


        """
    )


try:
    if argv[1] == "-h":
        show_help()
        exit()

    translator = Translator(to_lang=argv[1], from_lang=argv[2])
    path_file = argv[3]
except Exception:
    show_help()
    exit()


def start():
    data_xml = ET.parse(path_file)
    xml_copy = data_xml

    total = len(xml_copy.getroot())
    count = 0

    for child in xml_copy.getroot():
        count += 1
        print("Progress: ", count, "/", total, "...", end="\r")

        try:
            child.text = translator.translate(child.text)
        except Exception as e:
            print("Error: ", e)
            break

    print("Process as finished! Total words translated: ", count, " of ", total)
    with open("translated.xml", "w") as f:
        all_data = ET.tostring(xml_copy.getroot(), "utf-8").decode("utf-8")
        f.write(all_data)


if __name__ == "__main__":
    start()
