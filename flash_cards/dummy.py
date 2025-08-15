import pandas

data_frame=pandas.read_csv('data/french_words.csv')
french_list=data_frame['french'].to_list()
english_list=data_frame['english'].to_list()
final=[{item1:item2} for item1 in french_list for item2 in english_list]
print(final)