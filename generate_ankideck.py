import genanki
import fetch_notion_db
import fetch_wiki_summary

data=fetch_notion_db.main()
querys=fetch_wiki_summary.yield_querys(data) #This is a generator


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
  'Notion Deck')


for elt in querys:
    my_note = genanki.Note(
      model=my_model,
      fields=[elt['question'], elt['answer']])
    my_deck.add_note(my_note)
    
#Create a new Anki Package


#Export to Anki
genanki.Package(my_deck).write_to_file('output.apkg')