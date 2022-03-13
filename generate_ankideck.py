import genanki


my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

#Initialize an Anki Deck
my_deck = genanki.Deck(
  2059400110,
  'Country Capitals')


my_note = genanki.Note(
  model=my_model,
  fields=['Capital of Argentina', 'Buenos Aires'])


my_deck.add_note(my_note)


#Export to Anki
genanki.Package(my_deck).write_to_file('output.apkg')