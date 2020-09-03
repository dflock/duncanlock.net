:title: Textmate & Sublimetext do Syntax Highlighting Wrong
:slug: textmate-sublimetext-do-syntax-highlighting-wrong
:date: 2013-11-08 02:19:58
:tags: rant, editor wars, sublimetext

They mix content with presentation:

The syntax definition includes the visual presentation - the colours - as well and a description of the language.

There should be one central syntax definition that everyone can hack on and improve. Then the theme would just be a list of colours for each syntax element defined by the syntax definition file.

Currently each theme caries it's own copy of all the syntax definitions around. This is obviously wastefull - but it also leads to inconsistencies and to themes 'not supporting' some languages.

It also makes theme files much larger than they should be.