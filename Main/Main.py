import PySimpleGUI as sg
import Crawler

if __name__ == '__main__':
    Crawler.execute()

    layout = [
        [sg.Text('*'*130)],
        [sg.Text("Enter phrase:", font=5), sg.Input(s=70, key='-phrase-')],
        [sg.Text("Enter number of letters surrounding the phrase: ", font=5), sg.Input(5, s=3, font=5, key='-number_of_letters-')],
        [sg.Text("\n")],
        [sg.HSep()],
        [sg.Text("\n")],
        [sg.Text("Article link: ", font=5), sg.Output(font=5, key='-article_link-')],
        [sg.Text("Found section: ", font=5), sg.Output(size=(42,10), font=5, key='-found_section-')],
        [sg.Push(), sg.Button('Search', size=(10, 2), font=5, enable_events=True), sg.Push()]
    ]

    window = sg.Window("Speechalizer", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Closed":
            break
        if event == "Search":
            phrase = values['-phrase-']
            number_of_letters = values['-number_of_letters-']
            article_link, found_section = Crawler.find_context(Crawler.ALL_SPEECHES, Crawler.ALL_ARTICLES, phrase, int(number_of_letters))
            window['-article_link-'].update(article_link)
            window['-found_section-'].update(found_section)
    window.close()
