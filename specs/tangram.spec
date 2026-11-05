@	
s	app	Run the app
s	migrate	Migrate your app database
s	predict	Make predictions with a model
s	train	Train a model
o	--help|-h	Print help information	
o	--version|-v	Print version information	
@	app
o	-c|--config	The path to a config file	v
=	app	-c
t	filepaths
@	migrate
o	--database-url		v
@	predict
o	-f|--file	The path to read examples from, defaults to stdin	v
o	-m|--model	The path to the model to make predictions with	v
o	-o|--output	The path to write the predictions to, defaults to stdout	v
o	-p|--probabilities	Output probabilities instead of class labels, only relevant for classifier models	v
=	predict	-f
t	filepaths
=	predict	-m
t	filepaths
=	predict	-o
t	filepaths
@	train
o	-c|--config	The path to a config file	v
o	-f|--file	The path to your .csv file	v
o	--file-test	The path to your .csv file used for testing	v
o	--file-train	The path to your .csv file used for training	v
o	-o|--output	The path to write the .tangram file to	v
o	-t|--target	The name of the column to predict	v
=	train	-c
t	filepaths
=	train	-f
t	filepaths
=	train	--file-test
t	filepaths
=	train	--file-train
t	filepaths
=	train	-o
t	filepaths
