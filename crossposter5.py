import praw
import pyimgur
import time
import datetime


#SET UP
        #Reddit info
username = ('the_karma_llama')
password = ('rt4YgVR5Sn#6')
client_id = ('y2LXRBjyISoodQ')
client_secret = ('rHPzSj2n_AGP4bfYcz33HPQY1ng')

        #Imgur info
Imgur_username = ('thekarmallama1')
Imgur_password = ('Regri05s')
Imgur_client_id = ('3431c3145229af2')
Imgur_client_secret = ('3ae9bc28acbccb7dab5d49878f721694269d990b')

'''New Code Starts here - Developed bu lancelot Albion'''
# This function takes a post and crossposts it to another subreddit
# subredditName - The new subreddit in which the post should be posted to 
# submissionPost - A unique id like 'bcs1g4' for the post which needs to be cross posted. You can find this id in the URL or if you posted it using PRAW API it will be returned to you via code
# title - In case you need a custom title for your crosspost
# flair_template_id - If the subreddit has various flair template decide which one to use
# flair_text - Text which should be posted in flair 
def crossPost(subredditName, submissionPostId, title = '', flair_text = '', flair_number = '' ) :
    result = api.submission(id = submissionPostId).crosspost(subredditName, title= title, send_replies=False)
#    print(result.author.name + ' Posted it successfully.  Post id = ' + str(result))
    if(flair_text):
        all_choices = result.flair.choices()
        for i in range(0, len(all_choices)):
                ()
        print(all_choices)
        template_id = all_choices[int(flair_number)]['flair_template_id']        
        result.flair.select(template_id, flair_text)
    else:
        print('Flair not set, so ignore')
    return result
    
# Add a comment to a post
# submissionId - The ID of the post which goes like 'bcs1g4' this
# comment - the comment string 
def addComment(submissionId, comment):
    submission = api.submission(id = submissionId)
    submission.reply(comment)
    
    
# Setting a flair also requires you mention the flair template id, that can be queried using this
# The template id will be printed which you can later hard code into your code after some trial runs
# postId -The ID of the post which goes like 'bcs1g4' this 
def getSubmissionFlair(postId):
    flairChoices = api.submission(id = postId).link_flair_template_id
    print('Flair template ID = '+ str(flairChoices))
    flairChoices = api.submission(id = postId).link_flair_text
    print('Flair text = '+str(flairChoices))
    
    
'''New Code ends here - Developed by lancelot Albion'''
        #Going through my Reddit user's API
api = praw.Reddit(username = username,
                password = password,
                client_id = client_id,
                client_secret = client_secret,
                user_agent = '1am xpost bot by u/the_karma_llama')

        #Going through my Imgur user's API
imgur_api = pyimgur.Imgur(Imgur_client_id)



#THE SUBMISSION
def Submission (Title, subreddit, Url):
    print('Starting upload...')

        #Upload image to imgur
    upload_image = imgur_api.upload_image(Url, title = Title)
    time.sleep(15)
    
    imgur_link = (upload_image.link)
    print('Successfully uploaded ' + upload_image.title + ' to Imgur!')
    print('Posting to Reddit...')
    
    #Post to reddit
    uniquePostId = api.subreddit(subreddit).submit(Title, url=imgur_link)
    # I need the post URL to crosspost it.
    print('Successfully posted ' + Title + ' to r/' + subreddit +'!')
    
    # Using Praw user can post only once. After that you have to wait some time which depends on the karma of your account. So change the sleep time accordingly
    print ('Retrieving original post ID...')
    time.sleep(15)
    return uniquePostId
    print ('Done. Crossposting...')    
    

#if __name__ == "__main__":

    # Don't forget to double up the backslashes
#    postId = Submission ('A Bandit wasp close-up', 'discoverearth', 'wasp.jpg')
    
    
    #Cross post to another subreddit
#    crossPost1Id = crossPost(subredditName = 'Discoverearthama', submissionPostId = postId, title= 'xpost from discovereath Fuego Volcano & Milky Way by u/Furfural')
#    print ('Successfully crossposted!')

    # Add comment to the crosspost content
#    addComment(crossPost1Id, 'Source: Shauns Wildlife Photography on Flickr: https://www.flickr.com/photos/shaundickinson/6185074831/')
#    print ('Comment submitted!')
    
    #Cross post to another subreddit WITH flair
#    crossPost2Id = crossPost(subredditName = 'discoverearthama', submissionPostId = postId, title= 'A Bandit wasp close-up', flair_text= 'pic', flair_number = '0')
#    print ('Successfully crossposted with flair!')

    # Add comment to the crosspost content
#    addComment(crossPost2Id, 'Source: Shauns Wildlife Photography on Flickr: https://www.flickr.com/photos/shaundickinson/6185074831/')
#    print ('Comment submitted!')

#   print ('Done!')


# If you want to submit with a flair, go into the subreddit beforehand and see the list.
# You need to put in the flairs number. See examples below.

'''
r/Woahdude flairs
0. picture
1. wallpaper
2. gifv
3. audio
4. music
5. musicvideo
6. video
7. woahdudeapproved
8. game
9. interactive
10. text
'''

# Submission ('Title', 'Subreddit', 'Filepath')
# Crosspost no flair ('Subreddit Xpost', submissionPostId = postId, 'Title')
# addComment (crossPostID, 'Comment body')
# Crosspost with flair ('Subreddit Xpost', submissionPostId = postId, 'Title', 'Flair name', 'Flair number')
# addcomment (crosspostID, 'Comment body')

now = datetime.datetime.now()
today = str(now.strftime("%d/%m"))

if __name__ == "__main__":
    
    postId = Submission (
        Title = 'A bandit wasp close-up',
        subreddit = 'discoverearth',
        Url = 'wasp.jpg'
            )
        
#    crossPost1Id = crossPost(
#        subredditName = 'Discoverearthama',
#        submissionPostId = postId,
#        title= 'xpost from discovereath Fuego Volcano & Milky Way by u/Furfural'
#            )
#    addComment(crossPost1Id,
#        'Source: Shauns Wildlife Photography on Flickr: https://www.flickr.com/photos/shaundickinson/6185074831/'
#            )
        
    crossPost2Id = crossPost(
        subredditName = 'discoverearthama',
        submissionPostId = postId,
        title= 'A Bandit wasp close-up',
        flair_text= 'pic',
        flair_number = '0'
            )
    addComment(crossPost2Id,
        'Source: Shauns Wildlife Photography on Flickr: https://www.flickr.com/photos/shaundickinson/6185074831/'
                   )


print ('Done!')
