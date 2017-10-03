# Prints posts and comments from Change My View Reddit threads into separate
# files

from __future__ import print_function

import json, requests
import praw

print (praw.__file__)

r = praw.Reddit(client_id="GIJBIBgfQUyw9A",
				client_secret="Li4pVwUrrnGM6h86d9VmVcZKSzU",
				user_agent="url scraper")

sub = r.subreddit("changemyview")

f = 0
limit = input("Limit ")


# Print posts and comments to individual file
for submission in sub.hot(limit=limit) :
	title = submission.title


	if title[0:3] == "CMV" :
		outfile = open(str(f) + ".txt", "w")

		# Print original post
		outfile.write(submission.title.upper() + "\n")
		outfile.write("ID: " + submission.id + "\n")
		outfile.write("Original Post" + "\n")
		outfile.write("Author: " + str(submission.author) + "\n\n")
		outfile.write(json.dumps(submission.selftext) + "\n") # original post
		outfile.write("_______________\n\n")

		outfile.close()
		
		f += 1

		submission.comments.replace_more(limit=None)
		for comment in submission.comments :
			# new file for every root reply
			outfile = open(str(f) + ".txt", "w")


			# root reply
			outfile.write(submission.title.upper() + "\n")
			outfile.write("ID: " + comment.id + "\n")
			outfile.write("Author: " + str(comment.author) + "\n\n")
			outfile.write(json.dumps(comment.body) + "\n")
			outfile.write("_______________\n\n")

			outfile.close()

			# increment file name
			f += 1


			for reply in comment.replies :
				# next layer of responses

				outfile = open(str(f) + ".txt", "w")

				outfile.write(submission.title.upper() + "\n")
				outfile.write("ID: " + reply.id + "\n")
				outfile.write("Author: " + str(reply.author) + "\n\n")
				outfile.write(json.dumps(reply.body) + "\n") 
				outfile.write("______________\n\n")

				outfile.close()

				f += 1



	



